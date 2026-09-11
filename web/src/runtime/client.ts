import type {
  Exercise,
  Files,
  GradeResult,
  RunMode,
  RuntimeStatus,
  WorkerResponse,
} from '@/types'

export class PythonRunner {
  private worker?: Worker
  private sequence = 0
  private timer?: ReturnType<typeof setTimeout>
  private pending?: { reject: (error: Error) => void }
  private readonly status: (state: RuntimeStatus) => void
  constructor(status: (state: RuntimeStatus) => void) {
    this.status = status
  }

  run(exercise: Exercise, files: Files, mode: RunMode): Promise<GradeResult> {
    if (this.pending)
      return Promise.reject(new Error('已有代码正在运行，请等待或停止。'))
    const id = ++this.sequence
    const fresh = !this.worker
    this.worker ??= new Worker(new URL('./python.worker.ts', import.meta.url), {
      type: 'module',
    })
    this.status(fresh ? 'loading' : 'running')
    return new Promise((resolve, reject) => {
      this.pending = { reject }
      const timeout = (milliseconds: number, message: string) => {
        clearTimeout(this.timer)
        this.timer = setTimeout(() => this.cancel(message), milliseconds)
      }
      timeout(
        fresh ? 90000 : 10000,
        fresh
          ? 'Python 环境加载超时，请重试。'
          : '运行超过 10 秒，已停止。请检查是否有死循环。',
      )
      this.worker!.onmessage = (event: MessageEvent<WorkerResponse>) => {
        const message = event.data
        if (message.id !== id || !this.pending) return
        if (message.type === 'status') {
          this.status(message.status)
          if (message.status === 'running')
            timeout(10000, '运行超过 10 秒，已停止。请检查是否有死循环。')
          return
        }
        clearTimeout(this.timer)
        this.pending = undefined
        if (message.type === 'result') {
          this.status('ready')
          resolve(message.result)
        } else {
          this.worker?.terminate()
          this.worker = undefined
          this.status('error')
          reject(new Error(`执行环境异常：${message.message.slice(0, 600)}`))
        }
      }
      this.worker!.onerror = () =>
        this.cancel('执行环境加载失败，请检查网络后重试。')
      this.worker!.postMessage({
        id,
        mode,
        files,
        tests: exercise.tests,
        entrypoint: exercise.entrypoint,
        runtimeURL: new URL(
          'runtime/',
          new URL(import.meta.env.BASE_URL, window.location.href),
        ).href,
      })
    })
  }

  cancel(message = '已停止运行，代码已保留。') {
    clearTimeout(this.timer)
    this.worker?.terminate()
    this.worker = undefined
    const pending = this.pending
    this.pending = undefined
    this.status('idle')
    pending?.reject(new Error(message))
  }
}
