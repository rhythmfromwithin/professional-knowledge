---
interest: medium
link: https://arxiv.org/abs/2602.23999
next_step: skim
priority: low
slack_ts: '1773132413.223109'
source: cs.DB - Databases
status: unread
title: 'GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index
  Build and Search'
---
# GPU-Native Approximate Nearest Neighbor Search with IVF-RaBitQ: Fast Index Build and Search
> 原文: [https://arxiv.org/abs/2602.23999](https://arxiv.org/abs/2602.23999)

arXiv:2602.23999v1 Announce Type: new
Abstract: Approximate nearest neighbor search (ANNS) on GPUs is gaining increasing popularity for modern retrieval and recommendation workloads that operate over massive high-dimensional vectors. Graph-based indexes deliver high recall and throughput but incur heavy build-time and storage costs. In contrast, cluster-based methods build and scale efficiently yet often need many probes for high recall, straining memory bandwidth and compute. Aiming to simultaneously achieve fast index build, high-throughput search, high recall, and low storage requirement for GPUs, we present IVF-RaBitQ (GPU), a GPU-native ANNS solution that integrates the cluster-based method IVF with RaBitQ quantization into an efficient GPU index build/search pipeline. Specifically, for index build, we develop a scalable GPU-native RaBitQ quantization method that enables fast and accurate low-bit encoding at scale. For search, we develop GPU-native distance computation schemes for RaBitQ codes and a fused search kernel to achieve high throughput with high recall. With IVF-RaBitQ implemented and integrated into the NVIDIA cuVS Library, experiments on cuVS Bench across multiple datasets show that IVF-RaBitQ offers a strong performance frontier in recall, throughput, index build time, and storage footprint. For Recall approximately equal to 0.95, IVF-RaBitQ achieves 2.2x higher QPS than the state-of-the-art graph-based method CAGRA, while also constructing indices 7.7x faster on average. Compared to the cluster-based method IVF-PQ, IVF-RaBitQ delivers on average over 2.7x higher throughput while avoiding accessing the raw vectors for reranking.
