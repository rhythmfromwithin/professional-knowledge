---
title: "One Ring to Shuffle Them All: Scalable Intra-Process Data Redistribution with Ring-Buffer Shuffle in Redpanda Oxla"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.29099
priority: low
status: unread
interest: medium
next_step: skim
---
# One Ring to Shuffle Them All: Scalable Intra-Process Data Redistribution with Ring-Buffer Shuffle in Redpanda Oxla
> 原文: [https://arxiv.org/abs/2605.29099](https://arxiv.org/abs/2605.29099)

arXiv:2605.29099v1 Announce Type: new
Abstract: As server CPUs scale to dozens and now hundreds of cores per socket, parallel query engines must rethink how they redistribute data between threads. Partitioned operators such as hash joins and aggregations require frequent data redistribution across threads, yet existing intra-process shuffle designs fundamentally fail to scale with core count: batch partitioning avoids cross-thread synchronization in the hot path but materializes all intermediate data, introduces a global producer/consumer barrier, and requires a consumption approach with low cache locality, while channel-based streaming avoids materialization but incurs per-channel synchronization that scales poorly with core count. As core counts rise, these architectural tradeoffs increasingly prevent engines from fully utilizing modern hardware.
We present a ring-buffer streaming shuffle design that addresses these shortcomings through lock-free atomic slot acquisition into fixed-size batch groups, achieving amortized O(1) synchronization cost per batch and O(M) memory independent of input size. Ring-buffer shuffle has been implemented in Redpanda's Oxla query engine for two years, where it currently powers production queries for Redpanda SQL users.
We evaluate all three approaches on a 72-core NVIDIA GraceHopper, a 192-core dual-socket AWS Graviton4, and a 96-core (192-thread) AMD EPYC. On a 72-core single-socket system the ring buffer outperforms channel streaming by up to 44% and batch partitioning by up to 79%; at 192 cores the advantage over channel grows to over 100% and over 300% versus batch partitioning. Even so, on chiplet architectures with many partitioned L3 caches, the shared atomic counter becomes a cross-die bottleneck and channel-based streaming remains competitive. End-to-end Graviton4 evaluation on TPC-H (21 queries) and ClickBench (43 queries) shows the advantage is workload-shape-dependent.
