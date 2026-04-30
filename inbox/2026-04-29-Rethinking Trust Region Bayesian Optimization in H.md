---
interest: medium
link: https://arxiv.org/abs/2604.22967
next_step: skim
priority: medium
slack_ts: '1777521053.051159'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Rethinking Trust Region Bayesian Optimization in High Dimensions
---
# Rethinking Trust Region Bayesian Optimization in High Dimensions
> 原文: [https://arxiv.org/abs/2604.22967](https://arxiv.org/abs/2604.22967)

arXiv:2604.22967v1 Announce Type: new
Abstract: Trust Region Bayesian Optimization (TuRBO) is an effective strategy for alleviating the curse of dimensionality in high-dimensional black-box optimization. However, inappropriate lengthscale design can cause the local Gaussian process (GP) model within the trust region to degenerate, leading to suboptimal performance in high dimensions. In this work, we show that TuRBO's local GP may remain either excessively complex or overly simple as the dimension $D$ and trust region side length $L$ vary. To address this issue, we propose a straightforward variant, AdaScale-TuRBO, which scales the GP lengthscale with both the problem dimension and trust region size, thereby preserving kernel geometry and maintaining consistent prior complexity. Empirically, we show that AdaScale-TuRBO can robustly outperform standard TuRBO and other popular high-dimensional BO methods on synthetic benchmarks and real-world trajectory planning tasks.
