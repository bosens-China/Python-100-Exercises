---
name: apply-yliu-product-development-practices
description: "Apply Yliu's product development practices when creating or changing applications across product clarification, project setup, architecture, frontend, backend, data, UI, testing, deployment, and validation. Use for new projects and incremental work in existing projects."
---

# Apply Yliu Product Development Practices

使用 Yliu 的方法完成产品开发。它覆盖开发前确认、项目初始化、技术选型、前后端实现、页面交互、测试和交付前验证。

这套方法提供默认选择，但不会覆盖用户要求，也不会强迫旧项目全面迁移。

## 决策顺序

遇到不同做法时，按以下顺序决定：

1. 先按用户本次的明确要求执行。
2. 用户没有指定时，沿用项目已经稳定使用的方案。
3. 前两项都没有答案时，再采用本技能的默认做法。

新项目可以直接采用本技能。旧项目默认采用渐进方式：新代码使用新做法；本次需要修改的旧代码可以顺手调整；其他旧代码保持不动。只有用户明确提出全面重构时，才进行统一迁移。

只有用户明确说明项目目前处于开发阶段，或明确要求由我们负责从零实现某个功能时，才将对应项目或功能视为开发阶段。不要根据版本号、代码成熟度或正在进行开发自行推测。用户明确指定的范围内，可以不保留对旧实现的兼容，按最佳实践直接调整或重构，不必局限于渐进适配；仍需遵守用户的其他明确约束，不把单个功能的授权扩展到无关功能或整个仓库。

## 工作流程

1. 先查看任务、现有代码、依赖、脚本和配置，理解目标、约束和项目当前的做法，明确完成后应出现的可验证结果。
2. 能从项目中确认的信息直接确认，不要重复询问。会影响范围、行为或实现方向的关键歧义先澄清；低风险细节自行判断，明确说明影响结果的必要假设和取舍。
3. 根据任务范围，读取下方对应的规范。复杂任务给出简要步骤和对应的验证方式；简单任务直接执行。
4. 写代码前先看项目里能否复用，再评估成熟的社区方案。采用满足当前需求的最简单实现；发现更简单的可行方案时主动提出，必要时说明原方案的问题。
5. 默认沿用项目风格，只完成当前任务需要的改动；明确授权的重构按授权范围执行。
6. 根据改动范围和风险验证结果。验证失败时继续定位和修正；遇到无法解决的阻碍时说明原因。完成时说明验证结果和尚未验证的部分。

## 按需读取规范

- 涉及目标用户、设备与主题范围、跨平台差异、项目初始化、端口、包管理、Monorepo、Git hook、`.gitattributes`、技术选型、别名或社区方案时，读取 [project-and-architecture.md](references/project-and-architecture.md)。
- 涉及 TypeScript、修改范围、代码清理、注释、Hook、Composable、组件抽象或代码复用时，读取 [implementation-practices.md](references/implementation-practices.md)。
- 涉及接口、请求、路由、页面数据、Loading、错误反馈、危险操作或样式时，读取 [requests-routing-and-ui.md](references/requests-routing-and-ui.md)。
- 涉及数据库、ORM、数据验证、统一响应、Swagger、时间、环境变量、后端日志或生产编排时，读取 [backend-data-and-runtime.md](references/backend-data-and-runtime.md)。
- 涉及测试、类型检查、Lint、格式化、构建或完成后的验证时，读取 [testing-and-validation.md](references/testing-and-validation.md)。

一个任务涉及多个方面时，读取所有相关规范。普通任务不需要为了了解全貌而加载全部文件。

## 核心原则

- 新项目直接采用新做法，旧项目默认只在修改时逐步适配；开发阶段的兼容例外按上方决策顺序执行。
- 先复用项目已有能力，再评估成熟社区方案。两者都不合适时，才自行实现。
- 同构项目优先复用语言、类型和验证规则，减少重复维护。
- 页面只管理自己的请求。跨页面的核心状态优先放入 URL。
- 请求失败必须进入错误流程。Loading 尽量只影响对应区域。
- 不增加未要求的功能、配置或扩展能力。抽象和依赖必须带来实际收益，不为假想需求设计。
- 只测试重要且稳定的行为。检查力度与改动风险保持一致。
