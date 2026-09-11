import { useRef } from 'react'
import { App, Button, Dropdown, Tooltip } from 'antd'
import {
  CodeOutlined,
  DownloadOutlined,
  ImportOutlined,
  SettingOutlined,
} from '@ant-design/icons'
import type { Course } from '@/types'
import type { ThemeMode } from '@/hooks/useTheme'
import { parseProgress, type ProgressData } from '@/services/progress'

interface Props {
  course: Course
  progress: ProgressData
  onImport: (data: ProgressData) => void
  mode: ThemeMode
  onTheme: (mode: ThemeMode) => void
}
export function Header({ course, progress, onImport, mode, onTheme }: Props) {
  const input = useRef<HTMLInputElement>(null)
  const { modal, message } = App.useApp()
  const exportProgress = () => {
    const url = URL.createObjectURL(
      new Blob([JSON.stringify(progress, null, 2)], {
        type: 'application/json',
      }),
    )
    const anchor = document.createElement('a')
    anchor.href = url
    anchor.download = `python100-progress-${new Date().toISOString().slice(0, 10)}.json`
    anchor.click()
    setTimeout(() => URL.revokeObjectURL(url), 1000)
  }
  const importProgress = async (file?: File) => {
    if (!file) return
    try {
      if (file.size > 2_000_000)
        throw new Error('学习记录文件过大，最大支持 2 MB。')
      const imported = parseProgress(await file.text(), course)
      modal.confirm({
        title: '导入学习记录？',
        content: `这份备份包含 ${Object.keys(imported.drafts).length} 道题的记录，将替换此浏览器中的全部课程记录。建议先导出当前记录。`,
        okText: '替换并导入',
        cancelText: '取消',
        onOk: () => {
          onImport(imported)
          message.success('学习记录已导入')
        },
      })
    } catch (error) {
      message.error(
        error instanceof Error ? error.message : '导入失败，原记录已保留。',
      )
    }
  }
  return (
    <header className="app-header">
      <a className="brand" href="#/exercises/001">
        <span className="brand-mark">
          <CodeOutlined aria-hidden="true" />
        </span>
        <span>
          Python<span className="brand-100">100</span>
        </span>
      </a>
      <span className="header-divider" />
      <span className="header-caption">从零开始，写出你的可能</span>
      <div className="header-tools">
        <Tooltip title="进度仅保存在当前浏览器，清理浏览器数据前请导出备份。">
          <span className="local-badge">
            <span className="save-dot" /> 本机学习记录
          </span>
        </Tooltip>
        <Button
          type="text"
          icon={<DownloadOutlined aria-hidden="true" />}
          onClick={exportProgress}
        >
          导出记录
        </Button>
        <Button
          type="text"
          icon={<ImportOutlined aria-hidden="true" />}
          onClick={() => input.current?.click()}
        >
          导入
        </Button>
        <input
          ref={input}
          type="file"
          accept=".json,application/json"
          hidden
          aria-label="导入学习记录文件"
          onChange={(event) => {
            void importProgress(event.target.files?.[0])
            event.target.value = ''
          }}
        />
        <Dropdown
          trigger={['click']}
          menu={{
            selectedKeys: [mode],
            items: [
              { key: 'system', label: '主题 · 跟随系统' },
              { key: 'light', label: '主题 · 浅色' },
              { key: 'dark', label: '主题 · 深色' },
            ],
            onClick: ({ key }) => onTheme(key as ThemeMode),
          }}
        >
          <Button
            type="text"
            icon={<SettingOutlined aria-hidden="true" />}
            aria-label="主题设置"
          />
        </Dropdown>
      </div>
    </header>
  )
}
