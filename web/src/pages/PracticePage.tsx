import { useEffect, useState } from 'react'
import { Alert, Button, Result, Splitter } from 'antd'
import type {
  Course,
  Exercise,
  Files,
  GradeResult,
  RunMode,
  RuntimeStatus,
} from '@/types'
import type { ThemeMode } from '@/hooks/useTheme'
import { useProgress } from '@/hooks/useProgress'
import { useExerciseRoute } from '@/hooks/useExerciseRoute'
import {
  filesFor,
  recordResult,
  signature,
  updateFiles,
} from '@/services/progress'
import { PythonRunner } from '@/runtime/client'
import { CourseSidebar } from '@/components/CourseSidebar'
import { Question } from '@/components/Question'
import { CodeWorkspace } from '@/components/CodeWorkspace'
import { Results } from '@/components/Results'
import { Header } from '@/components/Header'

type ProgressState = ReturnType<typeof useProgress>
interface Props {
  course: Course
  dark: boolean
  mode: ThemeMode
  onTheme: (mode: ThemeMode) => void
}
export default function PracticePage({ course, dark, mode, onTheme }: Props) {
  const progress = useProgress(course)
  const [revision, setRevision] = useState(0)
  const { id, navigate } = useExerciseRoute()
  const exercise = course.exercises.find(
    (item) => item.id === (id || course.exercises[0].id),
  )
  return (
    <div className="application">
      <Header
        course={course}
        progress={progress.progress}
        onImport={(data) => {
          progress.replace(data)
          setRevision((value) => value + 1)
        }}
        mode={mode}
        onTheme={onTheme}
      />
      {progress.error && (
        <Alert type="warning" showIcon title={progress.error} />
      )}
      <main className="practice-layout">
        <CourseSidebar
          course={course}
          selected={exercise?.id ?? ''}
          progress={progress.progress}
          onSelect={navigate}
        />
        {exercise ? (
          <ExerciseView
            key={`${exercise.id}/${revision}`}
            exercise={exercise}
            course={course}
            progress={progress}
            dark={dark}
            onSelect={navigate}
          />
        ) : (
          <div className="not-found">
            <Result
              status="404"
              title="没有这道题"
              subTitle="题号可能有误，请从课程目录选择一道练习。"
              extra={
                <Button onClick={() => navigate(course.exercises[0].id)}>
                  回到第一题
                </Button>
              }
            />
          </div>
        )}
      </main>
    </div>
  )
}

function ExerciseView({
  exercise,
  course,
  progress,
  dark,
  onSelect,
}: {
  exercise: Exercise
  course: Course
  progress: ProgressState
  dark: boolean
  onSelect: (id: string) => void
}) {
  const [status, setStatus] = useState<RuntimeStatus>('idle')
  const [runner] = useState(() => new PythonRunner(setStatus))
  const [execution, setExecution] = useState<{
    result: GradeResult
    mode: RunMode
    source: string
  }>()
  const [error, setError] = useState('')
  const [lastMode, setLastMode] = useState<RunMode>('submit')
  const files = filesFor(exercise, progress.progress)
  const next =
    course.exercises[
      course.exercises.findIndex((item) => item.id === exercise.id) + 1
    ]
  useEffect(() => () => runner.cancel(), [runner])
  const run = async (mode: RunMode) => {
    setError('')
    setLastMode(mode)
    const submitted = { ...files }
    try {
      const result = await runner.run(exercise, submitted, mode)
      setExecution({ result, mode, source: signature(submitted) })
      if (mode === 'submit')
        progress.change((previous) =>
          recordResult(previous, exercise, submitted, result.passed),
        )
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : '运行失败，请重试。')
    }
  }
  const change = (nextFiles: Files) =>
    progress.change((previous) => updateFiles(previous, exercise, nextFiles))
  const reset = () => {
    progress.change((previous) => {
      const drafts = { ...previous.drafts }
      delete drafts[exercise.id]
      return { ...previous, drafts }
    })
    setExecution(undefined)
    setError('')
  }
  return (
    <div className="workspace">
      <Splitter>
        <Splitter.Panel defaultSize="44%" min={330}>
          <Question exercise={exercise} onSelect={onSelect} />
        </Splitter.Panel>
        <Splitter.Panel min={420}>
          <Splitter orientation="vertical">
            <Splitter.Panel defaultSize="65%" min={280}>
              <CodeWorkspace
                exercise={exercise}
                files={files}
                dark={dark}
                saved={progress.saved && !progress.error}
                status={status}
                onChange={change}
                onReset={reset}
                onRun={run}
                onStop={() => runner.cancel()}
              />
            </Splitter.Panel>
            <Splitter.Panel min={160}>
              <Results
                key={`${execution?.source ?? ''}/${execution?.mode ?? ''}`}
                result={execution?.result}
                mode={execution?.mode}
                status={status}
                error={error}
                stale={!!execution && execution.source !== signature(files)}
                onRetry={() => run(lastMode)}
                onNext={next ? () => onSelect(next.id) : undefined}
              />
            </Splitter.Panel>
          </Splitter>
        </Splitter.Panel>
      </Splitter>
    </div>
  )
}
