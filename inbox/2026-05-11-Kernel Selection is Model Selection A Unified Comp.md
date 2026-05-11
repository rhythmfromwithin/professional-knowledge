---
interest: medium
link: https://arxiv.org/abs/2605.06883
next_step: skim
priority: medium
slack_ts: '1778472627.313779'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Kernel Selection is Model Selection: A Unified Complexity-Penalized Approach
  for MMD Two-Sample Tests'
---
# Kernel Selection is Model Selection: A Unified Complexity-Penalized Approach for MMD Two-Sample Tests
> 原文: [https://arxiv.org/abs/2605.06883](https://arxiv.org/abs/2605.06883)

arXiv:2605.06883v1 Announce Type: new
Abstract: The Maximum Mean Discrepancy (MMD) is a cornerstone statistic for nonparametric two-sample testing, but its test power is dictated entirely by the chosen kernel. Because any fixed kernel inherently fails to distinguish certain distributions, the kernel must be dynamically optimized. However, data-driven optimization violates the foundational i.i.d. assumption, forcing a strict trade-off in existing frameworks. Ratio criteria ignore this dependence, inducing overfitting and variance collapse on rich kernel classes. Conversely, aggregation methods bypass the dependence using finite grids, but this strategy cannot scale to continuous search spaces like deep kernels.
To break this dichotomy, we establish data-driven kernel selection as a model selection problem. We propose Complexity-Penalized MMD (CP-MMD), a criterion derived by applying the two-sample uniform concentration inequality of preceding works to the post-optimization MMD problem. The resulting penalty bounds the empirical MMD by the complexity of the kernel search space, mathematically absorbing the cost of optimization, so that CP-MMD enables direct, grid-free maximization over continuous parametric classes, including scalar bandwidths, polynomial feature bandwidths, and deep network parameters. By formally accounting for optimization complexity, we prove that CP-MMD maximizes true test power while ensuring unconditional Type-I validity. Consequently, CP-MMD enables grid-free kernel selection across linear, polynomial-feature, and deep regimes, matching or exceeding state-of-the-art test power.
