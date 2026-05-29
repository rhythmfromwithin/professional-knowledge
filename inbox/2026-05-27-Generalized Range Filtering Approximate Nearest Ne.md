---
interest: medium
link: https://arxiv.org/abs/2605.26474
next_step: skim
priority: low
slack_ts: '1780028377.927859'
source: cs.DB - Databases
status: unread
title: 'Generalized Range Filtering Approximate Nearest Neighbor Search: Containment
  and Overlap [Technical Report]'
---
# Generalized Range Filtering Approximate Nearest Neighbor Search: Containment and Overlap [Technical Report]
> 原文: [https://arxiv.org/abs/2605.26474](https://arxiv.org/abs/2605.26474)

arXiv:2605.26474v1 Announce Type: new
Abstract: Approximate nearest neighbor (ANN) search with range filters has recently garnered significant attention. This paper delves into a generalized form of this problem, i.e., ANN search with exact range-range (RR) predicates on a range-valued attribute, named RR filtering ANN (RRANN). Specifically, given $n$ vectors in $\mathbb{R}^d$, each vector $v\_i$ is associated with a numeric range $[l\_i, r\_i]$, symbolizing aspects like a price range or time interval. An RRANN query $(v\_q, l\_q, r\_q)$ aims at finding $k$ vectors closest to $v\_q$ within the vectors satisfying an arbitrary RR predicate defined between the query range $[l\_q, r\_q]$ and the object range $[l\_i, r\_i]$. The RR predicate remains unspecified, enabling user-defined conditions. It may encompass containment ($[l\_i, r\_i] \subseteq [l\_q, r\_q]$ or $[l\_q, r\_q] \subseteq [l\_i, r\_i]$), overlap ($l\_i \le l\_q \le r\_i \le r\_q$ or $l\_q \le l\_i \le r\_q \le r\_i$), or a disjunction of them. RRANN has broad applications in queries related to price ranges or time intervals, and it generalizes existing variants of ANN search with range filters. However, existing dedicated approaches for these problems lack the capacity to support queries with arbitrary RR predicates. Hence, we introduce a new approach, labeled multi-segment tree graph. It efficiently handles arbitrary RR predicates by avoiding traversal through non-predicate-satisfied nodes, and keeps equivalent index size and construction time to state-of-the-art methods for RFANN. Extensive experiments on real-world data demonstrate the efficacy of our approach in RRANN queries, achieving up to 12.5x speedups with the same accuracy as the baselines. Moreover, our approach attains comparable RFANN search performance and notably superior IFANN and TSANN search performance compared to the respective state-of-the-art approaches. Our code is available at https://github.com/FanEDG/MSTG.
