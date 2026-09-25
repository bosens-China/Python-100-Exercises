export type TestResult = { name: string; passed: boolean; message?: string }
let worker: Worker | undefined

export function runBrowserTests(number: number, code: string, tests: string): Promise<TestResult[]> {
  worker ??= new Worker(new URL('./runner.worker.ts', import.meta.url), { type: 'module' })
  const current = worker
  return new Promise((resolve, reject) => {
    const timeout = window.setTimeout(() => {
      current.terminate()
      worker = undefined
      reject(new Error('运行超时，请检查代码是否进入死循环'))
    }, 90_000)
    function cleanup() {
      window.clearTimeout(timeout)
      current.removeEventListener('message', onMessage)
      current.removeEventListener('error', onError)
    }
    function onMessage(event: MessageEvent<{ results?: TestResult[]; error?: string }>) {
      cleanup()
      if (event.data.error) reject(new Error(event.data.error))
      else resolve(event.data.results ?? [])
    }
    function onError(event: ErrorEvent) {
      cleanup()
      current.terminate()
      worker = undefined
      reject(new Error(event.message || 'Python 运行环境加载失败'))
    }
    current.addEventListener('message', onMessage)
    current.addEventListener('error', onError)
    current.postMessage({ number, code, tests })
  })
}
