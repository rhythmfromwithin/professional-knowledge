---
title: "Scaling Worst-Case Optimal Datalog to GPUs"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.20073
priority: low
status: unread
interest: medium
next_step: skim
---
# Scaling Worst-Case Optimal Datalog to GPUs
> 原文: [https://arxiv.org/abs/2604.20073](https://arxiv.org/abs/2604.20073)

arXiv:2604.20073v2 Announce Type: new
Abstract: Datalog is a declarative logic-programming language used for complex analytic reasoning workloads such as program analysis and graph analytics. Datalog's popularity is due to its unique price-point, marrying logic-defined specification with the potential for massive data parallelism. While traditional engines are CPU-based, the memory-bound nature of Datalog has led to increasing interest in leveraging GPUs. These engines beat CPU-based engines by operationalizing iterated relational joins via SIMT-friendly join algorithms. Unfortunately, all existing GPU Datalog engines are built on binary joins, which are inadequate for the complex multi-way queries arising in production systems such as DOOP and ddisasm. For these queries, binary decomposition can incur the AGM bound asymptotic blowup in time and space, leading to OOM failures regardless of join order. Worst-Case Optimal Joins (WCOJ) avoid this blowup, but their attribute-at-a-time intersections map poorly to SIMT hardware under key skew, causing severe load imbalance across Streaming Multiprocessors (SMs). We present SRDatalog, the first GPU Datalog engine based on WCOJ. SRDatalog uses flat columnar storage and two-phase deterministic memory allocation to avoid the OOM failures of binary joins and the index-rebuild overheads of static WCOJ systems. To mitigate skew and hide hardware stalls, SRDatalog further employs root-level histogram-guided load balancing, structural helper-relation splitting, and stream-aligned rule multiplexing. On real-world program-analysis workloads, SRDatalog achieves geometric-mean speedups of 21x to 47x.
