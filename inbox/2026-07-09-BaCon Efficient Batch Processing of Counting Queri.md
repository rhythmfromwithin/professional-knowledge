---
interest: medium
link: https://arxiv.org/abs/2607.05832
next_step: skim
priority: low
slack_ts: '1783569524.908879'
source: cs.DB - Databases
status: unread
title: 'BaCon: Efficient Batch Processing of Counting Queries [Full Version]'
---
# BaCon: Efficient Batch Processing of Counting Queries [Full Version]
> 原文: [https://arxiv.org/abs/2607.05832](https://arxiv.org/abs/2607.05832)

arXiv:2607.05832v1 Announce Type: new
Abstract: Counting queries are ubiquitous in database systems, particularly for driving internal system optimization. Learned models for cardinality estimation rely heavily on large-scale training data, yet generating such data by executing massive batches of counting queries is expensive. We propose BaCon, an efficient algorithm for batch evaluation of counting queries on top of a database system, without modifying its internals. BaCon integrates the idea of factorized databases with a workload-aware domain quantization strategy, allowing it to evaluate batches of counting queries using compact data structures rather than materializing massive join results. BaCon's design is compatible with most database management system, and we have implemented it as a client-side application on PostgreSQL with a lightweight C-language UDF (user-defined function). This implementation delivers speedups between 2$\times$ and 178$\times$ over baselines and good performance across various workloads, making training and maintenance of learned cardinality estimation models significantly more practical.
