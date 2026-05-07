---
title: "Dynamic Vine Copulas: Detecting and Quantifying Time-Varying Higher-Order Interactions"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.03061
priority: medium
status: unread
interest: medium
next_step: skim
---
# Dynamic Vine Copulas: Detecting and Quantifying Time-Varying Higher-Order Interactions
> 原文: [https://arxiv.org/abs/2605.03061](https://arxiv.org/abs/2605.03061)

arXiv:2605.03061v1 Announce Type: new
Abstract: Time varying dependence is often modeled through dynamic correlations or Gaussian graphical models, yet many multivariate systems change through tail behavior, asymmetry, or conditional structure while correlations change little. We introduce Dynamic Vine Copulas (DVC), a temporal vine copula framework for estimating and diagnosing sequence wide non-Gaussian dependence. DVC keeps a chosen vine factorization fixed for comparability, can use C-, D-, or R-vines, and couples pair copula states across time through smooth parameter trajectories or temporally regularized family switching paths. Its central diagnostic contrasts held-out scores from a full vine and its matched 1-truncated counterpart, separating flexible first-tree pairwise evidence from higher-tree conditional evidence. At the population level, under a correct fixed vine and simplifying assumption, this contrast is the higher-tree term of a vine total correlation decomposition; in finite samples, it is a predictive diagnostic. Across controlled benchmarks, DVC detects Student-t tail degree changes, Clayton-to-Gumbel switches, and recurrent conditional interaction episodes that Gaussian dynamic baselines miss or conflate. The higher-tree score stays near zero in pairwise only regimes but rises selectively during conditional interaction regimes. On Allen Visual Behavior Neuropixels data, DVC identifies a reproducible time indexed higher-tree signal that is positive across held-out splits and disappears under a decorrelated null, indicating simultaneous cross-area dependence. Together, these results show that DVC is both a flexible temporal copula model and an interpretable diagnostic for whether time varying dependence changes are pairwise or conditional.
