---
interest: medium
link: https://arxiv.org/abs/2608.13696
next_step: skim
priority: low
slack_ts: '1787103721.692809'
source: cs.DB - Databases
status: unread
title: 'Over the Memory Wall, Into the Instruction Wall: The New Bottleneck in GPU
  Data Processing'
---
# Over the Memory Wall, Into the Instruction Wall: The New Bottleneck in GPU Data Processing
> 原文: [https://arxiv.org/abs/2608.13696](https://arxiv.org/abs/2608.13696)

arXiv:2608.13696v1 Announce Type: new
Abstract: Datacenter GPUs have seen an order-of-magnitude increase in memory bandwidth with the adoption of newer generations of HBM. Meanwhile, GPU database systems are gaining traction, many building on cuDF, an open-source library of GPU relational operators. Previously, query performance was bound by memory bandwidth, but the increase in memory bandwidth has not resulted in a proportional speedup of cuDF kernels. To investigate why performance has not kept up, we built Valk, a performance analysis tool that combines data from multiple profilers. We profile cuDF running TPC-H in-memory on two extremes of hardware capability, the L4 and GH200 GPUs. The GH200 has 13.4$\times$ the memory bandwidth and 2.5$\times$ the instruction throughput of the L4, yet is only 5.2$\times$ faster in running TPC-H. Our analysis shows that when memory bandwidth is increased, kernels become compute bound. From our analysis, we make three recommendations to fully utilize the GPUs' potential for relational workloads when the memory wall is removed: kernels need to 1) make more efficient use of caches, and 2) increase occupancy and/or instruction level parallelism, and 3) execute fewer instructions per memory access.
