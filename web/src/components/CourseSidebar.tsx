import { useState } from 'react'
import { CheckOutlined, SearchOutlined, CodeOutlined } from '@ant-design/icons'
import { Collapse, Empty, Input, Progress, Tooltip } from 'antd'
import type { Course } from '@/types'
import { isPassed, type ProgressData } from '@/services/progress'

interface Props {
  course: Course
  selected: string
  progress: ProgressData
  onSelect: (id: string) => void
}
export function CourseSidebar({ course, selected, progress, onSelect }: Props) {
  const [search, setSearch] = useState('')
  const category = course.exercises.find(
    (item) => item.id === selected,
  )?.category
  const [opened, setOpened] = useState<string[]>(
    category ? [category] : [course.categories[0].id],
  )
  const completed = Object.values(progress.drafts).filter(isPassed).length
  const term = search.trim().toLowerCase()
  const groups = course.categories
    .map((group) => ({
      group,
      exercises: course.exercises.filter(
        (item) =>
          item.category === group.id &&
          `${item.id} ${item.title} ${group.title}`
            .toLowerCase()
            .includes(term),
      ),
    }))
    .filter((group) => group.exercises.length)
  return (
    <aside className="course-sidebar" aria-label="课程目录">
      <div className="sidebar-heading">
        <div className="eyebrow">LEARNING PATH</div>
        <div className="flex items-center justify-between mt-2">
          <h2>课程目录</h2>
          <span className="muted">10 个章节</span>
        </div>
        <div className="learning-progress">
          <span>你的学习进度</span>
          <strong>
            {completed}
            <small> / 100</small>
          </strong>
        </div>
        <Progress
          percent={completed}
          showInfo={false}
          strokeColor="var(--accent)"
          size="small"
        />
        <Input
          aria-label="搜索题目"
          placeholder="搜索题目或知识点"
          prefix={<SearchOutlined aria-hidden="true" />}
          allowClear
          value={search}
          onChange={(event) => setSearch(event.target.value)}
        />
      </div>
      <nav className="chapter-scroll">
        {groups.length ? (
          <Collapse
            ghost
            activeKey={
              term
                ? groups.map((item) => item.group.id)
                : [...new Set([...opened, category ?? ''])]
            }
            onChange={(keys) =>
              setOpened(typeof keys === 'string' ? [keys] : keys)
            }
            expandIconPlacement="end"
            items={groups.map(({ group, exercises }) => ({
              key: group.id,
              label: (
                <div className="chapter-title">
                  <span className="chapter-number">{group.id.slice(0, 2)}</span>
                  <span>{group.title}</span>
                </div>
              ),
              children: (
                <div className="exercise-list">
                  {exercises.map((item) => {
                    const draft = progress.drafts[item.id]
                    return (
                      <button
                        key={item.id}
                        className={`exercise-link ${selected === item.id ? 'selected' : ''}`}
                        aria-current={selected === item.id ? 'page' : undefined}
                        onClick={() => onSelect(item.id)}
                      >
                        <span className="exercise-number">{item.id}</span>
                        <span className="exercise-name">{item.title}</span>
                        {isPassed(draft) ? (
                          <Tooltip title="当前代码已通过">
                            <CheckOutlined
                              aria-hidden="true"
                              className="passed-icon"
                            />
                          </Tooltip>
                        ) : draft ? (
                          <span className="draft-dot" title="待检查" />
                        ) : null}
                      </button>
                    )
                  })}
                </div>
              ),
            }))}
          />
        ) : (
          <Empty
            image={Empty.PRESENTED_IMAGE_SIMPLE}
            description="没有找到相关题目"
          />
        )}
      </nav>
      <div className="sidebar-foot">
        <CodeOutlined aria-hidden="true" />
        <div>
          <strong>从第一行代码开始</strong>
          <span>循序渐进，把知识变成能力。</span>
        </div>
      </div>
    </aside>
  )
}
