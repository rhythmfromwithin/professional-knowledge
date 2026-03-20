---
interest: medium
link: https://arxiv.org/abs/2603.10184
next_step: skim
priority: medium
slack_ts: '1773974638.316559'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Stability and Robustness via Regularization: Bandit Inference via Regularized
  Stochastic Mirror Descent'
---
# Stability and Robustness via Regularization: Bandit Inference via Regularized Stochastic Mirror Descent
> 原文: [https://arxiv.org/abs/2603.10184](https://arxiv.org/abs/2603.10184)

arXiv:2603.10184v1 Announce Type: new
Abstract: Statistical inference with bandit data presents fundamental challenges due to adaptive sampling, which violates the independence assumptions underlying classical asymptotic theory. Recent work has identified stability as a sufficient condition for valid inference under adaptivity. This paper develops a systematic theory of stability for bandit algorithms based on stochastic mirror descent, a broad algorithmic framework that includes the widely-used EXP3 algorithm as a special case.
Our contributions are threefold. First, we establish a general stability criterion: if the average iterates of a stochastic mirror descent algorithm converge in ratio to a non-random probability vector, then the induced bandit algorithm is stable. This result provides a unified lens for analyzing stability across diverse algorithmic instantiations. Second, we introduce a family of regularized-EXP3 algorithms employing a log-barrier regularizer with appropriately tuned parameters. We prove that these algorithms satisfy our stability criterion and, as an immediate corollary, that Wald-type confidence intervals for linear functionals of the mean parameter achieve nominal coverage. Notably, we show that the same algorithms attain minimax-optimal regret guarantees up to logarithmic factors, demonstrating that inference-enabling stability and learning efficiency are compatible objectives within the mirror descent framework. Third, we establish robustness to corruption: a modified variant of regularized-EXP3 maintains asymptotic normality of empirical arm means even in the presence of $o(T^{1/2})$ adversarial corruptions. This stands in sharp contrast to other stable algorithms such as UCB, which suffer linear regret even under logarithmic levels of corruption.
