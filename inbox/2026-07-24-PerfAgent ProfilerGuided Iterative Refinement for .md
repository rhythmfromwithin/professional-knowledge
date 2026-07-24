---
title: "PerfAgent: Profiler-Guided Iterative Refinement for Repository-Level Code Optimization"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2607.19653
priority: low
status: unread
interest: medium
next_step: skim
---
# PerfAgent: Profiler-Guided Iterative Refinement for Repository-Level Code Optimization
> 原文: [https://arxiv.org/abs/2607.19653](https://arxiv.org/abs/2607.19653)

arXiv:2607.19653v1 Announce Type: new
Abstract: Large language model (LLM) agents now perform well on correctness-oriented repository-level tasks, including SWE-Bench issue resolution and feature implementation in real codebases. However, they still struggle with repository-level code optimization, which requires preserving behavior while improving runtime performance. Passing tests is not enough in this setting; a patch must preserve behavior, implement code optimization, and approach expert speedups. Current agents often miss bottlenecks hidden behind abstraction layers and native extensions, stop after shallow speedups, or insufficiently test the code patches that thus may silently break edge cases. We present PerfAgent, a profiler-guided, verifier-in-the-loop workflow that gives an off-the-shelf coding agent the feedback needed to find real hotspots, improve beyond the first passing patch, and use profiler evidence rather than timing alone to decide what to optimize next. On two challenging optimization benchmarks, GSO and SWE-fficiency-Lite, PerfAgent more than doubles the rate of expert-matching patches over OpenHands with GPT-5.1, improving from 19.6% to 39.2% on GSO and from 26% to 74% on SWE-fficiency-Lite. It also surpasses an oracle best-of-five baseline at substantially lower cost, showing that the gains come from better feedback rather than additional test-time sampling.
