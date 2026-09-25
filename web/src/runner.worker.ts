import script from './run_tests.py?raw'

type Request = { number: number; code: string; tests: string }
const runtimeUrl = 'https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide.mjs'
let runtime: Promise<{ globals: { set: (name: string, value: unknown) => void }; runPythonAsync: (code: string) => Promise<string> }> | undefined

function getRuntime() {
  runtime ??= import(/* @vite-ignore */ runtimeUrl).then((module) => module.loadPyodide())
  return runtime
}

self.addEventListener('message', async (event: MessageEvent<Request>) => {
  try {
    const pyodide = await getRuntime()
    pyodide.globals.set('exercise_number', event.data.number)
    pyodide.globals.set('exercise_source', event.data.code)
    pyodide.globals.set('test_source', event.data.tests)
    const result = await pyodide.runPythonAsync(`${script}\nrun_tests(exercise_number, exercise_source, test_source)`)
    self.postMessage({ results: JSON.parse(result) })
  } catch (error) {
    self.postMessage({ error: error instanceof Error ? error.message : String(error) })
  }
})
