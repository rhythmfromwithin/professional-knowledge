---
interest: medium
link: https://arxiv.org/abs/2607.08956
next_step: skim
priority: low
slack_ts: '1783998904.543999'
source: cs.DB - Databases
status: unread
title: Accelerating Point-in-Polygon Predicates via Algebraic Hash-Joins and Discrete
  Global Grids at Scale
---
# Accelerating Point-in-Polygon Predicates via Algebraic Hash-Joins and Discrete Global Grids at Scale
> 原文: [https://arxiv.org/abs/2607.08956](https://arxiv.org/abs/2607.08956)

arXiv:2607.08956v1 Announce Type: new
Abstract: Traditional vector-based point-in-polygon queries rely on computationally expensive geometric predicates that scale poorly for massive datasets, even when accelerated by spatial indices. Discrete Global Grid Systems (DGGS) offer a scalable alternative by discretizing geometries into hierarchical cells, transforming complex spatial relations into constant-time relational hash-joins. However, adopting a DGGS introduces an overhead to encode data, and current grid implementations exhibit a significant performance ``tooling gap.'' In this demonstration, we present an interactive dashboard that empirically evaluates these computational tradeoffs across four DGGS implementations (H3, S2, A5, and ISEA4H) using DuckDB. Through progressive scenarios, the platform visualizes the overhead of on-the-fly encoding and demonstrates how pre-indexing spatial datasets eliminates this overhead. Ultimately, the demo proves that when data is pre-indexed, all DGGS regardless of their mathematical complexity or tooling converge to sub-second join latencies, unlocking the throughput of modern vectorized execution engines.
