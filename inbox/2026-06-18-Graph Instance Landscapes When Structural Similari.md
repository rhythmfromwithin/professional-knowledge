---
interest: medium
link: https://arxiv.org/abs/2606.18267
next_step: skim
priority: low
slack_ts: '1781759642.173629'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Graph Instance Landscapes: When Structural Similarity Does (Not) Reflect Shortest-Path
  Performance'
---
# Graph Instance Landscapes: When Structural Similarity Does (Not) Reflect Shortest-Path Performance
> 原文: [https://arxiv.org/abs/2606.18267](https://arxiv.org/abs/2606.18267)

arXiv:2606.18267v1 Announce Type: cross
Abstract: Benchmarking shortest-path algorithms is commonly based on aggregate performance over heterogeneous graph sets, which limits insight into how different search paradigms react to instance structure. We adopt an instance-landscape view of graph benchmarking by embedding graphs into a low-cost structural feature space and clustering them into regions of similar structure. Three benchmark suites are studied: weighted Erd\H{o}s--R\'enyi graphs, random geometric (wireless) graphs, and real-world road networks. We evaluate four representative shortest-path solvers spanning uninformed exact search (Dijkstra), bidirectional exact search (bidirectional Dijkstra), heuristic-guided exact search (A$^{\*}$), and deque-based strategies (DEQ). Clustering robustness is analyzed under multiple feature-selection schemes, and runtime distributions are compared across landscape regions using non-parametric tests. While generator parameters induce stable structural regions, we find that feature-space similarity does not necessarily imply performance similarity: significant runtime shifts are frequently observed even within the same landscape region. A merged-suite analysis further shows that different benchmark families occupy largely disjoint regions. These results highlight both the potential and the limits of structural landscapes for the structure-aware benchmarking of shortest-path algorithms.
