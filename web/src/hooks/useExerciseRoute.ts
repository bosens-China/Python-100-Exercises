import { useEffect, useState } from 'react'
export const exerciseHash = (id: string) => `#/exercises/${id}`
export function useExerciseRoute() {
  const [id, setId] = useState(() =>
    window.location.hash.slice('#/exercises/'.length),
  )
  useEffect(() => {
    const update = () =>
      setId(
        window.location.hash.startsWith('#/exercises/')
          ? window.location.hash.slice('#/exercises/'.length)
          : '',
      )
    window.addEventListener('hashchange', update)
    return () => window.removeEventListener('hashchange', update)
  }, [])
  return {
    id,
    navigate: (next: string) => {
      window.location.hash = exerciseHash(next)
    },
  }
}
