---
interest: medium
link: https://arxiv.org/abs/2606.00002
next_step: skim
priority: high
slack_ts: '1780548657.516059'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Position Paper: Post-Solve Robustness in Decision Engines: Feasible Regions
  and Smoothness Under Perturbations'
---
# Position Paper: Post-Solve Robustness in Decision Engines: Feasible Regions and Smoothness Under Perturbations
> 原文: [https://arxiv.org/abs/2606.00002](https://arxiv.org/abs/2606.00002)

arXiv:2606.00002v1 Announce Type: new
Abstract: Mixed-Integer Linear Programming (MILP) decision engines routinely output nominally optimal plans for high-stakes industrial systems. Yet deployment rarely matches solve-time assumptions: small perturbations in costs, demands, or resource availability can invalidate feasibility or trigger discontinuous shifts to qualitatively different solutions. We argue that this post-solve robustness gap is a missing layer in today's optimization pipelines and a missing evaluation dimension for learning-enabled decision systems. Rather than replacing robust optimization or stochastic programming, the proposed layer audits a solved incumbent and returns solver-backed evidence about how far that solution can be trusted. We formalize two central objects: (i) an $\epsilon$-near-optimal feasible neighborhood in parameter space, capturing when an incumbent remains feasible and near-optimal under perturbations, and (ii) solution smoothness in decision space, capturing whether nearby alternatives with small combinatorial edits remain competitive. We then synthesize the most relevant partial answers from sensitivity and stability analysis, robust optimization, neighborhood search, adversarial testing, and learning-based enhancements, and articulate an agenda for a unified post-solve robustness layer. Concretely, we call for certified inner approximations around the incumbent, probabilistic robustness estimation with calibrated uncertainty, adversarial robustness margins, and learning-based prediction and explanation aligned with solver-backed verification. We conclude with a compact reporting template and evaluation protocol that would make robustness a first-class output of decision engines.
