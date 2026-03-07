---
title: "Bayesian Modeling of Collatz Stopping Times: A Probabilistic Machine Learning Perspective"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.04479
priority: medium
status: unread
---
# Bayesian Modeling of Collatz Stopping Times: A Probabilistic Machine Learning Perspective
> 原文: [https://arxiv.org/abs/2603.04479](https://arxiv.org/abs/2603.04479)

arXiv:2603.04479v1 Announce Type: new
Abstract: We study the Collatz total stopping time $\tau(n)$ over $n\le 10^7$ from a probabilistic machine learning viewpoint. Empirically, $\tau(n)$ is a skewed and heavily overdispersed count with pronounced arithmetic heterogeneity. We develop two complementary models. First, a Bayesian hierarchical Negative Binomial regression (NB2-GLM) predicts $\tau(n)$ from simple covariates ($\log n$ and residue class $n \bmod 8$), quantifying uncertainty via posterior and posterior predictive distributions. Second, we propose a mechanistic generative approximation based on the odd-block decomposition: for odd $m$, write $3m+1=2^{K(m)}m'$ with $m'$ odd and $K(m)=v\_2(3m+1)\ge 1$; randomizing these block lengths yields a stochastic approximation calibrated via a Dirichlet-multinomial update. On held-out data, the NB2-GLM achieves substantially higher predictive likelihood than the odd-block generators. Conditioning the block-length distribution on $m\bmod 8$ markedly improves the generator's distributional fit, indicating that low-order modular structure is a key driver of heterogeneity in $\tau(n)$.
