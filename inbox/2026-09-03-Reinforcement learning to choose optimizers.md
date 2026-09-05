---
interest: medium
link: https://arxiv.org/abs/2609.01811
next_step: skim
priority: low
slack_ts: '1788581037.851119'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Reinforcement learning to choose optimizers
---
# Reinforcement learning to choose optimizers
> 原文: [https://arxiv.org/abs/2609.01811](https://arxiv.org/abs/2609.01811)

arXiv:2609.01811v1 Announce Type: new
Abstract: No single optimization method is uniformly best for all problems, and the most suitable optimizer choice can change during a run. Existing approaches that change optimizer during execution typically predetermine part of the strategy: the portfolio is restricted to one algorithm class, the switch occurs once at a fixed time, or the frequency of decisions is treated as a hyperparameter rather than a learned one. We introduce "Reinforcement Learning to Choose Optimizers", which formulates the optimization algorithm choice as a sequential decision-making problem. At each decision, a recurrent policy reads the current run state and decides both which optimizer should be used next and for how long. The portfolio includes both gradient-based and derivative-free optimizers, and each switch passes on the current best solution and a representative step size. A context proxy conditions a gating network over expert heads, and training employs a decoupled actor-critic whose return is expressed in the same empirical runtime distribution metric used at evaluation. Training tasks and portfolio are designed jointly so that no optimizer dominates. On unseen problems, the learned policy outperforms every portfolio optimizer at all but the smallest budgets, and it remains robust under distribution shift.
