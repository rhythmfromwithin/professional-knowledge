---
interest: medium
link: https://arxiv.org/abs/2604.04963
next_step: skim
priority: medium
slack_ts: '1775703403.492799'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Learning Nonlinear Regime Transitions via Semi-Parametric State-Space Models
---
# Learning Nonlinear Regime Transitions via Semi-Parametric State-Space Models
> 原文: [https://arxiv.org/abs/2604.04963](https://arxiv.org/abs/2604.04963)

arXiv:2604.04963v1 Announce Type: new
Abstract: We develop a semi-parametric state-space model for time-series data with latent regime transitions. Classical Markov-switching models use fixed parametric transition functions, such as logistic or probit links, which restrict flexibility when transitions depend on nonlinear and context-dependent effects. We replace this assumption with learned functions $f\_0, f\_1 \in \calH$, where $\calH$ is either a reproducing kernel Hilbert space or a spline approximation space, and define transition probabilities as $p\_{jk,t} = \sigmoid(f(\bx\_{t-1}))$.
The transition functions are estimated jointly with emission parameters using a generalized Expectation-Maximization algorithm. The E-step uses the standard forward-backward recursion, while the M-step reduces to a penalized regression problem with weights from smoothed occupation measures. We establish identifiability conditions and provide a consistency argument for the resulting estimators.
Experiments on synthetic data show improved recovery of nonlinear transition dynamics compared to parametric baselines. An empirical study on financial time series demonstrates improved regime classification and earlier detection of transition events.
