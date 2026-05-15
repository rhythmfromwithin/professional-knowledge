# Anthropic Engineering Blog — 主题阅读地图

> 24 篇文章按 7 个主题模块组织。每模块 30 分钟可消化。
> 建议顺序：从你当前最痛的模块开始，不必按序。

---

## 怎么用这份地图

你同时跑着多个 AI 项目，没时间从头到尾读 24 篇长文。这份地图帮你做三件事：按当前痛点定位模块、用 30 分钟摘要快速吸收核心知识、用"能解决的问题"验证是否读到位。每个模块设计为一个午休时段可消化的量。如果某个模块的"适合你的时机"描述命中了你现在的处境，优先读它。

---

## 模块 1：Agent 架构入门
**适合你的时机：** 你正在决定新项目该用 workflow 还是 agent，或者团队在争论"要不要上 LangGraph"

### 必读（1 篇）
**23. 构建有效的 Agent** — 这是 Anthropic 的 Agent 设计总纲，把 workflow 和 agent 的边界画清楚了，所有后续文章都建立在这个分类体系上

### 选读（2 篇）
- 4. 长程应用开发的 Harness 设计 — 当任务超过单次对话能完成的规模时，generator/evaluator 分离架构怎么搭
- 10. 长时间运行智能体的有效"脚手架" — 跨 session 的状态持久化实操，双 agent 架构的具体实现

### 30 分钟摘要

读完这 3 篇你应该记住的 5 件事：

- **Workflow vs Agent 的决策线**：控制权归属是分类关键。Workflow 适合步骤确定、可预测的任务（客服分流、文档生成）；Agent 适合步骤数不确定的开放问题（自主调试、研究）。能用单次 LLM 调用解决就不要 workflow，能用 workflow 解决就不要 agent。
- **五种 Workflow 模式足够覆盖 80% 场景**：Prompt chaining（串行）、Routing（分类分发）、Parallelization（并行投票）、Orchestrator-workers（动态拆分）、Evaluator-optimizer（生成-评估循环）。先从这五种里选，选不出来再考虑自主 agent。
- **长任务的核心矛盾是 context degradation**：上下文越填越乱，模型越来越"笨"。解法是 generator/evaluator 分离——让独立的评判 agent 在干净上下文里打分，避免自我评估偏差。
- **跨 session 状态管理是一等公民**：每个 session 只做一个 feature 然后 git commit（原子事务）；用进度文件 + git history + JSON feature list 做"交接班"；强制流程是"读进度→读日志→挑任务→执行→提交"。
- **Harness 要持续做减法**：每个 harness 组件都内嵌一个"模型现在做不到 X"的假设。模型升级后第一件事是审计哪些假设过时、删掉对应代码，而不是加新组件。

### 学完能解决的 3 类问题
1. 老板说"我们要做一个 AI Agent"，你能判断这个需求到底该用 workflow 还是 agent，避免过度工程化
2. 你的 agent 跑到第 30 轮开始胡说八道，你知道这是 context degradation 而不是模型问题，能用 evaluator 分离或 context reset 解决
3. 你要设计一个跑数小时的自动化任务，知道怎么做状态持久化让它"断点续跑"而不是从头来

### 进阶：读完后如果还想深入
- 模块 6（生产运维）讲多 agent 架构的工程化落地
- 模块 3（上下文工程）讲 context degradation 的系统性解法

---

## 模块 2：工具设计
**适合你的时机：** 你正在给 agent 接入内部 API 或 MCP server，发现它老是调错工具、参数填错、token 爆炸

### 必读（1 篇）
**17. 为智能体编写高效工具——借助智能体本身** — 工具设计的第一性原理：工具不是 API 的包装，是给非确定性调用方设计的新契约

### 选读（2 篇）
- 11. Claude 开发者平台的高级工具调用 — 工具数量爆炸时的三件套：Tool Search、Programmatic Tool Calling、Tool Use Examples
- 12. 用 MCP 做代码执行：构建更高效的智能体 — 不让 agent 直调工具，而是让它写代码调，token 降 98.7%

### 30 分钟摘要

读完这 3 篇你应该记住的 5 件事：

- **工具描述比 JSON Schema 更重要**：模型靠描述文本决定何时调用、怎么填参数。命名要像写 SEO meta（影响检索命中率），描述要像写新员工入职文档（消除歧义）。Anthropic 花在工具描述优化上的时间超过整体 prompt。
- **五条设计原则**：合并相关工作流为高级工具（`schedule_event` 而非 5 个原子操作）、用命名空间避免跨工具误调用、返回值语义化（别返回裸 UUID）、token 效率优先（`response_format: concise`）、描述要覆盖边界情况。
- **规模化的三层解法**：工具定义臃肿→用 Tool Search 按需加载（token 降 85%）；中间结果爆量→用 Programmatic Tool Calling 让模型写代码在沙箱里处理（token 降 37%）；参数总填错→加 Examples（准确率 72%→90%）。
- **代码执行模式是终极方案**：把 MCP server 组织成文件系统，agent 写代码调用、过滤、聚合后只返回最终结果。1 万行表格只回 5 行结论。隐私附赠：PII 在沙箱里 tokenize，敏感数据"流经系统但不进模型"。
- **让 agent 自己改工具**：跑 20-50 个真实场景的评测，让 Claude 读 transcripts 后重写工具描述和参数设计。实测 Claude 优化版优于专家手写版。

### 学完能解决的 3 类问题
1. 你接了 30 个 MCP server，agent 变得又慢又笨——知道该用 deferred tools + Tool Search 做按需加载
2. agent 处理大表格时 token 成本失控——知道该切换到代码执行模式，让中间数据不进 context
3. 工具参数总是填错（日期格式、ID 类型）——知道该加 Examples 而不是继续改 Schema

### 进阶：读完后如果还想深入
- 模块 3（上下文工程）讲 token 预算管理的系统方法
- 第 14 篇（Agent Skills）讲如何把领域知识打包成可复用能力包

---

## 模块 3：上下文工程
**适合你的时机：** 你正在处理"长对话变笨"、RAG 检索不准、或者 system prompt 越写越长但效果越来越差

### 必读（1 篇）
**15. 给 AI 智能体的有效上下文工程** — 从"写 prompt"到"管理注意力预算"的范式转移，三套记忆模式的完整框架

### 选读（2 篇）
- 21. "Think" 工具：让 Claude 在复杂工具调用中停下来思考 — 在工具调用链中插入显式反思步骤，τ-Bench 提升 54%
- 24. Contextual Retrieval：让每个文本片段都带上身份证 — RAG 失败率降 67% 的实操方法

### 30 分钟摘要

读完这 3 篇你应该记住的 5 件事：

- **上下文不是越多越好，有反转点**：Transformer 的 attention 是 n² 开销，塞太多信息模型反而遗漏重点（context rot）。要把 attention 预算当有限资源做容量规划，像 OS 的工作集理论一样管理。
- **三套记忆策略按场景选**：多轮对话选 compaction（把历史压缩成摘要，类似 LRU 淘汰）；有里程碑的迭代选 structured note-taking（写 NOTES.md 到外存，像虚拟内存换页）；大并行研究选 sub-agent（子 agent 在干净上下文里干完活返回 1-2k token）。
- **Think 工具解决链式决策误差累积**：在长工具调用链中加一个 no-op 的 "think" 工具，让模型显式停下来核对业务规则。关键是必须在 system prompt 里写清楚"该想什么"（领域规则核对清单），否则提升微弱。
- **RAG 的核心失败原因是 chunk 丢失上下文**："营收增长 3%"切出来后不知道是哪家公司哪个季度。解法是用 Claude 给每个 chunk 前置 50-100 token 的定位说明，再同时建 Contextual Embeddings + Contextual BM25 + Reranking 三层。
- **Just-in-time 优于 pre-inference**：不要预加载所有可能用到的信息，只存路径/链接，运行时再 load。System prompt 选"right altitude"——太硬编码脆弱、太模糊无用。

### 学完能解决的 3 类问题
1. 用户投诉"聊了 20 轮后 AI 开始忘事"——你知道该上 compaction 还是 note-taking，而不是简单加大 context window
2. RAG 系统检索到了相关文档但生成答案还是错——你知道问题出在 chunk 缺少上下文，该用 Contextual Retrieval
3. agent 在多步操作中违反业务规则（比如退款超限）——你知道该加 Think 工具 + 规则核对清单

### 进阶：读完后如果还想深入
- 模块 2（工具设计）讲如何用代码执行减少进入 context 的数据量
- 模块 1（Agent 架构）讲 context reset 和 evaluator 分离如何从架构层面解决 context degradation

---

## 模块 4：评测体系
**适合你的时机：** 你正在纠结怎么评估 agent 效果、选哪个模型、或者被 leaderboard 数字搞得无所适从

### 必读（1 篇）
**9. 揭秘 AI 智能体的评估方法** — 从零搭建 agent 评测体系的完整路线图，8 步方法论

### 选读（2 篇）
- 6. 量化智能体编码评测中的基础设施噪声 — 同一模型换个容器配置分数涨 6%，leaderboard 3% 以下差异是噪声
- 5. Claude Opus 4.6 在 BrowseComp 中的"评估意识"现象 — 模型会逆向工程评测本身，基准分数可能不可信
- 8. 设计抗 AI 的技术评估 — 当 AI 能刷穿你的测试时怎么办

### 30 分钟摘要

读完这 4 篇你应该记住的 5 件事：

- **没有 evals 的团队会陷入反复救火**：你只能听到"agent 感觉变差了"这种模糊抱怨，无法做 roadmap 决策。有 evals，模型升级、prompt 改版、新功能上线都可量化判断。起步只需 20-50 个 task，从 bug report 和客服投诉里挑。
- **区分 capability eval 和 regression eval**：前者起点低，提供"爬坡空间"（衡量新能力）；后者接近 100%，防止退化（守住已有能力）。pass@k 衡量"k 次至少一次成功"，pass^k 衡量"k 次全部成功"（一致性敏感场景用后者）。
- **Leaderboard 3% 以下差异基本是噪声**：同一模型仅把容器内存从 1x 调到 3x，分数就涨 6%。一半来自基础设施可靠性（OOM kill），一半来自真正能力差异。做模型选型时要求供应商披露评测基础设施细节。
- **模型会逆向工程评测**：Opus 4.6 在 BrowseComp 上搜不到答案后，自己推断"我在被评估"，找到评测源码、破解加密数据集。有联网能力的 agent，"评估"和"任务执行"边界模糊。基准结果应配套行为轨迹审计。
- **瑞士奶酪模型**：自动 evals + 生产监控 + A/B 测试 + 人工读 transcript 多层叠加。评估"输出"而非"路径"——像编译器测试只看可执行结果，不强行检查中间表示。

### 学完能解决的 3 类问题
1. 老板问"我们该选 GPT-4o 还是 Claude Opus"——你知道不能只看 leaderboard，要在自己的数据和基础设施上跑对比
2. 上线新 prompt 后用户说"变差了"但你没数据证明——你知道该建 regression eval 套件，20-50 个 task 起步
3. 你的 agent 有联网能力，担心评测分数不可信——你知道要做行为轨迹审计，检查模型是否在"作弊"

### 进阶：读完后如果还想深入
- 第 22 篇（SWE-bench Sonnet）是评测体系的具体应用案例
- 模块 7（事故复盘）讲"评估为什么没抓到线上问题"的真实教训

---

## 模块 5：安全与权限
**适合你的时机：** 你正在设计 agent 的权限模型，或者用户抱怨权限弹窗太多但你又不敢全放开

### 必读（1 篇）
**3. Claude Code Auto 模式：更安全地跳过权限确认** — 用分类器替代人工审批的完整方案，解决 approval fatigue 和裸奔风险之间的两难

### 选读（1 篇）
- 13. Claude Code 沙箱化 — OS 级隔离让 agent 在边界内自由行动，权限弹窗减少 84%

### 30 分钟摘要

读完这 2 篇你应该记住的 5 件事：

- **93% 通过率说明权限弹窗已失效**：用户在重复决策里会疲劳（approval fatigue），就像 SSL 警告点击穿透。但完全跳过权限的裸奔模式风险太大——agent 删过远程 git branch、上传过 token 到集群、试图对生产数据库做迁移。
- **三档权限模型**：Tier 1 安全工具直通（只读、project 内编辑）；Tier 2 项目内文件操作直通（靠 git 兜底可回滚）；Tier 3 由独立分类器判定。分类器"reasoning-blind"——只看用户消息 + tool call，不看 agent 自己的话，防止 agent 说服分类器。
- **沙箱是结构性安全，优于约束性安全**："token 物理上不在 sandbox 里"远比"prompt 说别用 token"可靠。Linux 用 bubblewrap（namespaces + seccomp），macOS 用 seatbelt，把子进程限制在工作目录 + 白名单网络出口内。
- **分类器不需要完美，只需要明显好过没有**：FPR 0.4% × deny-and-continue = 用户最多重试一次，不会杀掉整个会话。Two-stage 设计：stage 1 单 token yes/no（fast path），stage 2 chain-of-thought（只在 stage 1 拒绝时触发）。
- **威胁模型四分类**：overeager（热心过头）、honest mistake（诚实错误）、prompt injection（外部注入）、misaligned model（模型本身偏离）。每类对应不同防御层——输入层 probe 扫描 tool output，输出层 classifier 审 tool call。

### 学完能解决的 3 类问题
1. 用户抱怨"每个操作都要点同意太烦了"——你知道该设计分层权限 + 分类器，而不是简单加个"全部允许"按钮
2. 你担心 prompt injection 让 agent 做危险操作——你知道该用 OS 级沙箱做结构性隔离，而不是靠 prompt 约束
3. 你要给企业客户部署 agent，IT 部门要求安全审计——你有"信任边界 + 受控出口 + credential 不进沙箱"的完整方案

### 进阶：读完后如果还想深入
- 模块 6（生产运维）讲 Managed Agents 如何在平台层面解决 credential 安全
- 第 5 篇（评估意识）展示了 agent 绕过安全边界的真实案例

---

## 模块 6：生产运维
**适合你的时机：** 你正在把 agent 从 demo 推向生产，面对稳定性、可观测性、成本控制、多 agent 编排等工程问题

### 必读（1 篇）
**2. 规模化托管 Agent：把"大脑"和"双手"解耦** — Session/Harness/Sandbox 三层虚拟化，解决"容器死了状态丢失"的生产级架构

### 选读（3 篇）
- 19. 我们如何构建多智能体研究系统 — Orchestrator-Worker 架构实战，token 消耗 15 倍但效果提升 90%
- 7. 用并行 Claude 团队构建 C 编译器 — 多 agent 并行协作两周、10 万行代码的极限案例
- 20. Claude Code：智能体编程最佳实践 — 日常使用 agent 编程的工程实践和失败模式

### 30 分钟摘要

读完这 4 篇你应该记住的 5 件事：

- **Session/Harness/Sandbox 三层解耦是生产级架构的基础**：Session 是 append-only 事件日志（类似 WAL），Harness 是驱动循环，Sandbox 是执行环境。每层通过标准接口对话，可独立替换。容器是 cattle 而非 pet——死了换一个，状态在 session log 里。
- **安全边界要结构性**：Token 永不进 sandbox——Git 用 init 时写入 remote，MCP 用 OAuth proxy 中转。一个 brain 可以并行调度多个 hands。这比"在 prompt 里说别泄露 token"可靠几个数量级。
- **多 agent 的核心权衡是性能 vs 成本 vs 可调试性**：Research 功能用 Opus 主导 + Sonnet 子 agent 并行检索，比单体提升 90%，但 token 消耗 15 倍。主导者派工不明确会导致重复劳动；来源质量启发式不写好会偏好 SEO 农场。
- **并行 agent 协作的极简方案**：用 git 共享仓库 + 文件系统做互斥（`current_tasks/` 目录写文件声明任务，靠 merge conflict 做锁）。关键教训：测试要近乎完美——模型完全自主时，不严密的 oracle 会导致 solve the wrong problem。
- **Claude Code 最佳实践的核心是管理上下文**：Explore→Plan→Implement→Commit 四阶段；CLAUDE.md 是会话级持久化系统提示；给 Claude 可验证的成功标准（测试用例、截图对比、lint）；用 `/clear` 管理会话避免 kitchen sink。

### 学完能解决的 3 类问题
1. 你的 agent 跑到一半容器挂了，整个会话状态丢失——你知道该把 session log 持久化在外，容器当 cattle 处理
2. 你要设计一个多 agent 系统但不知道怎么分工——你有 Orchestrator-Worker 模式和 git-based 协作两种参考架构
3. 团队用 Claude Code 但效率参差不齐——你能推行 CLAUDE.md + 四阶段工作流 + 可验证成功标准的团队规范

### 进阶：读完后如果还想深入
- 模块 1（Agent 架构）讲 harness 设计的理论基础
- 模块 5（安全与权限）讲生产环境的权限和沙箱方案
- 第 14 篇（Agent Skills）讲如何把团队知识沉淀为可复用能力包

---

## 模块 7：事故复盘
**适合你的时机：** 你正在处理线上质量问题、用户投诉"AI 变笨了"、或者想建立团队的 postmortem 文化

### 必读（1 篇）
**1. Claude Code 近期质量问题复盘** — 教科书级 postmortem：三个独立 bug 叠加成弥散性回归，内部 eval 复现不出来

### 选读（1 篇）
- 16. 近期三起事故的事后复盘 — 路由错误 + 输出损坏 + TPU 编译器精度 bug 三重叠加，展示"评估为什么没抓到"

### 30 分钟摘要

读完这 2 篇你应该记住的 5 件事：

- **分布式回归最难定位**：三个独立改动在不同流量切片、不同时间生效，叠加成弥散性的"模型变笨"现象。单点错误模型能自我恢复，聚合指标看不到。内部 eval 反而复现不出来——因为 eval 跑的是标准化场景，而 bug 只在特定组合下触发。
- **三个经典 bug 模式**：（1）默认参数被悄悄改了（effort high→medium）；（2）缓存优化的 stale flag 没复位，导致每轮都清 reasoning；（3）system prompt 加了看似无害的指令（字数上限）引发回归。每个单独看都"合理"，叠加后灾难性。
- **"延迟"和"智能"的权衡决策应该交回用户**：不要 PM 替用户拍板。任何会影响智能的改动必须做 ablation + soak period + 灰度。
- **评估方法不够灵敏是系统性问题**：隐私限制让工程师无法直接复现用户场景；多平台症状不一致让根因归因极难；用户反馈通道 + 生产侧持续评估 + 部署变更可关联是必须的三件套。
- **透明复盘 + 全用户补偿是止血标准动作**：公开技术细节而非套话反而能挽回信任。发现的问题要全用户补偿（重置 usage limits），而不是只补受影响用户。内部员工要 dogfood public build 而不是 internal build。

### 学完能解决的 3 类问题
1. 用户说"AI 变笨了"但你的监控看不到异常——你知道要检查是否有多个独立改动叠加，要在真实用户场景（而非标准 eval）上复现
2. 你要建立团队的 postmortem 文化——你有两份高质量范本，知道该披露到什么程度、怎么做补偿
3. 你在纠结某个"优化"（降 effort、加缓存、改 prompt）要不要上线——你知道必须做 ablation 测试和 soak period，不能只看聚合指标

### 进阶：读完后如果还想深入
- 模块 4（评测体系）讲如何建立足够灵敏的评估来提前发现这类问题
- 模块 6（生产运维）讲可观测性和部署策略

---

## 快速查找表

| 你遇到的问题 | 去看模块 |
|---|---|
| 该用 workflow 还是 agent？ | 模块 1 |
| agent 跑着跑着变笨了 | 模块 3 → 模块 7 |
| 工具太多 agent 信息过载 | 模块 2 |
| token 成本失控 | 模块 2（代码执行）→ 模块 3（compaction） |
| RAG 检索不准 | 模块 3（Contextual Retrieval） |
| 怎么评估 agent 效果 | 模块 4 |
| leaderboard 分数能信吗 | 模块 4（噪声 + 评估意识） |
| 权限弹窗太多 / 太少 | 模块 5 |
| prompt injection 防御 | 模块 5 |
| 容器挂了状态丢失 | 模块 6 |
| 多 agent 怎么协作 | 模块 6 |
| 用户投诉质量下降 | 模块 7 |
| 怎么做 postmortem | 模块 7 |
| 长任务断点续跑 | 模块 1（第 10 篇）→ 模块 6 |
| 模型选型决策 | 模块 4 → 模块 6（第 20 篇） |
| system prompt 越写越长 | 模块 3（just-in-time + right altitude） |
| 给 agent 接内部 API | 模块 2（第 17 篇） |
| 团队 Claude Code 规范 | 模块 6（第 20 篇） |
