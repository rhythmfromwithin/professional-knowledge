---
interest: medium
link: https://arxiv.org/abs/2605.15222
next_step: skim
priority: low
slack_ts: '1779164078.677209'
source: cs.SE - Software Engineering
status: unread
title: 'PerfCodeBench: Benchmarking LLMs for System-Level High-Performance Code Optimization'
---
# PerfCodeBench: Benchmarking LLMs for System-Level High-Performance Code Optimization
> 原文: [https://arxiv.org/abs/2605.15222](https://arxiv.org/abs/2605.15222)

arXiv:2605.15222v1 Announce Type: new
Abstract: Large language models (LLMs) can often generate functionally correct code, but their ability to produce efficient implementations for performance-critical systems tasks remains limited. Existing code benchmarks mainly emphasize correctness or algorithmic problem solving, while realistic systems-level optimization is still underexplored. To address this gap, we introduce PerfCodeBench, an executable benchmark for evaluating LLMs on high-performance code optimization. The tasks require system-level implementation choices, hardware-aware optimization, and careful handling of performance bottlenecks. Each task includes executable correctness checks, a baseline implementation, and a reference optimized solution. This allows us to evaluate both correctness and runtime-oriented efficiency. Our evaluation on a broad set of state-of-the-art LLMs shows a clear gap between model-generated code and expert-optimized implementations. The gap is especially large on tasks involving parallelism and GPU operations. Current models also show weaknesses in cross-language robustness and in consistently reaching expert-level efficiency. These results suggest that performance-aware evaluation are still needed. LLMs should move beyond generating merely correct code toward producing efficient systems software. We submit the benchmark data, evaluation infrastructure, and complete logs of all LLMs-generated code at https://anonymous.4open.science/r/perfcodebench-7CDE.
