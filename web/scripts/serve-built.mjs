import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'
import { resolve, extname } from 'node:path'
import { fileURLToPath } from 'node:url'
const root = fileURLToPath(new URL('../dist/', import.meta.url))
const prefix = '/Python-100-Exercises/'
const types = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.mjs': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.wasm': 'application/wasm',
}
createServer(async (request, response) => {
  const pathname = new URL(request.url, 'http://localhost').pathname
  if (!pathname.startsWith(prefix)) {
    response.writeHead(404).end()
    return
  }
  const filename = resolve(
    root,
    decodeURIComponent(pathname.slice(prefix.length)) || 'index.html',
  )
  if (!filename.startsWith(root)) {
    response.writeHead(403).end()
    return
  }
  try {
    const body = await readFile(filename)
    response
      .writeHead(200, {
        'Content-Type': types[extname(filename)] ?? 'application/octet-stream',
      })
      .end(body)
  } catch {
    response.writeHead(404).end()
  }
}).listen(4173, '127.0.0.1')
