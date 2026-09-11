import { Alert, Button, Collapse, Empty, Spin, Tag } from 'antd'
import {
  CheckCircleFilled,
  CloseCircleFilled,
  LoadingOutlined,
  CodeOutlined,
  ArrowRightOutlined,
} from '@ant-design/icons'
import type { GradeResult, RunMode, RuntimeStatus } from '@/types'

interface Props {
  result?: GradeResult
  mode?: RunMode
  status: RuntimeStatus
  error: string
  stale: boolean
  onRetry: () => void
  onNext?: () => void
}
export function Results({
  result,
  mode,
  status,
  error,
  stale,
  onRetry,
  onNext,
}: Props) {
  const busy = status === 'running' || status === 'loading'
  return (
    <section
      className="results-panel"
      aria-label="运行与检查结果"
      aria-live="polite"
    >
      <div className="panel-label">
        <CodeOutlined aria-hidden="true" /> 运行与检查{' '}
        <span className="ml-auto">
          {status === 'ready' && (
            <span className="runtime-ready">● Python 已就绪</span>
          )}
        </span>
      </div>
      <div className="results-scroll">
        {busy ? (
          <div className="runtime-loading">
            <Spin indicator={<LoadingOutlined aria-hidden="true" spin />} />
            <div>
              <strong>
                {status === 'loading'
                  ? '正在准备 Python 环境'
                  : '正在运行你的代码'}
              </strong>
              <p>
                {status === 'loading'
                  ? '首次加载需要一点时间，你可以继续阅读和编辑。'
                  : '正在独立工作区中检查，不会影响你的代码。'}
              </p>
            </div>
          </div>
        ) : error ? (
          <Alert
            type="warning"
            showIcon
            title={error}
            action={
              <Button size="small" onClick={onRetry}>
                重试
              </Button>
            }
          />
        ) : !result ? (
          <div className="result-empty">
            <Empty
              image={Empty.PRESENTED_IMAGE_SIMPLE}
              description={
                <>
                  <strong>写下第一行，然后试一试</strong>
                  <p>运行示例了解输出，提交检查验证全部要求。</p>
                </>
              }
            />
          </div>
        ) : (
          <>
            {stale && (
              <Alert
                className="mb-3"
                type="info"
                showIcon
                title="代码已修改，以下是上一次运行结果。请重新检查当前代码。"
              />
            )}
            <div
              className={`result-summary ${result.passed ? 'success' : 'failure'}`}
            >
              {result.passed ? (
                <CheckCircleFilled aria-hidden="true" />
              ) : (
                <CloseCircleFilled aria-hidden="true" />
              )}
              <div>
                <strong>
                  {result.passed
                    ? mode === 'submit'
                      ? '全部通过，继续前进！'
                      : '示例检查通过'
                    : '还差一点，看看下面的反馈'}
                </strong>
                <span>
                  {mode === 'example' ? '示例检查' : '全部检查'} ·{' '}
                  {result.passed_count} / {result.total} 项通过
                </span>
              </div>
              {result.passed && mode === 'submit' && !stale && onNext && (
                <Button size="small" type="primary" onClick={onNext}>
                  下一题 <ArrowRightOutlined aria-hidden="true" />
                </Button>
              )}
            </div>
            {result.content_error && (
              <Alert
                type="error"
                title="题目测试内容有误"
                description={result.content_error}
              />
            )}
            <Collapse
              ghost
              size="small"
              defaultActiveKey={result.cases
                .filter((item) => item.status !== 'passed')
                .map((item) => item.name)}
              items={result.cases.map((item, index) => ({
                key: item.name,
                label: (
                  <div className="case-label">
                    {item.status === 'passed' ? (
                      <CheckCircleFilled
                        aria-hidden="true"
                        className="passed-icon"
                      />
                    ) : (
                      <CloseCircleFilled
                        aria-hidden="true"
                        className="failed-icon"
                      />
                    )}
                    <span>检查 {index + 1}</span>
                    <Tag
                      variant="filled"
                      color={item.status === 'passed' ? 'success' : 'error'}
                    >
                      {item.status === 'passed' ? '通过' : '未通过'}
                    </Tag>
                  </div>
                ),
                children: (
                  <div className="case-detail">
                    {item.message && <pre>{item.message}</pre>}
                    {item.stdout && (
                      <>
                        <span className="muted">标准输出</span>
                        <pre>{item.stdout}</pre>
                      </>
                    )}
                    {item.stderr && <pre>{item.stderr}</pre>}
                    {item.traceback && (
                      <details>
                        <summary>查看错误位置</summary>
                        <pre>{item.traceback}</pre>
                      </details>
                    )}
                    {!item.message && !item.stdout && !item.stderr && (
                      <span className="muted">结果符合本项要求。</span>
                    )}
                  </div>
                ),
              }))}
            />
          </>
        )}
      </div>
    </section>
  )
}
