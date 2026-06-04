---
interest: medium
link: https://arxiv.org/abs/2606.02784
next_step: skim
priority: low
slack_ts: '1780548664.279489'
source: cs.DB - Databases
status: unread
title: 'LAANN: I/O-Aware Look-Ahead Search for Disk-Based Approximate Nearest Neighbor
  Search'
---
# LAANN: I/O-Aware Look-Ahead Search for Disk-Based Approximate Nearest Neighbor Search
> 原文: [https://arxiv.org/abs/2606.02784](https://arxiv.org/abs/2606.02784)

arXiv:2606.02784v1 Announce Type: new
Abstract: Approximate nearest neighbor search (ANNS) is a fundamental primitive in large-scale retrieval, recommendation, and AI systems. As vector datasets grow to billions or even trillions of items, disk-based ANNS systems have emerged to handle this scale by storing vector data and index structures on storage systems, but their query performance remains dominated by I/O latency. Existing disk-based ANNS systems primarily optimize I/O efficiency or overlap I/O with computation, but they treat CPU computation and I/O access as largely separate components. This separation misses a critical opportunity: selectively processing candidates already cached in memory before making I/O decisions can reduce unnecessary disk accesses and improve search quality. However, exploiting this opportunity is challenging because excessive computation can delay critical I/O operations, while poorly chosen computation provides little benefit, potentially increasing overall query latency.
In this paper, we present LAANN, a disk-based ANNS system that makes graph search explicitly I/O-aware by co-optimizing CPU computation and I/O access. LAANN combines three techniques: look-ahead search, which adapts the search strategy across query stages to balance I/O reduction and timely I/O issuance; a priority I/O-CPU pipeline, which uses I/O waiting time to process candidates cached in memory according to their expected impact on upcoming I/O decisions; and a fast lightweight in-memory graph index, which provides high-quality initial candidates to accelerate convergence and reduce disk accesses. Experiments on million- and billion-scale datasets demonstrate that LAANN substantially outperforms state-of-the-art disk-based ANNS systems. At Recall@10 = 0.9, LAANN achieves 1.41x-4.66x higher throughput, 29%-79% lower latency, and 1.59x-6.34x fewer I/O operations.
