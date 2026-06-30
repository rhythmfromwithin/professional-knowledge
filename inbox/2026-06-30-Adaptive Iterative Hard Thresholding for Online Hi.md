---
interest: medium
link: https://arxiv.org/abs/2606.28652
next_step: skim
priority: medium
slack_ts: '1782792819.778549'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Adaptive Iterative Hard Thresholding for Online High-dimensional Quantile Regression
---
# Adaptive Iterative Hard Thresholding for Online High-dimensional Quantile Regression
> 原文: [https://arxiv.org/abs/2606.28652](https://arxiv.org/abs/2606.28652)

arXiv:2606.28652v1 Announce Type: new
Abstract: Online high-dimensional regression requires algorithms that can update sequentially while preserving structural sparsity. We propose \textit{Adaptive Iterative Hard Thresholding (AIHT)}, an online sparse-regression framework that alternates stochastic subgradient updates with adaptively scheduled hard-thresholding steps. The key idea is to separate support discovery from local refinement: early in the learning process, AIHT delays thresholding so that weak but informative coordinates have time to accumulate signal, while later it increases the projection frequency to stabilize the sparse estimator and exploit local curvature. We develop the theory for high-dimensional online quantile regression, a challenging setting in which the loss is nonsmooth and the data may exhibit heterogeneity or heavy-tailed noise. Under restricted curvature and gradient-leakage conditions, AIHT remains in an inflated sparse cone, exhibits a two-phase convergence behavior, and attains logarithmic regret for the sliding-window objective. Simulations for online quantile regression, together with threshold-scheduling ablations, support the proposed mechanism and illustrate its advantage over standard online sparse-learning baselines.
