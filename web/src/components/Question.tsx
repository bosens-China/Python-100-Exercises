import Markdown from 'react-markdown'
import rehypeRaw from 'rehype-raw'
import remarkGfm from 'remark-gfm'
import { Tag, Tooltip } from 'antd'
import { ArrowLeftOutlined, ReadOutlined } from '@ant-design/icons'
import type { Exercise } from '@/types'

export function Question({
  exercise,
  onSelect,
}: {
  exercise: Exercise
  onSelect: (id: string) => void
}) {
  const markdown = exercise.question
    .replace(/^# .+\n/, '')
    .replace(/## 学习目标[\s\S]*?(?=## 前置知识)/, '')
    .replace(/## 开始编写[\s\S]*?(?=## 分层提示)/, '')
  return (
    <section className="question-panel" aria-label="题目说明">
      <div className="panel-label">
        <ReadOutlined aria-hidden="true" /> 题目说明{' '}
        <Tag variant="filled">练习 {exercise.id}</Tag>
      </div>
      <div className="question-scroll" key={exercise.id}>
        <div className="question-intro">
          <span className="eyebrow">EXERCISE {exercise.id}</span>
          <h1>{exercise.title}</h1>
          <p>{exercise.goal}</p>
          <div className="flex items-center gap-2">
            <Tag color="green" variant="filled">
              {Number(exercise.id) > 92 ? '综合实战' : '基础练习'}
            </Tag>
            <Tag variant="filled">自动检查</Tag>
            {exercise.prerequisites.length > 0 && (
              <Tooltip title="查看前置练习">
                <button
                  className="text-link"
                  onClick={() => onSelect(exercise.prerequisites[0])}
                >
                  <ArrowLeftOutlined aria-hidden="true" /> 前置{' '}
                  {exercise.prerequisites[0]}
                </button>
              </Tooltip>
            )}
          </div>
        </div>
        <article className="markdown">
          <Markdown
            remarkPlugins={[remarkGfm]}
            rehypePlugins={[rehypeRaw]}
            components={{
              a: ({ children }) => <span>{children}</span>,
            }}
          >
            {markdown}
          </Markdown>
        </article>
        <div className="question-note">
          先尝试，再展开提示。每一次修改，都是一次进步。
        </div>
      </div>
    </section>
  )
}
