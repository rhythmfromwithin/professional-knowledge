---
interest: medium
link: https://arxiv.org/abs/2603.19431
next_step: skim
priority: medium
slack_ts: '1774581537.788369'
source: cs.DC - Distributed Computing
status: unread
title: 'SWARM+: Scalable and Resilient Multi-Agent Consensus for Fully-Decentralized
  Data-Aware Workload Management'
---
# SWARM+: Scalable and Resilient Multi-Agent Consensus for Fully-Decentralized Data-Aware Workload Management
> 原文: [https://arxiv.org/abs/2603.19431](https://arxiv.org/abs/2603.19431)

arXiv:2603.19431v1 Announce Type: new
Abstract: Distributed scientific workflows increasingly span heterogeneous compute clusters, edge resources, and geo-distributed data repositories. In these environments, a centralized orchestrator is an architectural bottleneck -- introducing a single point of failure, limiting scalability, and constraining adaptability to changing resource availability or failures. Decentralized multi-agent coordination offers a compelling alternative: autonomous agents representing distributed resources collaboratively negotiate workload assignment (e.g., job selection) through peer-to-peer consensus, making decisions based on local compute capacity, data locality, and network conditions. However, scaling such systems for production workloads requires addressing challenges in coordination, resilience, and data-aware optimization. This work presents SWARM+, which builds on our prior work that demonstrated the feasibility of multi-agent decentralized consensus for distributed job selection. SWARM+ addresses three main problems: scalability of consensus for large numbers of agents, resilience of workload management under agent failure, and efficiency of job scheduling for highly distributed resources and data-intensive workloads. For each problem, we propose novel algorithms and evaluate them in the distributed FABRIC testbed. The results show that SWARM+ (a) scales to 1000 distributed agents with nearly equal workload distribution across the hierarchy levels and reduced coordination overhead due to hierarchical consensus, (b) is resilient to agent failures, maintaining >99% job completion rate under single agent failure, and demonstrating graceful system degradation, with at most 7.5% impact under 50% agent failures, and (c) achieves 97-98% improvement over baseline SWARM for both selection time and scheduling latency metrics.
