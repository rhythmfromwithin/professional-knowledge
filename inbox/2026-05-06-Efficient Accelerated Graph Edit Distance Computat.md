---
interest: medium
link: https://arxiv.org/abs/2605.00830
next_step: skim
priority: medium
slack_ts: '1778125801.462419'
source: cs.DC - Distributed Computing
status: unread
title: Efficient Accelerated Graph Edit Distance Computation on GPU
---
# Efficient Accelerated Graph Edit Distance Computation on GPU
> 原文: [https://arxiv.org/abs/2605.00830](https://arxiv.org/abs/2605.00830)

arXiv:2605.00830v1 Announce Type: new
Abstract: Graph representation is a powerful abstraction of real-world objects and relations. Computing the Graph Edit Distance (GED) between graphs is critical in domains such as bioinformatics, machine learning, and pattern recognition. GED measures the minimum number of edit operations required to transform one graph into another. However, the high computational complexity of optimal and near-optimal methods limits their applicability to large-scale graphs, making high-performance parallel GED computation essential. To address this, we propose FAST-GED, a fast and scalable open-source framework for GED computation on GPUs. FAST-GED overcomes existing limitations by combining high accuracy with fast execution through GPU-friendly algorithmic design and efficient mapping to GPU hardware, minimizing host-device communication. The implementation is optimized and tested across multiple GPU architectures. We validate FAST-GED on real and synthetic datasets with diverse graph sizes and densities. It achieves speedups of several orders of magnitude over the Python NetworkX library while reaching optimal solutions in most cases. Moreover, it outperforms state-of-the-art approximate methods in both accuracy and scalability. We show that FAST-GED enables broader adoption of GED-based solutions in real-world applications.
