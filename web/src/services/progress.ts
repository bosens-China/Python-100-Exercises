import type { Course, Exercise, Files } from '@/types'

export interface Draft {
  files: Files
  passedSource: string | null
  updatedAt: string
}
export interface ProgressData {
  schema: 1
  courseId: string
  drafts: Record<string, Draft>
}
export const storageKey = (course: Course) => `python100.progress.${course.id}`
export const emptyProgress = (course: Course): ProgressData => ({
  schema: 1,
  courseId: course.id,
  drafts: {},
})
export const signature = (files: Files) =>
  JSON.stringify(
    Object.keys(files)
      .sort()
      .map((name) => [name, files[name]]),
  )
export const isPassed = (draft?: Draft) =>
  !!draft?.passedSource && draft.passedSource === signature(draft.files)
export const filesFor = (exercise: Exercise, progress: ProgressData) =>
  progress.drafts[exercise.id]?.files ?? exercise.files

function record(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

export function parseProgress(text: string, course: Course): ProgressData {
  if (text.length > 2_000_000)
    throw new Error('学习记录文件过大，最大支持 2 MB。')
  const data: unknown = JSON.parse(text)
  if (
    !record(data) ||
    data.schema !== 1 ||
    data.courseId !== course.id ||
    !record(data.drafts)
  ) {
    throw new Error('这不是当前课程版本的有效学习记录。')
  }
  const drafts: Record<string, Draft> = {}
  for (const [id, value] of Object.entries(data.drafts)) {
    const exercise = course.exercises.find((item) => item.id === id)
    if (
      !exercise ||
      !record(value) ||
      !record(value.files) ||
      typeof value.updatedAt !== 'string' ||
      (value.passedSource !== null && typeof value.passedSource !== 'string')
    ) {
      throw new Error(`题目 ${id} 的学习记录不完整。`)
    }
    const files: Files = {}
    if (Object.keys(value.files).length !== exercise.starter_files.length)
      throw new Error(`题目 ${id} 的文件不匹配。`)
    for (const name of exercise.starter_files) {
      const source = value.files[name]
      if (typeof source !== 'string' || source.length > 200_000)
        throw new Error(`题目 ${id} 的代码文件无效。`)
      files[name] = source
    }
    drafts[id] = {
      files,
      updatedAt: value.updatedAt,
      passedSource: value.passedSource as string | null,
    }
  }
  return { schema: 1, courseId: course.id, drafts }
}

export function updateFiles(
  progress: ProgressData,
  exercise: Exercise,
  files: Files,
): ProgressData {
  const previous = progress.drafts[exercise.id]
  return {
    ...progress,
    drafts: {
      ...progress.drafts,
      [exercise.id]: {
        files: { ...files },
        passedSource: previous?.passedSource ?? null,
        updatedAt: new Date().toISOString(),
      },
    },
  }
}

export function recordResult(
  progress: ProgressData,
  exercise: Exercise,
  submitted: Files,
  passed: boolean,
): ProgressData {
  const draft = progress.drafts[exercise.id] ?? {
    files: { ...exercise.files },
    passedSource: null,
    updatedAt: new Date().toISOString(),
  }
  const submittedSource = signature(submitted)
  return {
    ...progress,
    drafts: {
      ...progress.drafts,
      [exercise.id]: {
        ...draft,
        passedSource: passed
          ? submittedSource
          : draft.passedSource === submittedSource
            ? null
            : draft.passedSource,
      },
    },
  }
}
