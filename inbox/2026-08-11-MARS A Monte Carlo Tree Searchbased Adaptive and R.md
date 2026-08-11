---
title: "MARS: A Monte Carlo Tree Search-based Adaptive and Responsive Scheduler"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.06629
priority: medium
status: unread
interest: medium
next_step: skim
---
# MARS: A Monte Carlo Tree Search-based Adaptive and Responsive Scheduler
> 原文: [https://arxiv.org/abs/2608.06629](https://arxiv.org/abs/2608.06629)

arXiv:2608.06629v1 Announce Type: new
Abstract: Modern High Performance Computing systems depend on static heuristics and manual administration for job scheduling and reservation management. Deep Reinforcement Learning (DRL) has shown promising scheduling performance but requires historical training data and fixes the optimization goal at training time, forcing operators to retrain whenever priorities shift. We introduce MARS (Monte Carlo Tree Search-based Adaptive and Responsive Scheduler), a training-free HPC scheduler whose optimization goal is configurable through a reward function rather than baked into a learned model. MARS uses a lightweight discrete-event simulator to explore the future consequences of scheduling decisions within a strict time budget, adapting to the configured reward at each scheduling cycle. We evaluate MARS on year-long production workloads from two systems at Argonne Leadership Computing Facility -- 4,360-node Theta and 560-node Polaris---under two reward functions: wait-time minimization (MARS-CW) and utilization maximization (MARS-CU). Unlike DRL and heuristics, which only react to the current queue or wait for backfill to find holes, MARS exploits look-ahead to proactively drain the system and plan around future reservations, packing the system to avoid the fragmentation and utilization drop that typically precede reservation windows. MARS-CW reduces tail wait time by 64% on Theta and 43% on Polaris over the production WFP heuristic, while MARS-CU recovers utilization in the 48 hours leading into maintenance, demonstrating that MARS can target either objective via reward reconfiguration.
