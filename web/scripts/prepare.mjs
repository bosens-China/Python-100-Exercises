import { spawnSync } from 'node:child_process'
import { copyFile, mkdir, readdir } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

const web = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const root = resolve(web, '..')
const python =
  process.env.PYTHON ?? (process.platform === 'win32' ? 'python' : 'python3')
const result = spawnSync(
  python,
  ['-m', 'tools.course', 'export', 'web/public/course.json'],
  {
    cwd: root,
    stdio: 'inherit',
  },
)
if (result.error) throw result.error
if (result.status !== 0) process.exit(result.status ?? 1)
const runtime = resolve(web, 'public/runtime')
await mkdir(runtime, { recursive: true })
await copyFile(resolve(root, 'tools/grader.py'), resolve(runtime, 'grader.py'))
const pyodide = resolve(web, 'node_modules/pyodide')
for (const name of await readdir(pyodide)) {
  if (/\.(mjs|wasm|zip|json)$/.test(name) && name !== 'package.json') {
    await copyFile(resolve(pyodide, name), resolve(runtime, name))
  }
}
console.log('题库与 Python 执行资源已准备。')
