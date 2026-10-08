---
title: "RiftANN: Efficient Graph Traversal for Vector Search with RDMA-Based Memory Disaggregation"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.08990
priority: low
status: unread
interest: medium
next_step: skim
---
# RiftANN: Efficient Graph Traversal for Vector Search with RDMA-Based Memory Disaggregation
> 原文: [https://arxiv.org/abs/2610.08990](https://arxiv.org/abs/2610.08990)

arXiv:2610.08990v1 Announce Type: new
Abstract: Graph indexes for billion-scale vector collections can exceed a single server's DRAM capacity. Passive RDMA-based disaggregated memory provides scalable capacity without memory-node computation, but conventional best-first search performs poorly in this setting. Fine-grained and unnecessary remote reads increase communication cost, while dependencies between candidate evaluation and subsequent expansion serialize traversal and leave CPUs idle.
We present RiftANN, a graph-based approximate nearest neighbor search (ANNS) system for passive RDMA-based disaggregated memory. RiftANN navigates using compact vectors at compute nodes and selectively verifies exact vectors using a threshold calibrated from observed approximation errors. A bounded one-sided RDMA pipeline batches and overlaps the remaining remote accesses with local processing. RiftANN evaluates returned neighbors in parallel and incrementally incorporates completed results. An impact gate estimates whether unfinished evaluations may change the candidate set, allowing traversal to continue when their expected influence is small while preventing unsafe advancement from incomplete search state. A lightweight feedback controller coordinates RDMA concurrency with background evaluation capacity as search configurations and query loads change.
We evaluate RiftANN on SIFT, DEEP, and SPACEV at 100M scale and SIFT1B. At matched recall, RiftANN achieves 1.6x to 4.3x latency speedups and 1.1x to 2.2x higher throughput than DistVS, and 1.6x to 5.6x latency speedups over SSD-based DiskANN and PipeANN. These results show that passive disaggregated memory can support low-latency graph-based vector retrieval without query-time computation at memory nodes.
