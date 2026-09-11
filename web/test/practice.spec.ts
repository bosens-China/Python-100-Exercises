import { test, expect, type Page } from '@playwright/test'
import { execFileSync } from 'node:child_process'
import type { Course, Files } from '../src/types'
const solutions: Record<string, Files> = JSON.parse(
  execFileSync(
    process.env.PYTHON ?? 'python3',
    [
      '-c',
      'import json; from tools.course import load_course, sources; print(json.dumps({e["id"]: sources(e, "solution") for e in load_course()[1]}))',
    ],
    { cwd: '..', encoding: 'utf8' },
  ),
)
const production = 'http://127.0.0.1:4173/Python-100-Exercises/'
async function edit(page: Page, source: string) {
  const editor = page.locator('.cm-content')
  await editor.click()
  await editor.press('ControlOrMeta+a')
  await editor.fill(source)
}

test('100 道参考实现全部通过，100 道起始代码全部未通过（真实浏览器 Worker）', async ({
  page,
}) => {
  test.setTimeout(240_000)
  await page.goto('/')
  const outcome = await page.evaluate(
    async ({ solutions }) => {
      const path = '/src/runtime/client.ts'
      const { PythonRunner } = (await import(
        /* @vite-ignore */ path
      )) as typeof import('../src/runtime/client')
      const runner = new PythonRunner(() => {})
      const course: Course = await fetch('/course.json').then((response) =>
        response.json(),
      )
      const errors: string[] = []
      let checks = 0
      try {
        for (const exercise of course.exercises) {
          const correct = await runner.run(
            exercise,
            solutions[exercise.id],
            'submit',
          )
          checks += correct.passed_count
          if (!correct.passed)
            errors.push(`${exercise.id} reference: ${JSON.stringify(correct)}`)
          const starter = await runner.run(exercise, exercise.files, 'submit')
          if (starter.passed || starter.content_error)
            errors.push(`${exercise.id} starter: ${JSON.stringify(starter)}`)
        }
      } finally {
        runner.cancel()
      }
      return { errors, checks }
    },
    { solutions },
  )
  expect(outcome.errors).toEqual([])
  expect(outcome.checks).toBe(329)
})

test('生产子路径：做题、保存、完成状态、刷新、重置和备份', async ({ page }) => {
  await page.goto(`${production}#/exercises/001`)
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
  await edit(page, solutions['001']['main.py'])
  await page.getByRole('button', { name: '运行示例', exact: true }).click()
  await expect(page.getByText('示例检查通过', { exact: true })).toBeVisible({
    timeout: 90000,
  })
  await expect(page.locator('.learning-progress strong')).toHaveText('0 / 100')
  await page.getByRole('button', { name: '提交检查', exact: true }).click()
  await expect(page.getByText('全部通过，继续前进！')).toBeVisible()
  await expect(page.locator('.learning-progress strong')).toHaveText('1 / 100')
  await page.reload()
  await expect(page.locator('.cm-content')).toContainText('def ')
  await expect(page.locator('.learning-progress strong')).toHaveText('1 / 100')
  const backup = page.waitForEvent('download')
  await page.getByRole('button', { name: '导出记录' }).click()
  const download = await backup
  const backupPath = await download.path()
  await edit(page, `${solutions['001']['main.py']}\n# changed`)
  await expect(page.locator('.learning-progress strong')).toHaveText('0 / 100')
  await page.locator('input[type=file]').setInputFiles({
    name: 'broken.json',
    mimeType: 'application/json',
    buffer: Buffer.from('{"schema":0}'),
  })
  await expect(
    page.getByText('这不是当前课程版本的有效学习记录。'),
  ).toBeVisible()
  await expect(page.locator('.cm-content')).toContainText('# changed')
  await page.locator('input[type=file]').setInputFiles(backupPath!)
  await page.getByRole('button', { name: '替换并导入' }).click()
  await expect(page.locator('.learning-progress strong')).toHaveText('1 / 100')
  await page.getByRole('button', { name: '重置本题' }).click()
  await page
    .getByRole('button', { name: '重置本题', exact: true })
    .last()
    .click()
  await expect(page.locator('.learning-progress strong')).toHaveText('0 / 100')
  await page.reload()
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
  await page.screenshot({ path: 'test-results/desktop-light.png' })
  await page.getByRole('button', { name: '主题设置' }).click()
  await page.getByRole('menuitem', { name: '主题 · 深色' }).click()
  await page.reload()
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark')
  await page.screenshot({ path: 'test-results/desktop-dark.png' })
  await page.goto(`${production}#/exercises/100`)
  await expect(page.getByRole('tab')).toHaveCount(
    Object.keys(solutions['100']).length,
  )
  await page.getByRole('tab').last().click()
  await page.reload()
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
  await page.goto(`${production}#/exercises/999`)
  await expect(page.getByText('没有这道题')).toBeVisible()
})

test('错误、语法异常、输出限制、超时、停止后恢复', async ({ page }) => {
  await page.goto('/')
  const outcomes = await page.evaluate(async () => {
    const path = '/src/runtime/client.ts'
    const { PythonRunner } = (await import(
      /* @vite-ignore */ path
    )) as typeof import('../src/runtime/client')
    const runner = new PythonRunner(() => {})
    const course: Course = await fetch('/course.json').then((response) =>
      response.json(),
    )
    const exercise = {
      ...course.exercises[0],
      tests: 'def test_value():\n    assert student.answer() == 42',
    }
    const syntax = await runner.run(
      exercise,
      { 'main.py': 'def nope(' },
      'submit',
    )
    const exception = await runner.run(
      exercise,
      { 'main.py': 'raise ValueError("broken")' },
      'submit',
    )
    const output = await runner.run(
      exercise,
      { 'main.py': 'def answer():\n    while True: print("x" * 1000)' },
      'submit',
    )
    let timeout = ''
    try {
      await runner.run(
        exercise,
        { 'main.py': 'def answer():\n    while True: pass' },
        'submit',
      )
    } catch (error) {
      timeout = String(error)
    }
    const stopped = runner
      .run(
        exercise,
        { 'main.py': 'def answer():\n    while True: pass' },
        'submit',
      )
      .catch((error: unknown) => String(error))
    setTimeout(() => runner.cancel(), 500)
    const stop = await stopped
    const recovery = await runner.run(
      exercise,
      { 'main.py': 'def answer():\n    return 42' },
      'submit',
    )
    runner.cancel()
    return { syntax, exception, output, timeout, stop, recovery }
  })
  expect(outcomes.syntax.passed).toBe(false)
  expect(outcomes.syntax.cases[0].message).toContain('SyntaxError')
  expect(outcomes.exception.cases[0].message).toContain('ValueError')
  expect(outcomes.output.cases[0].stdout.length).toBeLessThanOrEqual(32000)
  expect(outcomes.output.cases[0].message).toContain('OutputLimitExceeded')
  expect(outcomes.timeout).toContain('10 秒')
  expect(outcomes.stop).toContain('已停止')
  expect(outcomes.recovery.passed).toBe(true)
})

test('运行资源加载失败可重试', async ({ page }) => {
  await page.route('**/runtime/pyodide.mjs', (route) => route.abort())
  await page.goto(production)
  await edit(page, solutions['001']['main.py'])
  await page.getByRole('button', { name: '提交检查', exact: true }).click()
  await expect(
    page.getByRole('button', { name: '重试', exact: true }),
  ).toBeVisible({ timeout: 20000 })
  await page.unroute('**/runtime/pyodide.mjs')
  await page.getByRole('button', { name: '重试', exact: true }).click()
  await expect(page.getByText('全部通过，继续前进！')).toBeVisible({
    timeout: 90000,
  })
})

test('运行时编辑器保持响应，停止后可重新提交', async ({ page }) => {
  await page.goto(production)
  await edit(page, 'while True: pass')
  await page.getByRole('button', { name: '提交检查', exact: true }).click()
  await expect(
    page.getByRole('button', { name: '停止运行', exact: true }),
  ).toBeVisible()
  await edit(page, solutions['001']['main.py'])
  await page.getByRole('button', { name: '停止运行', exact: true }).click()
  await expect(page.getByText('已停止运行，代码已保留。')).toBeVisible()
  await page.getByRole('button', { name: '提交检查', exact: true }).click()
  await expect(page.getByText('全部通过，继续前进！')).toBeVisible({
    timeout: 90000,
  })
})

test('课程加载失败显示重试，损坏存储不被自动覆盖', async ({ page }) => {
  await page.route('**/course.json', (route) => route.abort())
  await page.goto(production)
  await expect(page.getByText('暂时无法打开课程')).toBeVisible()
  await page.unroute('**/course.json')
  await page.getByRole('button', { name: '重新加载' }).click()
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
  await page.addInitScript(() =>
    localStorage.setItem('python100.progress.python-100-v2', '{broken'),
  )
  await page.reload()
  await expect(page.getByText(/自动保存已暂停/)).toBeVisible()
  await edit(page, solutions['001']['main.py'])
  await expect
    .poll(() =>
      page.evaluate(() =>
        localStorage.getItem('python100.progress.python-100-v2'),
      ),
    )
    .toBe('{broken')
})
