---
interest: medium
link: https://arxiv.org/abs/2609.38194
next_step: skim
priority: high
slack_ts: '1790918087.870279'
source: cs.LG - Machine Learning
status: unread
title: A Moving-Horizon Approximate Branch-and-Reduce Method for Deep Classification
  Trees
---
# A Moving-Horizon Approximate Branch-and-Reduce Method for Deep Classification Trees
> 原文: [https://arxiv.org/abs/2609.38194](https://arxiv.org/abs/2609.38194)

arXiv:2609.38194v1 Announce Type: new
Abstract: Despite the importance for interpretability, decision trees face severe scalability challenges. Existing global optimal methods are often limited by binary feature selection and shallow tree depths, whereas traditional heuristic approaches frequently sacrifice predictive accuracy. To overcome these limitations, this paper proposes a moving-horizon approximate branch-and-reduce method to train near-optimal deep classification trees on large-scale datasets with continuous features. Built on a hierarchical root-subtree optimization framework, the method solves the root-level problem via branch-and-reduce while approximating the induced subtree problem using greedy heuristics. Although the underlying framework is capable of guaranteeing global optimality, the approximation, which functions as a lookahead rollout in a reinforcement learning context, significantly boosts efficiency for deeper structures. A low-cost moving-horizon strategy is then employed to iteratively refine model accuracy. Extensive numerical results demonstrate that our method exceeds the testing accuracy of existing heuristic baselines while offering significantly greater scalability, in terms of both dataset size and tree depth, than global optimal solvers.
