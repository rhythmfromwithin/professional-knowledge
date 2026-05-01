---
interest: medium
link: https://arxiv.org/abs/2604.25080
next_step: skim
priority: medium
slack_ts: '1777608123.076629'
source: cs.DC - Distributed Computing
status: unread
title: 'CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration'
---
# CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration
> 原文: [https://arxiv.org/abs/2604.25080](https://arxiv.org/abs/2604.25080)

arXiv:2604.25080v1 Announce Type: new
Abstract: KV cache restoration has emerged as a dominant bottleneck in serving long-context LLM workloads, including multi-turn conversations, retrieval-augmented generation, and agentic pipelines. Existing approaches treat restoration as a per-request tradeoff between recomputation and I/O transfer, recomputing KV states from scratch or offloading them from external storage (e.g., CPU memory or remote machines). However, existing advances fail to exploit parallelism across tokens, layers, and distributed deployments, and critically ignore resource contention under batched serving. We present CacheFlow, a KV cache restoration framework that rethinks cache restoration as a multi-dimensional parallel execution problem. CacheFlow introduces a unified 3D parallelism abstraction across tokens, layers, and GPUs, enabling fine-grained overlap of recomputation and I/O along the structural dependencies of transformer inference. At the core of CacheFlow is a batch-aware two-pointer scheduler that jointly optimizes compute and I/O allocation across requests by prioritizing operations with the highest marginal reduction in recomputation cost. Our evaluations show that CacheFlow reduces Time-To-First-Token (TTFT) by 10%-62% over existing advances across diverse models, workloads, and hardware.
