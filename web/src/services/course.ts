import type { Course, Exercise, Category } from '@/types'
const object = (value: unknown): value is Record<string, unknown> =>
  !!value && typeof value === 'object' && !Array.isArray(value)
const strings = (value: unknown): value is string[] =>
  Array.isArray(value) && value.every((item) => typeof item === 'string')

export const loadCourse = async (signal?: AbortSignal): Promise<Course> => {
  const response = await fetch(`${import.meta.env.BASE_URL}course.json`, {
    signal,
  })
  if (!response.ok) throw new Error('题目加载失败，请检查网络后重试。')
  const data: unknown = await response.json()
  if (
    !object(data) ||
    typeof data.id !== 'string' ||
    typeof data.title !== 'string' ||
    data.schema_version !== 1 ||
    !Array.isArray(data.categories) ||
    !Array.isArray(data.exercises)
  )
    throw new Error('课程数据版本不受支持。')
  const categories: Category[] = data.categories.map((item) => {
    if (
      !object(item) ||
      typeof item.id !== 'string' ||
      typeof item.title !== 'string' ||
      typeof item.goal !== 'string' ||
      !strings(item.exercises)
    )
      throw new Error('课程分类数据不完整。')
    return {
      id: item.id,
      title: item.title,
      goal: item.goal,
      exercises: item.exercises,
    }
  })
  const exercises: Exercise[] = data.exercises.map((item) => {
    if (
      !object(item) ||
      typeof item.id !== 'string' ||
      typeof item.title !== 'string' ||
      typeof item.category !== 'string' ||
      typeof item.goal !== 'string' ||
      typeof item.path !== 'string' ||
      typeof item.entrypoint !== 'string' ||
      typeof item.question !== 'string' ||
      typeof item.tests !== 'string' ||
      !strings(item.prerequisites) ||
      !strings(item.starter_files) ||
      !object(item.files)
    )
      throw new Error('题目内容不完整。')
    const files: Record<string, string> = {}
    for (const name of item.starter_files) {
      if (typeof item.files[name] !== 'string')
        throw new Error('题目代码文件不完整。')
      files[name] = item.files[name]
    }
    return {
      id: item.id,
      title: item.title,
      category: item.category,
      goal: item.goal,
      path: item.path,
      entrypoint: item.entrypoint,
      question: item.question,
      tests: item.tests,
      prerequisites: item.prerequisites,
      starter_files: item.starter_files,
      files,
    }
  })
  return {
    id: data.id,
    title: data.title,
    schema_version: 1,
    categories,
    exercises,
  }
}
