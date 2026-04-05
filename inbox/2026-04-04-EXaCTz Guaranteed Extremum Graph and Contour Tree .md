---
interest: medium
link: https://arxiv.org/abs/2604.01397
next_step: skim
priority: medium
slack_ts: '1775359528.973929'
source: cs.DC - Distributed Computing
status: unread
title: 'EXaCTz: Guaranteed Extremum Graph and Contour Tree Preservation for Distributed-
  and GPU-Parallel Lossy Compression'
---
# EXaCTz: Guaranteed Extremum Graph and Contour Tree Preservation for Distributed- and GPU-Parallel Lossy Compression
> 原文: [https://arxiv.org/abs/2604.01397](https://arxiv.org/abs/2604.01397)

arXiv:2604.01397v1 Announce Type: new
Abstract: This paper introduces EXaCTz, a parallel algorithm that concurrently preserves extremum graphs and contour trees in lossy-compressed scalar field data. While error-bounded lossy compression is essential for large-scale scientific simulations and workflows, existing topology-preserving methods suffer from (1) a significant throughput disparity, where topology correction speeds are on the order of MB/s, lagging orders of magnitude behind compression speeds on the order of GB/s, (2) limited support for diverse topological descriptors, and (3) a lack of theoretical convergence bounds. To address these challenges, EXaCTz introduces a high-performance, bounded-iteration algorithm that enforces topological consistency by deriving targeted edits for decompressed data. Unlike prior methods that rely on explicit topology reconstruction, EXaCTz enforces consistent min/max neighbors of all vertices, along with global ordering among critical points. As such, the algorithm enforces consistent critical-point classification, saddle extremum connectivity, and the preservation of merge/split events. We theoretically prove the convergence of our algorithm, bounded by the longest path in a vulnerability graph that characterizes potential cascading effects during correction. Experiments on real-world datasets show that EXaCTz achieves a single-GPU throughput of up to 4.52 GB/s, outperforming the state-of-the-art contour-tree-preserving method (Gorski et al.) by up to 213x (with a single-core CPU implementation for fair comparison) and 3,285x (with a single-GPU version). In distributed environments, EXaCTz scales to 128 GPUs with 55.6\% efficiency (compared with 6.4\% for a naive parallelization), processing datasets of up to 512 GB in under 48 seconds and achieving an aggregate correction throughput of up to 32.69 GB/s.
