---
title: "Fiber-Navigable Search: A Geometric Approach to Filtered ANN"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.00102
priority: low
status: unread
interest: medium
next_step: skim
---
# Fiber-Navigable Search: A Geometric Approach to Filtered ANN
> 原文: [https://arxiv.org/abs/2604.00102](https://arxiv.org/abs/2604.00102)

arXiv:2604.00102v1 Announce Type: new
Abstract: We present a geometric framework for filtered approximate nearest neighbor (ANN) search. Filtering a proximity graph by a metadata predicate produces a subgraph, a fiber, whose connectivity and geometry can differ sharply from the full graph. Using local signals, we propose a two-phase search algorithm that combines full-graph exploration with filtered-neighbor descent when the local geometry is favorable. These signals also classify search failures into three regimes: topological cuts, geometric folds, and genuine basins. A key observation is that all three share a common resolution: restarting the search in a fiber-present cluster near the query. To support this, we introduce a lightweight anchor structure that identifies such regions and restarts the search accordingly. We show empirically that the method outperforms FAISS HNSW on filtered search and the three failure regimes separate cleanly and shift predictably with filter selectivity.
