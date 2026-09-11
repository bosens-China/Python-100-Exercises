export type Files = Record<string, string>
export interface Exercise {
  id: string
  title: string
  category: string
  goal: string
  prerequisites: string[]
  path: string
  starter_files: string[]
  entrypoint: string
  question: string
  files: Files
  tests: string
}
export interface Category {
  id: string
  title: string
  goal: string
  exercises: string[]
}
export interface Course {
  schema_version: number
  id: string
  title: string
  categories: Category[]
  exercises: Exercise[]
}
export interface TestCase {
  name: string
  status: 'passed' | 'failed' | 'content_error'
  message: string
  traceback: string
  stdout: string
  stderr: string
}
export interface GradeResult {
  passed: boolean
  total: number
  passed_count: number
  cases: TestCase[]
  content_error?: string
}
export type RunMode = 'example' | 'submit'
export type RuntimeStatus = 'idle' | 'loading' | 'ready' | 'running' | 'error'
export interface RunRequest {
  id: number
  mode: RunMode
  files: Files
  tests: string
  entrypoint: string
  runtimeURL: string
}
export type WorkerResponse =
  | { type: 'status'; id: number; status: 'loading' | 'running' }
  | { type: 'result'; id: number; result: GradeResult }
  | { type: 'error'; id: number; message: string }
