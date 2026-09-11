import { lazy, Suspense, useEffect, useState } from 'react'
import {
  App as AntApp,
  Button,
  ConfigProvider,
  Result,
  Spin,
  theme,
} from 'antd'
import zhCN from 'antd/locale/zh_CN'
import { useTheme } from '@/hooks/useTheme'
import { loadCourse } from '@/services/course'
import type { Course } from '@/types'
import './App.css'
import './components/workspace.css'
const PracticePage = lazy(() => import('@/pages/PracticePage'))

export default function App() {
  const { mode, setMode, dark } = useTheme()
  const [course, setCourse] = useState<Course>()
  const [error, setError] = useState('')
  const [attempt, setAttempt] = useState(0)
  useEffect(() => {
    const controller = new AbortController()
    const timer = setTimeout(() => {
      controller.abort()
      setError('课程加载超时，请检查网络后重试。')
    }, 20000)
    loadCourse(controller.signal)
      .then(setCourse)
      .catch((caught: unknown) => {
        if (!controller.signal.aborted)
          setError(
            caught instanceof Error ? caught.message : '课程加载失败，请重试。',
          )
      })
      .finally(() => clearTimeout(timer))
    return () => {
      clearTimeout(timer)
      controller.abort()
    }
  }, [attempt])
  const loading = (
    <div className="page-loading">
      <Spin size="large" />
      <p>正在打开你的 Python 学习空间…</p>
    </div>
  )
  return (
    <ConfigProvider
      locale={zhCN}
      button={{ autoInsertSpace: false }}
      theme={{
        algorithm: dark ? theme.darkAlgorithm : theme.defaultAlgorithm,
        token: {
          colorPrimary: '#187f69',
          borderRadius: 7,
          fontFamily:
            "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif",
        },
      }}
    >
      <AntApp>
        {error ? (
          <Result
            status="warning"
            title="暂时无法打开课程"
            subTitle={error}
            extra={
              <Button
                type="primary"
                onClick={() => {
                  setError('')
                  setAttempt(attempt + 1)
                }}
              >
                重新加载
              </Button>
            }
          />
        ) : course ? (
          <Suspense fallback={loading}>
            <PracticePage
              course={course}
              mode={mode}
              onTheme={setMode}
              dark={dark}
            />
          </Suspense>
        ) : (
          loading
        )}
      </AntApp>
    </ConfigProvider>
  )
}
