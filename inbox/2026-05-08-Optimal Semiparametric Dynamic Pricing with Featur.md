---
title: "Optimal Semiparametric Dynamic Pricing with Feature Diversity"
source: "econ.GN - General Economics (AI Economics)"
link: https://arxiv.org/abs/2605.04207
priority: low
status: unread
interest: medium
next_step: skim
---
# Optimal Semiparametric Dynamic Pricing with Feature Diversity
> 原文: [https://arxiv.org/abs/2605.04207](https://arxiv.org/abs/2605.04207)

arXiv:2605.04207v1 Announce Type: cross
Abstract: We study contextual dynamic pricing under a semiparametric demand model in which the purchase probability is $1-F(p-m(\mathbf{x}))$, where $m(\mathbf{x})$ captures mean utility as a function of product features and buyer covariates, and $F$ is an unknown market-noise distribution. Existing methods either incur suboptimal regret or rely on restrictive structural assumptions. We propose a stagewise greedy pricing algorithm that iteratively refines the estimate of $F$ via local polynomial regression while pricing greedily with current estimates. By exploiting feature diversity, the algorithm reuses endogenous samples collected during exploitation for nonparametric estimation, avoiding costly global random exploration used in prior work.
We establish a general regret bound that applies to any estimator $\hat m$ of the utility function, and derive explicit rates for linear, nonparametric additive, and sparse linear classes of $m$. For the linear class, our regret scales as $T^{\max\{1/2,\,3/(2\beta+1)\}}$, where $\beta$ is the smoothness of $F$ and $T$ is the time horizon. This improves the best known rates for semiparametric contextual pricing and achieves the parametric $\sqrt{T}$ rate when $\beta \ge 5/2$. We further prove a matching lower bound, showing the optimality of our rate, and present numerical experiments that corroborate the theory and demonstrate the practical advantages of iterative refinement.
