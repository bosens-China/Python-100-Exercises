import type { PyodideInterface } from 'pyodide'
import type { RunRequest, WorkerResponse } from '@/types'

let engine: Promise<PyodideInterface> | undefined
const send = (message: WorkerResponse) => postMessage(message)

async function initialize(runtimeURL: string) {
  const { loadPyodide } = (await import(
    /* @vite-ignore */ `${runtimeURL}pyodide.mjs`
  )) as typeof import('pyodide')
  const pyodide = await loadPyodide({
    indexURL: runtimeURL,
    stdout: () => {},
    stderr: () => {},
  })
  const response = await fetch(`${runtimeURL}grader.py`)
  if (!response.ok) throw new Error('判题资源加载失败，请重试。')
  pyodide.runPython(await response.text())
  pyodide.runPython(`
import json as _json

def _run_request(raw):
    request = _json.loads(raw)
    tests = request['tests']
    if request['mode'] == 'example':
        tree = ast.parse(tests)
        first = next(node.name for node in tree.body if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'))
        tree.body = [node for node in tree.body if not (isinstance(node, ast.FunctionDef) and node.name.startswith('test_') and node.name != first)]
        tests = ast.unparse(tree)
    return _json.dumps(grade(request['files'], tests, request['entrypoint']), ensure_ascii=False)
`)
  return pyodide
}

self.onmessage = async (event: MessageEvent<RunRequest>) => {
  const request = event.data
  try {
    if (!engine) {
      send({ type: 'status', id: request.id, status: 'loading' })
      engine = initialize(request.runtimeURL)
    }
    const pyodide = await engine
    send({ type: 'status', id: request.id, status: 'running' })
    pyodide.globals.set('_request_json', JSON.stringify(request))
    try {
      const json = await pyodide.runPythonAsync('_run_request(_request_json)')
      if (typeof json !== 'string')
        throw new Error('执行结果格式异常，请重试。')
      send({
        type: 'result',
        id: request.id,
        result: JSON.parse(json) as import('@/types').GradeResult,
      })
    } finally {
      pyodide.globals.delete('_request_json')
    }
  } catch (error) {
    engine = undefined
    send({
      type: 'error',
      id: request.id,
      message:
        error instanceof Error
          ? error.message
          : 'Python 执行环境发生错误，请重试。',
    })
  }
}
