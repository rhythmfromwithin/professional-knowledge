---
interest: medium
link: https://arxiv.org/abs/2606.13954
next_step: skim
priority: medium
slack_ts: '1781500245.283719'
source: cs.DC - Distributed Computing
status: unread
title: Lattice Aggregation in Distributed Verification under Crash and Byzantine Failures
---
# Lattice Aggregation in Distributed Verification under Crash and Byzantine Failures
> 原文: [https://arxiv.org/abs/2606.13954](https://arxiv.org/abs/2606.13954)

arXiv:2606.13954v1 Announce Type: new
Abstract: We introduce c-Lattice Aggregation, a fault-tolerant reconstruction problem for distributed verification under crash and Byzantine failures. In our setting, n asynchronous processes supervise a concurrent execution I: each process holds a local sample, and must collaboratively reconstruct I from partial, potentially overlapping observations. A protocol solves c-Lattice Aggregation if at least c correct processes output the complete execution I, while all correct outputs are comparable and bounded by I. This strengthens Lattice Agreement [Attiya, Herlihy and Rachman, 1995] and Byzantine Lattice Agreement [Di Luna et al., 2020; Zheng and Garg, 2020].
We parameterize inputs by a redundancy parameter x -- every element of I appears in at least x initial samples -- and establish tight feasibility thresholds. Under crash failures with at most t faulty processes, Lattice Aggregation is solvable if and only if x >= t + 1. Under Byzantine failures with t < n/3, c-Lattice Aggregation is solvable if and only if x >= 2t + c. All bounds are tight: we present matching algorithms based on SCD-broadcast [Imbs et al., 2018; Khanchandani and Wattenhofer, 2024] and indistinguishability-based lower bounds.
Finally, we define globally dependent languages -- those for which no partial view can certify correctness, including consensus, linearizability, k-set agreement, and leader election -- and prove that soundness of any monitoring system is achievable if and only if c-Lattice Aggregation is solved, yielding the first complete characterization of fault-tolerant verification under Byzantine failures.
