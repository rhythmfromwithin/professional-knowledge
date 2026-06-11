---
interest: medium
link: https://arxiv.org/abs/2606.11582
next_step: skim
priority: low
slack_ts: '1781153121.282739'
source: cs.DB - Databases
status: unread
title: Querying Cohesive Subgraph regarding Span-Constrained Triangles on Temporal
  Graphs with Dynamic Index Maintenance
---
# Querying Cohesive Subgraph regarding Span-Constrained Triangles on Temporal Graphs with Dynamic Index Maintenance
> 原文: [https://arxiv.org/abs/2606.11582](https://arxiv.org/abs/2606.11582)

arXiv:2606.11582v1 Announce Type: new
Abstract: Recent advances in temporal graph research have redefined traditional static graph concepts such as triangles, motifs, and $k$-cores. Inspired by this, we introduce a novel $(k,\delta)$-truss for temporal graphs, requiring triangles to exist within sufficiently short time windows. The $(k,\delta)$-truss ensures both static and temporal cohesion, while the original $k$-truss is a special case when $\delta = \infty$. To address $(k,\delta)$-truss queries, we propose index-free and index-based approaches. Utilizing the dual containment relation of $(k,\delta)$-trusses, our indexes losslessly compress all $(k,\delta)$-trusses into map or tree structures, significantly reducing space while enabling optimal-time retrieval. To scale to large temporal graphs, we develop two index construction algorithms based on truss decomposition and truss maintenance, respectively, which substantially reduce redundant computations. Moreover, we present techniques for the dynamic maintenance of the proposed indexes. The experimental results demonstrate that index-based approaches process queries in interactive time and outperform the index-free approach by 2$\sim$4 orders of magnitude, while the indexes achieve compression ratios of up to $10^{-4}$ and can be updated efficiently without rebuilding from scratch.
