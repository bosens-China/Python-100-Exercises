import { defineConfig } from '@playwright/test'
export default defineConfig({
  testDir: './test',
  timeout: 120_000,
  workers: 1,
  use: {
    baseURL: 'http://127.0.0.1:5173',
    channel: process.env.PLAYWRIGHT_CHANNEL || undefined,
    viewport: { width: 1440, height: 1000 },
    trace: 'retain-on-failure',
    actionTimeout: 15000,
  },
  webServer: [
    {
      command: 'pnpm dev --host 127.0.0.1',
      url: 'http://127.0.0.1:5173',
      reuseExistingServer: !process.env.CI,
    },
    {
      command: 'node scripts/serve-built.mjs',
      url: 'http://127.0.0.1:4173/Python-100-Exercises/',
      reuseExistingServer: !process.env.CI,
    },
  ],
})
