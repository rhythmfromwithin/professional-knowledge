---
interest: medium
link: https://arxiv.org/abs/2605.19119
next_step: skim
priority: low
slack_ts: '1779423485.946059'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'GOAL: Graph-based Objective-Aligned Diffusion Solvers for Dynamic Multi-Objective
  Optimization'
---
# GOAL: Graph-based Objective-Aligned Diffusion Solvers for Dynamic Multi-Objective Optimization
> 原文: [https://arxiv.org/abs/2605.19119](https://arxiv.org/abs/2605.19119)

arXiv:2605.19119v1 Announce Type: new
Abstract: Existing neural combinatorial optimization solvers frame solution search as imitation of optimal decisions, inherently limiting their utility to single-objective minimization and static constraints. We propose GOAL, a conditioned diffusion solver over relational graph representations that enables controllable decision generations by conditioning on human-specified objectives. We introduce a heterogeneous graph encoding in which distinct edge types, corresponding to different classes of constraints, define the message passing structure of the graph neural network, which allows information to propagate selectively according to the ontology of each constraint. GOAL is instantiated and evaluated on three canonical scheduling benchmarks of various constraint complexity: the Flow Shop Problem (FSP), the Job Shop Scheduling Problem (JSP), and the Flexible Job Shop Scheduling Problem (FJSP). Generalization is demonstrated across structurally distinct constraint regimes and problem types without architectural modification. On all three benchmarks, GOAL achieves 100% solution feasibility and near-zero MAPE (below 0.20%) on multiple objectives for problem sizes up to 20 jobs and 60 operations, outperforming NSGA-II and MOEA/D in both solution quality and inference speed by up to 25x.
