---
interest: medium
link: https://arxiv.org/abs/2608.22185
next_step: skim
priority: low
slack_ts: '1787820609.394149'
source: cs.DB - Databases
status: unread
title: Residual Privacy Budgeting with Weighted Scarcity Allocation for Online Query
  Answering
---
# Residual Privacy Budgeting with Weighted Scarcity Allocation for Online Query Answering
> 原文: [https://arxiv.org/abs/2608.22185](https://arxiv.org/abs/2608.22185)

arXiv:2608.22185v1 Announce Type: new
Abstract: In many practical deployments of differential privacy, queries do not arrive all at once. We study online differentially private query answering under a finite zero-concentrated differential privacy (zCDP) contract. In this setting, queries arrive sequentially, carry different accuracy thresholds, and may overlap with information already released. We formulate this setting as residual privacy budgeting: for each arriving query, the mechanism first credits reusable support from previous DP outputs and then spends new budget only on the remaining support required to satisfy the current threshold. The controller separates feasible cases, where the minimal residual support is allocated exactly, from scarcity cases, where a weighted shortfall-conservation optimiser assigns limited support according to query difficulty. We define the weight using the Query Influence Factor (QIF), a diagnostic signal for query difficulty and instability rather than query importance. For scalar Gaussian exact reuse, inverse-variance fusion justifies additive support. We prove zCDP composition, residual minimality, 1-competitiveness against the offline optimum in the feasible regime, and avoidable expenditure for allocators that ignore released history. A scarcity impossibility result shows that no online allocator can guarantee a competitive ratio better than 1/n in threshold satisfaction, contextualising the QIF scarcity layer as a design choice for an inherently hard online problem.
