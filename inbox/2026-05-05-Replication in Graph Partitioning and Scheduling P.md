---
interest: medium
link: https://arxiv.org/abs/2605.00209
next_step: skim
priority: medium
slack_ts: '1778039481.515869'
source: cs.DC - Distributed Computing
status: unread
title: Replication in Graph Partitioning and Scheduling Problems
---
# Replication in Graph Partitioning and Scheduling Problems
> 原文: [https://arxiv.org/abs/2605.00209](https://arxiv.org/abs/2605.00209)

arXiv:2605.00209v1 Announce Type: new
Abstract: The efficient parallel execution of complex computations requires balancing the workload across processors while minimizing the communication between them. This inherent trade-off is often captured by graph partitioning or DAG scheduling problems. For the sake of model simplicity, most works on these problems assume that nodes can be assigned to only a single processor. However, in reality, replicating an operation on several processors can easily be beneficial: it may increase the computational costs only by a small amount, while significantly reducing the communication requirements.
Our goal is to provide a comprehensive analysis of the impact of replication on partitioning and scheduling problems. On the theoretical side, we show that for graph partitioning, replication makes the problem significantly harder in terms of approximation complexity, whereas for scheduling, its impact on complexity seems less prominent. On the experimental side, we conduct a thorough analysis of the cost reduction obtainable by replication, on a wide range of graphs from real-world applications. For hypergraph partitioning, we use Integer Linear Programming (ILP) formulations to compare the optimal costs; our experiments show that replication can reduce the cost by 17%-65% on average, or even entirely remove the need for communication in some cases. For DAG scheduling, we similarly use ILPs on smaller graphs, and develop a sophisticated heuristic that is also applicable to much larger workloads. Our experiments here demonstrate a mean cost reduction of 11.61%-23.13% with replication, or even up to 58.17% in some cases.
