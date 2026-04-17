---
interest: medium
link: https://arxiv.org/abs/2604.13147
next_step: skim
priority: medium
slack_ts: '1776396656.954489'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Adaptive Learning via Off-Model Training and Importance Sampling for Fully
  Non-Markovian Optimal Stochastic Control. Complete version
---
# Adaptive Learning via Off-Model Training and Importance Sampling for Fully Non-Markovian Optimal Stochastic Control. Complete version
> 原文: [https://arxiv.org/abs/2604.13147](https://arxiv.org/abs/2604.13147)

arXiv:2604.13147v1 Announce Type: new
Abstract: This paper studies continuous-time stochastic control problems whose controlled states are fully non-Markovian and depend on unknown model parameters. Such problems arise naturally in path-dependent stochastic differential equations, rough-volatility hedging, and systems driven by fractional Brownian motion. Building on the discrete skeleton approach developed in earlier work, we propose a Monte Carlo learning methodology for the associated embedded backward dynamic programming equation. Our main contribution is twofold. First, we construct explicit dominating training laws and Radon--Nikodym weights for several representative classes of non-Markovian controlled systems. This yields an off-model training architecture in which a fixed synthetic dataset is generated under a reference law, while the dynamic programming operators associated with a target model are recovered by importance sampling. Second, we use this structure to design an adaptive update mechanism under parametric model uncertainty, so that repeated recalibration can be performed by reweighting the same training sample rather than regenerating new trajectories. For fixed parameters, we establish non-asymptotic error bounds for the approximation of the embedded dynamic programming equation via deep neural networks. For adaptive learning, we derive quantitative estimates that separate Monte Carlo approximation error from model-risk error. Numerical experiments illustrate both the off-model training mechanism and the adaptive importance-sampling update in structured linear-quadratic examples.
