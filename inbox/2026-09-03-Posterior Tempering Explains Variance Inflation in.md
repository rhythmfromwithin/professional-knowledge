---
title: "Posterior Tempering Explains Variance Inflation in Linear and Generalized Linear Thompson Sampling"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.01999
priority: medium
status: unread
interest: medium
next_step: skim
---
# Posterior Tempering Explains Variance Inflation in Linear and Generalized Linear Thompson Sampling
> 原文: [https://arxiv.org/abs/2609.01999](https://arxiv.org/abs/2609.01999)

arXiv:2609.01999v1 Announce Type: new
Abstract: We study a variant of the Thompson Sampling (TS) algorithm, called $\alpha$-TS, for solving stochastic generalized linear bandit problems. Existing analyses of TS require inflating the posterior variance to derive near-optimal regret guarantees. We formalize the idea of variance inflation by introducing $\alpha$-TS that uses a fractional or $\alpha$-posterior instead of the standard posterior. Our main contribution is to identify general regularity conditions on the prior and reward distributions that enable a regret analysis of $\alpha$-TS without assuming any tractable approximation of the posterior distribution, unlike previous works. For a specific choice of $\alpha \propto d^{-1}$, our general regret bound yields the best known regret bound of $O(d^{3/2}\sqrt{T}\log T)$ for both the exponential and sub-Gaussian families of reward distributions. We further provide an $\alpha$-dependent lower bound showing that the regret constant depends on the product $\alpha d$, and that when $\alpha \propto d^{-1}$ the regret scales as $\Omega(d^{3/2}\sqrt{T})$, explaining the origin of the $d^{3/2}$ factor in the upper bound. Our proof technique adapts and combines recent advancements in the analysis of linear bandit problems with first- and second-order posterior concentration theory from the Bayesian statistics literature.
