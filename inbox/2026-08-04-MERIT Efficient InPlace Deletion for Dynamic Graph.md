---
interest: medium
link: https://arxiv.org/abs/2607.29173
next_step: skim
priority: low
slack_ts: '1785986402.713769'
source: cs.DB - Databases
status: unread
title: 'MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest
  Neighbor Indexes'
---
# MERIT: Efficient In-Place Deletion for Dynamic Graph-Based Approximate Nearest Neighbor Indexes
> 原文: [https://arxiv.org/abs/2607.29173](https://arxiv.org/abs/2607.29173)

arXiv:2607.29173v1 Announce Type: new
Abstract: Graph-based indexes have become the dominant approach to approximate nearest neighbor search (ANNS) over high-dimensional data and play a crucial role in real-world applications such as retrieval-augmented generation, recommendation systems, and vector databases. Despite extensive progress in static graph construction and search, efficient in-place deletion remains challenging because obsolete vectors must be removed without allowing stale incoming edges to consume search capacity or expensive graph-wide maintenance to interrupt online services, e.g., retrieval-augmented generation (RAG) and recommendation platforms. To address this problem, we propose MERIT (MST-based Efficient Repair with In-place updaTes), an in-place update framework with three core techniques: (1) bounded search-based recovery that combines a deleted vertex's outgoing neighbors with its readily searchable in-neighbors, (2) $k\_r$-Minimum Spanning Tree (MST) local repair that promotes local connectivity while retaining multiple routing choices for graph search, and (3) versioned-edge invalidation that immediately filters all stale incoming edges to the deleted vertex and progressively removes them as adjacency lists are rewritten. Its integration with the hierarchical HNSW index and the single-layer Vamana index demonstrates applicability across distinct graph structures. Extensive experiments on multiple real-world datasets show that MERIT processes deletion at nearly the cost of inserting one vector, achieves up to $3.02\times$--$18.87\times$ faster deletion than state-of-the-art (SOTA) methods, and keeps search recall stable or even improves it as deletions accumulate.
