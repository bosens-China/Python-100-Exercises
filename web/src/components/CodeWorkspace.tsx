import { useState } from 'react'
import CodeMirror from '@uiw/react-codemirror'
import { python } from '@codemirror/lang-python'
import { oneDark } from '@codemirror/theme-one-dark'
import { Button, Popconfirm, Tabs, Tooltip } from 'antd'
import {
  CodeOutlined,
  FileTextOutlined,
  ReloadOutlined,
  PlayCircleOutlined,
  SendOutlined,
  StopOutlined,
} from '@ant-design/icons'
import type { Exercise, Files, RuntimeStatus } from '@/types'
const extensions = [python()]

interface Props {
  exercise: Exercise
  files: Files
  dark: boolean
  saved: boolean
  status: RuntimeStatus
  onChange: (files: Files) => void
  onReset: () => void
  onRun: (mode: 'example' | 'submit') => void
  onStop: () => void
}
export function CodeWorkspace({
  exercise,
  files,
  dark,
  saved,
  status,
  onChange,
  onReset,
  onRun,
  onStop,
}: Props) {
  const [active, setActive] = useState(exercise.entrypoint)
  const busy = status === 'loading' || status === 'running'
  return (
    <section
      className="code-panel"
      aria-label="代码工作区"
      onKeyDownCapture={(event) => {
        if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
          event.preventDefault()
          if (!busy) onRun(event.shiftKey ? 'submit' : 'example')
        }
      }}
    >
      <div className="panel-label">
        <CodeOutlined aria-hidden="true" /> 代码工作区{' '}
        <span className="ml-auto muted">Python</span>
      </div>
      <div className="file-tabs">
        <Tabs
          activeKey={active}
          onChange={setActive}
          size="small"
          items={exercise.starter_files.map((name) => ({
            key: name,
            label: (
              <span>
                <FileTextOutlined aria-hidden="true" /> {name}
              </span>
            ),
          }))}
          tabBarExtraContent={
            <Popconfirm
              placement="bottomRight"
              title="重置当前题目？"
              description="本题所有文件和通过记录会被清除，恢复到起始代码。"
              onConfirm={onReset}
              okText="重置本题"
              cancelText="保留代码"
              disabled={busy}
            >
              <Button
                type="text"
                icon={<ReloadOutlined aria-hidden="true" />}
                aria-label="重置本题"
                title="恢复起始代码"
                disabled={busy}
              />
            </Popconfirm>
          }
        />
      </div>
      <div className="editor-container" data-testid="code-editor">
        <CodeMirror
          key={`${exercise.id}/${active}`}
          value={files[active]}
          height="100%"
          theme={dark ? oneDark : 'light'}
          extensions={extensions}
          onChange={(value) => onChange({ ...files, [active]: value })}
          basicSetup={{
            lineNumbers: true,
            foldGutter: true,
            highlightActiveLine: true,
            autocompletion: true,
            tabSize: 4,
          }}
          indentWithTab
          aria-label={`${active} 代码编辑器`}
        />
      </div>
      <div className="editor-status">
        <span>
          <span className={`save-dot ${saved ? '' : 'pending'}`} />
          {saved ? '已自动保存在此浏览器' : '保存中…'}
        </span>
        <span>
          UTF-8 <span className="ml-3">缩进 4 空格</span>
        </span>
      </div>
      <div className="editor-actions">
        <Tooltip title="Ctrl / ⌘ + Enter">
          <Button
            icon={<PlayCircleOutlined aria-hidden="true" />}
            onClick={() => onRun('example')}
            disabled={busy}
          >
            运行示例
          </Button>
        </Tooltip>
        {busy ? (
          <Button
            danger
            icon={<StopOutlined aria-hidden="true" />}
            onClick={onStop}
          >
            停止运行
          </Button>
        ) : (
          <Tooltip title="Ctrl / ⌘ + Shift + Enter">
            <Button
              type="primary"
              icon={<SendOutlined aria-hidden="true" />}
              onClick={() => onRun('submit')}
            >
              提交检查
            </Button>
          </Tooltip>
        )}
        <span className="muted action-hint">运行示例不记录通关</span>
      </div>
    </section>
  )
}
