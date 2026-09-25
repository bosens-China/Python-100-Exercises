# 做题网页

在仓库根目录保留 Python 题目和测试。网页在构建时直接读取这些文件。

```bash
cd web
npm ci
npm run dev
```

`npm run build` 生成 GitHub Pages 使用的 `dist/`。浏览器判题在 Web Worker 中运行 Pyodide；首次运行需下载 Python 运行环境。草稿与进度保存在浏览器 LocalStorage。
