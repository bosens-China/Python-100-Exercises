import { describe, expect, it } from 'vitest'
import {
  emptyProgress,
  isPassed,
  parseProgress,
  recordResult,
  updateFiles,
} from '../progress'
import type { Course, Exercise } from '../../types'
const exercise: Exercise = {
  id: '001',
  title: 'Hello',
  category: '01',
  goal: '',
  path: '',
  question: '',
  prerequisites: [],
  starter_files: ['main.py'],
  entrypoint: 'main.py',
  files: { 'main.py': '' },
  tests: '',
}
const course: Course = {
  id: 'v1',
  schema_version: 1,
  title: '',
  categories: [],
  exercises: [exercise],
}
const correct = { 'main.py': 'print("hello")' }

describe('学习记录', () => {
  it('修改已通过代码后不再显示当前通过，恢复原代码可识别', () => {
    let progress = updateFiles(emptyProgress(course), exercise, correct)
    progress = recordResult(progress, exercise, correct, true)
    expect(isPassed(progress.drafts['001'])).toBe(true)
    progress = updateFiles(progress, exercise, { 'main.py': 'wrong' })
    expect(isPassed(progress.drafts['001'])).toBe(false)
    progress = updateFiles(progress, exercise, correct)
    expect(isPassed(progress.drafts['001'])).toBe(true)
  })
  it('提交期间编辑，不会把新代码误记为已通过', () => {
    const progress = updateFiles(emptyProgress(course), exercise, {
      'main.py': 'new',
    })
    expect(
      isPassed(recordResult(progress, exercise, correct, true).drafts['001']),
    ).toBe(false)
  })
  it('同一版本再次失败应撤销通过状态', () => {
    const passed = recordResult(
      updateFiles(emptyProgress(course), exercise, correct),
      exercise,
      correct,
      true,
    )
    expect(
      isPassed(recordResult(passed, exercise, correct, false).drafts['001']),
    ).toBe(false)
  })
  it('导出记录可完整导回', () => {
    const data = updateFiles(emptyProgress(course), exercise, correct)
    expect(parseProgress(JSON.stringify(data), course)).toEqual(data)
  })
  it.each([
    '{',
    JSON.stringify({ schema: 1, courseId: 'old', drafts: {} }),
    JSON.stringify({ schema: 1, courseId: 'v1', drafts: { '002': {} } }),
    JSON.stringify({
      schema: 1,
      courseId: 'v1',
      drafts: {
        '001': {
          files: { 'other.py': 'bad' },
          passedSource: null,
          updatedAt: '',
        },
      },
    }),
  ])('拒绝不兼容或损坏的备份 %s', (text) => {
    expect(() => parseProgress(text, course)).toThrow()
  })
})
