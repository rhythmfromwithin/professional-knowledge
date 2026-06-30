---
interest: medium
link: https://arxiv.org/abs/2606.29151
next_step: skim
priority: low
slack_ts: '1782792820.711309'
source: cs.DB - Databases
status: unread
title: 'CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs
  for Semantic Query Processing'
---
# CADENZA: Compiling Natural-Language Intent into Task-Specific Operator DAGs for Semantic Query Processing
> 原文: [https://arxiv.org/abs/2606.29151](https://arxiv.org/abs/2606.29151)

arXiv:2606.29151v1 Announce Type: new
Abstract: Semantic query processing engines (SQPEs) extend relational query processing with semantic operators that are executed via model inference over unstructured data. Optimizing such queries is inherently multi-objective: model inference dominates latency and monetary cost, and outputs are stochastic and backend-dependent, so quality must be optimized alongside efficiency. Existing SQPE optimizers do not expose each semantic operator instance's intermediate task outputs as a relational optimization object, leaving optimization unable to filter, reorder, route, threshold, or jointly tune them. We present CADENZA, which compiles each semantic operator instance--a template bound to a natural-language intent--into an intent-specific plan space of typed task DAGs and selects an executable plan under user-specified quality-latency-cost trade-offs. CADENZA introduces task-extended relational algebra (TxRA), a conservative extension of relational algebra with task-specific operators. The logical planner synthesizes seed TxRA plans, applies structural rewrites whose safety conditions are checked from operator dependencies, and enumerates semantics-guided alternatives from alternative-generation templates. The physical planner compiles each task-specific operator into a router over heterogeneous backends and jointly tunes routing cutpoints, backend parameters, and relational thresholds with Bayesian optimization. On SemBench, CADENZA improves the scenario-level averages of quality, latency, and cost by up to +0.49, 165.7x, and 310.3x, respectively, relative to state-of-the-art.
