---
interest: medium
link: https://arxiv.org/abs/2611.21835
next_step: skim
priority: low
slack_ts: '1795157488.892589'
source: cs.DB - Databases
status: unread
title: Revisiting Index Performance under High Cache-Miss Penalties
---
# Revisiting Index Performance under High Cache-Miss Penalties
> 原文: [https://arxiv.org/abs/2611.21835](https://arxiv.org/abs/2611.21835)

arXiv:2611.21835v1 Announce Type: new
Abstract: Modern data-intensive applications often query very large datasets, making index performance critical. Recent index structures exploit the fine-grained access capabilities of emerging storage devices such as DCPMM and CXL. However, existing benchmarks typically evaluate indexes in isolation using saturated, closed-loop workloads that emphasize maximum throughput. Such workloads favor highly concurrent designs while overlooking the application work that follows an index lookup and competes for cache, memory bandwidth, and CPU resources. We present AuxBench - a microbenchmark that evaluates indexes as auxiliary access paths within larger application workloads. Using AuxBench, we evaluate four byte-addressable indexes under controlled post-lookup memory activity, concurrency, and request arrival patterns. Our experiments show that post-lookup memory activity can change the relative performance of competing indexes, that concurrency-oriented designs may lose their advantages when substantial application work is introduced, and that time-varying request arrivals can produce severe tail latency near saturation. These findings demonstrate why index-only benchmarks may not adequately predict performance in larger application workloads
