---
interest: medium
link: https://arxiv.org/abs/2604.14445
next_step: skim
priority: low
slack_ts: '1776482314.695629'
source: cs.DB - Databases
status: unread
title: Parallel R-tree-based Spatial Query Processing on a Commercial Processing-in-Memory
  System
---
# Parallel R-tree-based Spatial Query Processing on a Commercial Processing-in-Memory System
> 原文: [https://arxiv.org/abs/2604.14445](https://arxiv.org/abs/2604.14445)

arXiv:2604.14445v1 Announce Type: new
Abstract: The growing volume of data in scientific domains has made spatial query processing increasingly challenging due to high data transfer costs across the memory hierarchy and limited memory bandwidth. To address these bottlenecks and reduce the energy consumed on data movement, this work explores Processing-in-Memory (PIM) systems by executing range queries directly inside memory chips. Unlike prior PIM studies centered on linear scans or hash-based queries, this work is the first to map R-tree range queries onto commercial PIM hardware. The proposed broadcast-based method constructs the R-tree bottom-up on the CPU, broadcasts top levels to UPMEM DPUs (DRAM Processing Units) for global filtering, and distributes lower levels for parallel batched queries in a CPU-DPU system. We evaluate our approach on two real spatial datasets, Sports (999K rectangles) and Lakes (8.4M rectangles), and assess scalability using a synthetic dataset with up to 16M rectangles and 3.9M queries on a commercial UPMEM PIM system with up to 2,540 DPUs. Across all datasets, broadcast-based execution consistently outperforms subtree partitioning by preventing communication from dominating execution. On the Lakes dataset, strong scaling from 512 to 2,540 DPUs reduces kernel time from 64.9 s to 17.6 s, yielding up to 3.66x kernel and 2.70x end-to-end speedup relative to the CPU R-tree search on the same system. The PIM kernel also consumes approximately 3.4x less energy than the corresponding CPU search (e.g., 59.6 kJ vs. 167.0 kJ on Lakes), demonstrating scalable and energy-efficient hierarchical spatial range queries.
