---
title: "SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.02304
priority: low
status: unread
interest: medium
next_step: skim
---
# SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation
> 原文: [https://arxiv.org/abs/2610.02304](https://arxiv.org/abs/2610.02304)

arXiv:2610.02304v1 Announce Type: new
Abstract: Existing Simulink benchmarks mainly evaluate whether generated models compile, execute, or resemble a reference model. These criteria do not establish whether a model satisfies its engineering requirements. We introduce SimuVerity, a benchmark of 101 text-to-executable Simulink model-generation tasks across ten engineering domains. For each task, executable-system profiles ground the engineering specification and four families of native simulation scenarios. A hierarchical evaluator first checks artifact delivery, native executability, and engineering qualification, then scores qualified models across six dimensions covering accuracy, output quality, mechanistic fidelity, control and causal integrity, operating-domain robustness, and dynamic response. We evaluate six agent systems with SimuVerity. The best system achieves an overall score of only 42.86. The results show that structural similarity is a poor proxy for engineering performance: capability bottlenecks arise both in producing qualified implementations and in satisfying multidimensional requirements after qualification. Meanwhile, some high-scoring models still exhibit severe visual-layout disorder. SimuVerity provides a systematic basis for assessing agents' engineering capabilities and diagnosing failures in executable Simulink model generation.
