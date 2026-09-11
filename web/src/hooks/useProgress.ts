import { useEffect, useRef, useState } from 'react'
import type { Course } from '@/types'
import {
  emptyProgress,
  parseProgress,
  storageKey,
  type ProgressData,
} from '@/services/progress'

export function useProgress(course: Course) {
  const [initial] = useState(() => {
    try {
      const saved = localStorage.getItem(storageKey(course))
      return {
        data: saved ? parseProgress(saved, course) : emptyProgress(course),
        error: '',
      }
    } catch {
      return {
        data: emptyProgress(course),
        error:
          '无法读取本机学习记录。为避免覆盖原记录，自动保存已暂停；你仍可做题并导出当前代码。',
      }
    }
  })
  const [progress, setProgress] = useState(initial.data)
  const [error, setError] = useState(initial.error)
  const [saved, setSaved] = useState(true)
  const latest = useRef(progress)
  const blocked = useRef(!!initial.error)
  const change = (
    update: ProgressData | ((previous: ProgressData) => ProgressData),
  ) => {
    setSaved(false)
    setProgress(update)
  }
  useEffect(() => {
    latest.current = progress
    const save = () => {
      if (blocked.current) return
      try {
        localStorage.setItem(storageKey(course), JSON.stringify(latest.current))
        setSaved(true)
        setError('')
      } catch {
        setError(
          '浏览器存储不可用或空间不足，代码暂未保存。请导出学习记录备份。',
        )
      }
    }
    const timer = setTimeout(save, 300)
    window.addEventListener('beforeunload', save)
    return () => {
      clearTimeout(timer)
      window.removeEventListener('beforeunload', save)
    }
  }, [progress, course])
  const replace = (data: ProgressData) => {
    // 只有用户确认导入后才替换记录，不用空状态覆盖损坏的备份。
    blocked.current = false
    change(data)
  }
  return { progress, change, replace, error, saved }
}
