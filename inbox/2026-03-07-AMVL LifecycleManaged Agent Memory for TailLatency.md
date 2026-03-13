---
interest: medium
link: https://arxiv.org/abs/2603.04443
next_step: skim
priority: medium
slack_ts: '1773369815.503299'
source: cs.DC - Distributed Computing
status: unread
title: 'AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running
  LLM Systems'
---
# AMV-L: Lifecycle-Managed Agent Memory for Tail-Latency Control in Long-Running LLM Systems
> 原文: [https://arxiv.org/abs/2603.04443](https://arxiv.org/abs/2603.04443)

arXiv:2603.04443v1 Announce Type: new
Abstract: Long-running LLM agents require persistent memory to preserve state across interactions, yet most deployed systems manage memory with age-based retention (e.g., TTL). While TTL bounds item lifetime, it does not bound the computational footprint of memory on the request path: as retained items accumulate, retrieval candidate sets and vector similarity scans can grow unpredictably, yielding heavy-tailed latency and unstable throughput. We present AMV-L (Adaptive Memory Value Lifecycle), a memory-management framework that treats agent memory as a managed systems resource. AMV-L assigns each memory item a continuously updated utility score and uses value-driven promotion, demotion, and eviction to maintain lifecycle tiers; retrieval is restricted to a bounded, tier-aware candidate set that decouples the request-path working set from total retained memory. We implement AMV-L in a full-stack LLM serving system and evaluate it under identical long-running workloads against two baselines: TTL and an LRU working-set policy, with fixed prompt-injection caps. Relative to TTL, AMV-L improves throughput by 3.1x and reduces latency by 4.2x (median), 4.7x (p95), and 4.4x (p99), while reducing the fraction of requests exceeding 2s from 13.8% to 0.007%. Compared to LRU, AMV-L trades a small regression in median/p95 latency (+26% / +3%) for improved extreme-tail behavior (-15% p99; -98% >2s) and lower token overhead (approximately 6% fewer tokens/request), while matching retrieval quality (value means within approximately 0-2%). The gains arise primarily from bounding retrieval-set size and vector-search work, not from shortening prompts. Our results show that predictable performance for long-running LLM agents requires explicit control of memory working-set size and value-driven lifecycle management, rather than retention time alone.
