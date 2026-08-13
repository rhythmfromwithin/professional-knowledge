---
interest: medium
link: https://arxiv.org/abs/2608.07971
next_step: skim
priority: medium
slack_ts: '1786588258.024769'
source: cs.DC - Distributed Computing
status: unread
title: 'ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU
  Clusters'
---
# ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters
> 原文: [https://arxiv.org/abs/2608.07971](https://arxiv.org/abs/2608.07971)

arXiv:2608.07971v1 Announce Type: new
Abstract: Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations. This leaves substantial GPU capacity underutilized: training jobs reserve entire devices despite periodic idle phases, while offline inference tasks over-provision GPUs despite bursty demand patterns. We present ElastiCo, an elastic co-location framework that enables training and inference workloads to safely share GPUs through three integrated mechanisms. First, Resource Shape Transformation exposes each job as a family of feasible resource-performance configurations. Second, Elastic Shadow Pricing decomposes the resulting multi-resource allocation problem into per-job configuration selection subproblems via dynamic per-resource shadow prices. Third, Interference-Aware Co-location uses a predictor trained on hardware-counter and task-level features to estimate pairwise performance degradation under GPU sharing. Implemented as native Kubernetes middleware requiring no user-code modifications, ElastiCo is evaluated on a 64-GPU testbed and through large-scale trace-driven simulations (up to 512 GPUs), reducing the average JCT by up to 2.94x, increasing the cluster throughput by 2.02x, and increasing the GPU utilization from approximately 25% to 46%.
