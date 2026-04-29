---
interest: medium
link: https://arxiv.org/abs/2604.22171
next_step: skim
priority: low
slack_ts: '1777434579.683189'
source: cs.DB - Databases
status: unread
title: 'MCI: A Maximal Clique Index for Efficient Arbitrary-Filtered Approximate Nearest
  Neighbor Search'
---
# MCI: A Maximal Clique Index for Efficient Arbitrary-Filtered Approximate Nearest Neighbor Search
> 原文: [https://arxiv.org/abs/2604.22171](https://arxiv.org/abs/2604.22171)

arXiv:2604.22171v1 Announce Type: new
Abstract: Approximate Nearest Neighbor Search with arbitrary filtering predicates (AFANNS) is essential for modern data applications, yet existing methods often incur substantial storage and computational costs. In this work, we introduce the Maximal Clique Index (\mci), a novel graph-based index designed for robust and efficient AFANNS. The core idea of \mci is to approximate a dense Nearest Neighbor Graph (NNG) through a compact, clique-based representation. We propose two key techniques: (1) Maximal Clique Cover (\mcc), which exploits the geometric transitivity of high-dimensional spaces to encode dense neighborhoods as maximal cliques, achieving an index with high compression and connectivity; and (2) Local Neighborhood Graph Geometric Densification, a strategy that constructs an index approximating a large NNG from a sparse initial NNG, recovers global connectivity by progressively increasing distance thresholds to locally densify the structure. The index is built in a lock-free parallel manner for scalability and queried via a carefully-designed multi-seed strategy to handle fragmented predicate-induced subgraphs. Extensive experiments on 10 datasets show that \mci significantly outperforms state-of-the-art methods by up to one order of magnitude in QPS at high recall while using substantially smaller space, and remains competitive even on range/keyword filtering tasks, demonstrating robust general-purpose performance.
