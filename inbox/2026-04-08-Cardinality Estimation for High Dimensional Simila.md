---
interest: medium
link: https://arxiv.org/abs/2604.04603
next_step: skim
priority: low
slack_ts: '1775618435.197989'
source: cs.DB - Databases
status: unread
title: Cardinality Estimation for High Dimensional Similarity Queries with Adaptive
  Bucket Probing
---
# Cardinality Estimation for High Dimensional Similarity Queries with Adaptive Bucket Probing
> 原文: [https://arxiv.org/abs/2604.04603](https://arxiv.org/abs/2604.04603)

arXiv:2604.04603v1 Announce Type: new
Abstract: In this work, we address the problem of cardinality estimation for similarity search in high-dimensional spaces. Our goal is to design a framework that is lightweight, easy to construct, and capable of providing accurate estimates with satisfying online efficiency. We leverage locality-sensitive hashing (LSH) to partition the vector space while preserving distance proximity. Building on this, we adopt the principles of classical multi-probe LSH to adaptively explore neighboring buckets, accounting for distance thresholds of varying magnitudes. To improve online efficiency, we employ progressive sampling to reduce the number of distance computations and utilize asymmetric distance computation in product quantization to accelerate distance calculations in high-dimensional spaces. In addition to handling static datasets, our framework includes updating algorithm designed to efficiently support large-scale dynamic scenarios of data updates.Experiments demonstrate that our methods can accurately estimate the cardinality of similarity queries, yielding satisfying efficiency.
