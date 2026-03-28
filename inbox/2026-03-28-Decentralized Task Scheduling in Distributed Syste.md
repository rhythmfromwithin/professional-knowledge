---
interest: medium
link: https://arxiv.org/abs/2603.24738
next_step: skim
priority: medium
slack_ts: '1774666228.881379'
source: cs.DC - Distributed Computing
status: unread
title: 'Decentralized Task Scheduling in Distributed Systems: A Deep Reinforcement
  Learning Approach'
---
# Decentralized Task Scheduling in Distributed Systems: A Deep Reinforcement Learning Approach
> 原文: [https://arxiv.org/abs/2603.24738](https://arxiv.org/abs/2603.24738)

arXiv:2603.24738v1 Announce Type: new
Abstract: Efficient task scheduling in large-scale distributed systems presents significant challenges due to dynamic workloads, heterogeneous resources, and competing quality-of-service requirements. Traditional centralized approaches face scalability limitations and single points of failure, while classical heuristics lack adaptability to changing conditions. This paper proposes a decentralized multi-agent deep reinforcement learning (DRL-MADRL) framework for task scheduling in heterogeneous distributed systems. We formulate the problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) and develop a lightweight actor-critic architecture implemented using only NumPy, enabling deployment on resource-constrained edge devices without heavyweight machine learning frameworks. Using workload characteristics derived from the publicly available Google Cluster Trace dataset, we evaluate our approach on a 100-node heterogeneous system processing 1,000 tasks per episode over 30 experimental runs. Experimental results demonstrate 15.6% improvement in average task completion time (30.8s vs 36.5s for random baseline), 15.2% energy efficiency gain (745.2 kWh vs 878.3 kWh), and 82.3% SLA satisfaction compared to 75.5% for baselines, with all improvements statistically significant (p < 0.001). The lightweight implementation requires only NumPy, Matplotlib, and SciPy. Complete source code and experimental data are provided for full reproducibility at https://github.com/danielbenniah/marl-distributed-scheduling.
