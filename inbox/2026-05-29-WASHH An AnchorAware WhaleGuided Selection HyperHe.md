---
interest: medium
link: https://arxiv.org/abs/2605.28844
next_step: skim
priority: low
slack_ts: '1780290089.406139'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'WASHH: An Anchor-Aware Whale-Guided Selection Hyper-Heuristic for Continuous
  Optimization and SVC Configuration'
---
# WASHH: An Anchor-Aware Whale-Guided Selection Hyper-Heuristic for Continuous Optimization and SVC Configuration
> 原文: [https://arxiv.org/abs/2605.28844](https://arxiv.org/abs/2605.28844)

arXiv:2605.28844v1 Announce Type: new
Abstract: Learning-assisted algorithm design often has to make reliable search decisions under small evaluation budgets, where committing to a single metaheuristic can be unreliable. We propose WASHH, a Whale-guided Adaptive Selection Hyper-Heuristic for continuous black-box optimization. WASHH uses WOA as the main exploitation backbone, but treats PSO-style memory, GWO-style leader averaging, DE-style variation, local coordinate search, and anchor-guided refinement as selectable search behaviors. An online reward controller allocates evaluations according to observed improvements, while anchor refinement exploits inexpensive reference configurations such as box centers or default model settings without bypassing black-box evaluation. On ten 30-dimensional benchmark functions with 10 independent runs and 12,000 evaluations, WASHH achieves the best average rank, 1.10, and is best or tied best on all ten functions. It strictly improves over WOA on eight functions and ties WOA at the numerical optimum on Rastrigin and Griewank. We further study SVC hyperparameter configuration for breast cancer diagnosis under a 300-evaluation budget. WASHH obtains the lowest mean validation log loss among the compared optimizers, suggesting that anchor-aware selection hyper-heuristics are a practical lightweight direction for LEAD systems.
