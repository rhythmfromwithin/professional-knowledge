---
interest: medium
link: https://arxiv.org/abs/2611.13856
next_step: skim
priority: low
slack_ts: '1794550327.042959'
source: cs.DB - Databases
status: unread
title: 'SAIL: Self-Adaptive Index Learning with Hybrid Models (Extended Version)'
---
# SAIL: Self-Adaptive Index Learning with Hybrid Models (Extended Version)
> 原文: [https://arxiv.org/abs/2611.13856](https://arxiv.org/abs/2611.13856)

arXiv:2611.13856v1 Announce Type: new
Abstract: Learned index structures have demonstrated a significant improvement in query performance over traditional index structures. The majority of learned indexes use a uniform node structure throughout their index structures. A few studies show that combining multiple types of node structures can lead to indexes that better adapt to local key-set distributions, hence yielding query efficiency gains. Following this line of work, we propose a learned index structure named SAIL that supports a wide range of different candidate node structures for both leaf and inner nodes, selected via cost models based on data driven approximations. We design an efficient construction algorithm that recursively partitions the key-set to be fitted by the candidate node types. Experiments demonstrate that SAIL achieves 2x improvement over existing learned indexes in query time, with similar memory consumption and index build times.
