import { useEffect, useMemo, useState } from 'react'
import { Alert, Button, ConfigProvider, Drawer, Input, Progress, Select, Space, Tag, Typography } from 'antd'
import { modules, questions, type Question } from './questions'
import { runBrowserTests, type TestResult } from './runner'
import './App.css'

const storageKey = 'python-100-progress-v1'
type Saved = Record<number, { code: string; done: boolean }>

function loadSaved(): Saved {
  try {
    const value: unknown = JSON.parse(localStorage.getItem(storageKey) || '{}')
    if (!value || typeof value !== 'object' || Array.isArray(value)) return {}
    return Object.fromEntries(Object.entries(value).filter(([id, item]) =>
      Number(id) >= 1 && Number(id) <= 100 && item && typeof item === 'object' && typeof item.code === 'string' && typeof item.done === 'boolean'
    )) as Saved
  } catch {
    return {}
  }
}

function App() {
  const [saved, setSaved] = useState<Saved>(loadSaved)
  const [currentId, setCurrentId] = useState(1)
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [query, setQuery] = useState('')
  const [moduleId, setModuleId] = useState<string>('all')
  const [tab, setTab] = useState<'prompt' | 'tests'>('prompt')
  const [running, setRunning] = useState(false)
  const [results, setResults] = useState<TestResult[] | null>(null)
  const [runError, setRunError] = useState('')
  const current = questions[currentId - 1]
  const code = saved[currentId]?.code ?? current.starter
  const doneCount = Object.values(saved).filter((item) => item.done).length

  useEffect(() => {
    try {
      localStorage.setItem(storageKey, JSON.stringify(saved))
    } catch {
      // The exercise remains usable when browser storage is unavailable.
    }
  }, [saved])

  const visible = useMemo(() => questions.filter((item) => {
    const inModule = moduleId === 'all' || item.module.id === moduleId
    const matches = `${item.title} ${item.id} ${String(item.id).padStart(3, '0')} ${item.module.name}`.toLowerCase().includes(query.trim().toLowerCase())
    return inModule && matches
  }), [moduleId, query])

  function updateCurrent(changes: Partial<Saved[number]>) {
    setSaved((previous) => ({
      ...previous,
      [currentId]: { code: previous[currentId]?.code ?? current.starter, done: previous[currentId]?.done ?? false, ...changes },
    }))
  }

  function selectQuestion(question: Question) {
    setCurrentId(question.id)
    setDrawerOpen(false)
    setTab('prompt')
    setResults(null)
    setRunError('')
  }

  async function runCurrent() {
    setRunning(true)
    setResults(null)
    setRunError('')
    try {
      const nextResults = await runBrowserTests(current.id, code, current.tests)
      setResults(nextResults)
      if (nextResults.length > 0 && nextResults.every((result) => result.passed)) updateCurrent({ done: true })
    } catch (error) {
      setRunError(error instanceof Error ? error.message : String(error))
    } finally {
      setRunning(false)
    }
  }

  return <ConfigProvider theme={{ token: { colorPrimary: '#2563eb', borderRadius: 10, fontFamily: 'Inter, system-ui, sans-serif' } }}>
    <div className="app-shell">
      <header className="topbar">
        <div className="brand flex items-center gap-2">
          <span className="brand-mark">Py</span>
          <div><strong>Python 100</strong><small>初级工程师实战练习</small></div>
        </div>
        <div className="topbar-progress">
          <span>{doneCount} / {questions.length} 已完成</span>
          <Progress percent={doneCount} showInfo={false} size="small" />
        </div>
        <Button disabled={running} onClick={() => setDrawerOpen(true)}>题目目录</Button>
      </header>

      <main className="workspace">
        <section className="prompt-pane">
          <div className="pane-head">
            <Space size={8} wrap>
              <Tag color="blue">{String(current.id).padStart(3, '0')}</Tag>
              <Tag>{current.module.name}</Tag>
              <Tag color={current.kind === 'project' ? 'gold' : 'green'}>{current.kind === 'project' ? '连续项目' : '独立练习'}</Tag>
            </Space>
            <div className="pane-nav flex gap-2">
              <Button size="small" disabled={running || currentId === 1} onClick={() => selectQuestion(questions[currentId - 2])}>上一题</Button>
              <Button size="small" disabled={running || currentId === questions.length} onClick={() => selectQuestion(questions[currentId])}>下一题</Button>
            </div>
          </div>
          <Typography.Title level={2} className="question-title">{current.title}</Typography.Title>
          <div className="tabbar" role="tablist" aria-label="题目内容">
            <button className={tab === 'prompt' ? 'active' : ''} onClick={() => setTab('prompt')} role="tab" aria-selected={tab === 'prompt'}>题目说明</button>
            <button className={tab === 'tests' ? 'active' : ''} onClick={() => setTab('tests')} role="tab" aria-selected={tab === 'tests'}>现有测试</button>
          </div>
          <div className="prompt-content">
            {tab === 'prompt' ? <>
              <div className="prompt-text">{current.prompt}</div>
              {current.kind === 'project' && <Alert type="info" showIcon message="连续项目题" description="本题需要在本地仓库持续修改 FastAPI 项目。页面保存你的草稿和进度；请在本地运行对应的 pytest 测试。" />}
            </> : <pre className="test-source">{current.tests}</pre>}
          </div>
        </section>

        <section className="editor-pane">
          <div className="editor-head"><div><strong>{current.kind === 'project' ? '项目笔记 / 代码草稿' : '你的代码'}</strong><small>自动保存在当前浏览器</small></div><Tag>Python 3.12+</Tag></div>
          <label className="sr-only" htmlFor="solution-editor">Python 代码编辑器</label>
          <textarea id="solution-editor" spellCheck={false} disabled={running} value={code} onChange={(event) => { updateCurrent({ code: event.target.value, done: false }); setResults(null) }} />
          {(results || runError) && <div className="results" role="status">
            {runError ? <Alert type="error" showIcon message={runError} /> : <>
              <strong>{results?.every((result) => result.passed) ? '测试通过' : '测试未通过'} · {results?.filter((result) => result.passed).length}/{results?.length}</strong>
              {results?.map((result) => <div key={result.name} className={result.passed ? 'result-pass' : 'result-fail'}>{result.passed ? '✓' : '×'} {result.name}{result.message && <span> — {result.message}</span>}</div>)}
            </>}
          </div>}
          <div className="editor-footer">
            <span>进度只保存在此浏览器，不会上传</span>
            <Space>
              <Button disabled={running} onClick={() => { updateCurrent({ code: current.starter, done: false }); setResults(null) }}>重置</Button>
              {current.kind === 'independent'
                ? <Button type="primary" loading={running} onClick={runCurrent}>运行测试</Button>
                : <Button type={saved[currentId]?.done ? 'default' : 'primary'} onClick={() => updateCurrent({ done: !saved[currentId]?.done })}>{saved[currentId]?.done ? '取消完成' : '标记完成'}</Button>}
            </Space>
          </div>
        </section>
      </main>

      <Drawer title="100 道练习" placement="left" width={380} open={drawerOpen} onClose={() => setDrawerOpen(false)}>
        <div className="catalog-controls grid gap-2">
          <Input.Search placeholder="搜索题号或标题" value={query} onChange={(event) => setQuery(event.target.value)} allowClear />
          <Select value={moduleId} onChange={setModuleId} options={[{ value: 'all', label: '全部模块' }, ...modules.map((item) => ({ value: item.id, label: `${item.name} · ${item.start}–${item.end}` }))]} />
        </div>
        <div className="catalog-list">
          {visible.map((item, index) => <div key={item.id}>
            {(index === 0 || visible[index - 1].module.id !== item.module.id) && <div className="module-heading">{item.module.name}<span>{item.module.start}–{item.module.end}</span></div>}
            <button disabled={running} className={`catalog-item ${item.id === currentId ? 'selected' : ''}`} onClick={() => selectQuestion(item)}>
            <span className="catalog-number">{String(item.id).padStart(3, '0')}</span>
            <span className="catalog-title">{item.title}</span>
            <span className={`catalog-status ${saved[item.id]?.done ? 'done' : ''}`} aria-label={saved[item.id]?.done ? '已完成' : '未完成'}>{saved[item.id]?.done ? '✓' : '○'}</span>
            </button>
          </div>)}
        </div>
      </Drawer>
    </div>
  </ConfigProvider>
}

export default App
