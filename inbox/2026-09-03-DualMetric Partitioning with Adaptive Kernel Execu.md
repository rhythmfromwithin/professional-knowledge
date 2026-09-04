---
interest: medium
link: https://arxiv.org/abs/2609.01983
next_step: skim
priority: low
slack_ts: '1788494853.647029'
source: cs.DB - Databases
status: unread
title: Dual-Metric Partitioning with Adaptive Kernel Execution for Efficient GCN Acceleration
---
# Dual-Metric Partitioning with Adaptive Kernel Execution for Efficient GCN Acceleration
> 原文: [https://arxiv.org/abs/2609.01983](https://arxiv.org/abs/2609.01983)

arXiv:2609.01983v1 Announce Type: new
Abstract: Graph Convolutional Networks (GCNs) are widely used for large graph-structured data, including social, citation, and e-commerce networks, but their deployment is constrained by irregular memory access and severe GPU workload imbalance. These challenges arise in two dimensions: width imbalance from power-law degree distributions and depth imbalance from heterogeneous neighborhood connectivity.We present DualGCN, a GPU acceleration framework addressing both dimensions through dual-metric graph partitioning and adaptive kernel execution. DualGCN combines node degree, reflecting aggregation width, with neighborhood density estimated by anonymous random walks, capturing multihop connectivity and access depth. This hybrid workload metric enables connectivity-aware partitioning of large graphs into sparse and dense regions while reducing workload imbalance from linear to logarithmic complexity. DualGCN then selects partition-specific execution strategies: sparse partitions use warp-level parallelism and coalesced memory access, whereas dense partitions exploit instruction-level parallelism to hide latency and improve GPU utilization. Experiments on twelve real-world graph datasets show that DualGCN consistently accelerates GCN computation, achieving average speedups of 2.53x, 3.8x, and 2.13x over cuSPARSE, GNNAdvisor, and ACCEL, respectively. These results demonstrate that jointly optimizing graph partitioning and kernel execution provides an effective solution for processing large-scale graph and socialnetwork workloads.
