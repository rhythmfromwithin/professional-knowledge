---
title: "LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.06676
priority: high
status: unread
interest: medium
next_step: skim
---
# LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction
> 原文: [https://arxiv.org/abs/2605.06676](https://arxiv.org/abs/2605.06676)

arXiv:2605.06676v1 Announce Type: new
Abstract: Long-context inference in Large Language Models (LLMs) is bottlenecked by the linear growth of Key-Value (KV) cache memory. Existing KV cache compression paradigms are fundamentally limited by heuristics: heuristic budgeting relies on statistical priors rather than task objectives, causing resource misallocation, while heuristic selection relies on coupled query-key interactions or static inductive biases (e.g., attention sinks). To address this limitation, we introduce LKV (Learned KV Eviction), which formulates KV compression as an end-to-end differentiable optimization problem. LKV integrates LKV-H to learn task-optimized global budgets, and LKV-T to derive intrinsic KV importance without materializing attention matrices. This design bypasses heuristic proxies, strictly aligning compression with task objectives. Extensive evaluations demonstrate that LKV achieves state-of-the-art performance on both LongBench and RULER benchmarks at high compression rates. In particular, on LongBench, LKV achieves near-lossless performance with only 15\% KV cache retention. Crucially, our analysis identifies learned budgeting as the dominant driver of fidelity, demonstrating that data-driven allocation is essential to overcome the limitations of hand-crafted heuristics.
