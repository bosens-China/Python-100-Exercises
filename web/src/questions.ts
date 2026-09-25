const exerciseFiles = import.meta.glob('../../part_*/exercise_*.py', { query: '?raw', import: 'default', eager: true }) as Record<string, string>
const testFiles = import.meta.glob('../../part_*/test_exercise_*.py', { query: '?raw', import: 'default', eager: true }) as Record<string, string>

export const modules = [
  { id: 'syntax', name: '语法与函数入门', start: 1, end: 10 },
  { id: 'collections', name: '字符串与容器', start: 11, end: 20 },
  { id: 'control', name: '控制流与数据处理', start: 21, end: 30 },
  { id: 'oop', name: '面向对象', start: 31, end: 35 },
  { id: 'files', name: '文件与综合练习', start: 36, end: 40 },
  { id: 'tools', name: '网络、日期与常用工具', start: 41, end: 50 },
  { id: 'api', name: 'Web API 起步', start: 51, end: 60 },
  { id: 'persistence', name: '数据库与项目结构', start: 61, end: 72 },
  { id: 'auth', name: '认证与授权', start: 73, end: 85 },
  { id: 'engineering', name: '交付与工程实践', start: 86, end: 100 },
] as const

export type Question = {
  id: number
  title: string
  prompt: string
  starter: string
  tests: string
  module: typeof modules[number]
  kind: 'independent' | 'project'
}

export const questions: Question[] = Object.entries(exerciseFiles).map(([path, source]): Question => {
  const id = Number(path.match(/exercise_(\d{3})\.py$/)?.[1])
  const doc = source.match(/^\s*"""([\s\S]*?)"""/)
  const lines = doc?.[1].trim().split(/\r?\n/) ?? []
  const module = modules.find((item) => id >= item.start && id <= item.end)
  if (!module || !doc) throw new Error(`题目格式错误：${path}`)
  const title = lines.shift()?.replace(/^题目\s+\d+:\s*/, '') ?? ''
  const testPath = path.replace('/exercise_', '/test_exercise_')
  return {
    id,
    title,
    prompt: lines.join('\n').trim(),
    starter: source.slice(doc[0].length).trim() || `# ${title}\n`,
    tests: testFiles[testPath] ?? '暂无测试文件',
    module,
    kind: id <= 50 || (id >= 96 && id <= 98) ? 'independent' : 'project',
  }
}).sort((a, b) => a.id - b.id)

if (questions.length !== 100 || questions.some((item, index) => item.id !== index + 1)) {
  throw new Error('题目必须连续编号 001–100')
}
