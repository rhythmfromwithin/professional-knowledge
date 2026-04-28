---
title: "Concave Statistical Utility Maximization Bandits via Influence-Function Gradients"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.22140
priority: medium
status: unread
interest: medium
next_step: skim
---
# Concave Statistical Utility Maximization Bandits via Influence-Function Gradients
> 原文: [https://arxiv.org/abs/2604.22140](https://arxiv.org/abs/2604.22140)

arXiv:2604.22140v1 Announce Type: new
Abstract: We study stochastic multi-armed bandits in which the objective is a statistical functional of the long-run reward distribution, rather than expected reward alone. Under mild continuity assumptions, we show that the infinite-horizon problem reduces to optimizing over stationary mixed policies: each weight vector \(w\) on the simplex induces a mixture law \(P^w\), and performance is measured by the concave utility \(U(w)=\mathfrak U(P^w)\).
For differentiable statistical utilities, we use influence-function calculus to derive stochastic gradient estimators from bandit feedback. This leads to an entropic mirror-ascent algorithm on a truncated simplex, implemented through multiplicative-weights updates and plug-in estimates of the influence function. We establish regret bounds that separate the mirror-ascent optimization error from the bias caused by estimating the influence function. The framework is developed for general concave distributional utilities and illustrated through variance and Wasserstein objectives, with numerical experiments comparing exact and plug-in influence-function implementations.
