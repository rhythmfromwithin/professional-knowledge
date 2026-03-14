---
title: "Beyond BFS: A Comparative Study of Rooted Spanning Tree Algorithms on GPUs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.11645
priority: medium
status: unread
interest: medium
next_step: skim
---
# Beyond BFS: A Comparative Study of Rooted Spanning Tree Algorithms on GPUs
> 原文: [https://arxiv.org/abs/2603.11645](https://arxiv.org/abs/2603.11645)

arXiv:2603.11645v1 Announce Type: new
Abstract: Rooted spanning trees (RSTs) are a core primitive in parallel graph analytics, underpinning algorithms such as biconnected components and planarity testing. On GPUs, RST construction has traditionally relied on breadth-first search (BFS) due to its simplicity and work efficiency. However, BFS incurs an O(D) step complexity, which severely limits parallelism on high-diameter and power-law graphs. We present a comparative study of alternative RST construction strategies on modern GPUs. We introduce a GPU adaptation of the Path Reversal RST (PR-RST) algorithm, optimizing its pointer-jumping and broadcast operations for modern GPU architecture. In addition, we evaluate an integrated approach that combines a state-of-the-art connectivity framework (GConn) with Eulerian tour-based rooting. Across more than 10 real-world graphs, our results show that the GConn-based approach achieves up to 300x speedup over optimized BFS on high-diameter graphs. These findings indicate that the O(log n) step complexity of connectivity-based methods can outweigh their structural overhead on modern hardware, motivating a rethinking of RST construction in GPU graph analytics.
