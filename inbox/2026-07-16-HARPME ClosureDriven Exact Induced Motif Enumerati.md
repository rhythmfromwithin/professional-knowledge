---
title: "HARP-ME: Closure-Driven Exact Induced Motif Enumeration on GPUs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.12074
priority: medium
status: unread
interest: medium
next_step: skim
---
# HARP-ME: Closure-Driven Exact Induced Motif Enumeration on GPUs
> 原文: [https://arxiv.org/abs/2607.12074](https://arxiv.org/abs/2607.12074)

arXiv:2607.12074v1 Announce Type: new
Abstract: Exact induced motif enumeration is a fundamental operation in graph mining, but it remains challenging on GPUs because candidate expansion is irregular, repeated set intersections dominate execution, and induced counting must consider both the presence and absence of edges. We present HARP-ME, which stands for Hierarchical Anchor-Reuse Partitioned Motif Enumeration. It is a GPU framework for the exact enumeration of connected induced four-node motifs. HARP-ME introduces closure-aware compilation, which selects a set of anchors for explicit enumeration by considering traversal cost, algebraic derivation benefits, expected state reuse, and the additional halo overhead caused by graph partitioning. HARP-ME also introduces induced-signature reuse. This technique identifies reusable completion states using candidate-frontier information together with compact constraints representing both adjacency and non-adjacency relationships. For graphs that exceed GPU memory, a canonical anchor-owner rule ensures exact counting across partitions with overlapping halo regions. We do not claim that the individual graphlet closure identities are new. Instead, our contribution is their integration into a GPU execution framework that reduces both explicit candidate expansion and repeated induced-edge checks. Across six social, web, biological, and synthetic graphs, HARP-ME is the fastest among the evaluated methods. It achieves up to 2.11 times speedup over Pangolin, up to 1.83 times speedup over partitioned PBE, and up to 10.73 times speedup over the evaluated CPU baseline. Detailed measurements show cache-hit rates between 64% and 76%, along with substantially lower host-to-device data transfer overhead than PBE-style partitioning. These results demonstrate that optimizing anchor selection for algebraic derivation benefits can complement traversal-based and reuse-based GPU motif enumeration techniques.
