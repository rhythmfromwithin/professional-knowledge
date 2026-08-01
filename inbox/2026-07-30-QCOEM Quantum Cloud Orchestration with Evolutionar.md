---
interest: medium
link: https://arxiv.org/abs/2607.25358
next_step: skim
priority: medium
slack_ts: '1785555370.055549'
source: cs.DC - Distributed Computing
status: unread
title: 'QCOEM: Quantum Cloud Orchestration with Evolutionary Multi-Objective Optimization'
---
# QCOEM: Quantum Cloud Orchestration with Evolutionary Multi-Objective Optimization
> 原文: [https://arxiv.org/abs/2607.25358](https://arxiv.org/abs/2607.25358)

arXiv:2607.25358v1 Announce Type: new
Abstract: Quantum cloud platforms need to dynamically orchestrate workloads across heterogeneous quantum computation backends whose noise profiles, qubit topologies, and queues vary over time. Existing orchestrators use noise-agnostic heuristics that ignore backend-specific errors, causing reduced execution fidelity, load imbalance, and frequent rescheduling. To address these challenges, we propose QCOEM - a Quantum Cloud Orchestration framework that leverages Evolutionary algorithms for Multi-objective optimization of quantum task scheduling. We compare NSGA-II and NSGA-III for jointly minimizing mean completion time, execution error rate, and load imbalance. To select schedules from a non-convex Pareto front, we apply an Augmented Achievement Scalarization Function (AASF) as a preference-based decision rule that maps the Pareto set to a single dispatchable schedule aligned with user priorities. Our extensive performance evaluation in a heterogeneous quantum cloud environment shows zero task rescheduling and about 30% higher mean fidelity than noise-agnostic heuristics, while maintaining bounded scheduling overhead. The experiment results indicate that our QCOEM framework can deliver stable, high-fidelity execution and lightweight resource management for quantum cloud computing.
