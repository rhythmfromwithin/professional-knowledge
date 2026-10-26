---
title: "Autoregressive Physics-Informed Neural Operator Surrogates and Joint 4-D Seismic-Production Bayesian History Matching"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.31677
priority: medium
status: unread
interest: medium
next_step: skim
---
# Autoregressive Physics-Informed Neural Operator Surrogates and Joint 4-D Seismic-Production Bayesian History Matching
> 原文: [https://arxiv.org/abs/2610.31677](https://arxiv.org/abs/2610.31677)

arXiv:2610.31677v1 Announce Type: new
Abstract: We present a surrogate-accelerated Bayesian history-matching framework, demonstrated on a realistic synthetic model ($N=100{,}188$ cells). The forward map $\mathcal{G}$ is replaced by a Fourier neural operator $\mathcal{G}\_\theta$ trained in a closed loop, $\hat{x}\_{n+1}=\mathcal{G}\_\theta(u,\hat{x}\_n)$, with the discrete black-oil residual $R(x\_{n+1},x\_n)$ as a physics-informed neural operator (PINO) penalty, truncated backpropagation and noise injection. We assimilate production data and 4-D seismic using adaptive regularised ensemble Kalman inversion (aREKI), and synthesise $\Delta V\_p$ inside the rollout via a closed-form Gassmann transform of the surrogate, under a two-stage schedule (aREKI on production, then an ensemble smoother with multiple data assimilation, ES-MDA, on both). To temper the ill-posedness, we invert $(\log K,\phi)$ not in $\mathbb{R}^{2N}$, where $N\_e\ll 2N$ leaves a rank-deficient covariance and a null space the data never inform, but on a chart $u=\Psi(\tilde m)$, $\tilde m\in\mathbb{R}^{d}$, $d\ll 2N$, given by a Parseval-exact truncated cosine transform or a variational auto-encoder decoder. The ensemble then spans its own search space; the directions the data cannot constrain are cut to those the chart can express, and every member decodes to a geologically plausible field. For the rollout we prove an exposure bound $W\_1\le\sum\_j L^{\,n-1-j}\mathbb{E}e\_j$, a physics-penalty contraction $\|D\_x\mathcal{G}\_\theta\|\le\alpha<1$ under a small residual defect, and an $\mathcal{O}(\rho^K)$ truncation bias. A Loewner-order inequality $\mathcal{I}\_p\preceq\mathcal{I}\_p+\mathcal{I}\_s$ explains why joint assimilation is no less informative. On held-out data, $\mathcal{G}\_\theta$ attains $R^2>0.999$ on pressure and saturation and rolls out in $0.579$ s, a $\sim2500\times$ speed-up, bringing an $N\_e=190$-member, $N\_a=10$-iteration joint inversion within one GPU-hour.
