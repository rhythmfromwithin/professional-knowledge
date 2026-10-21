---
interest: medium
link: https://arxiv.org/abs/2610.27010
next_step: skim
priority: medium
slack_ts: '1792556428.476919'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Robust Latent Variable Graphical Models: Exact Recovery and Fundamental Limits'
---
# Robust Latent Variable Graphical Models: Exact Recovery and Fundamental Limits
> 原文: [https://arxiv.org/abs/2610.27010](https://arxiv.org/abs/2610.27010)

arXiv:2610.27010v1 Announce Type: new
Abstract: We study robust estimation of a Gaussian precision matrix that decomposes as a sparse matrix minus a symmetric, possibly indefinite, low-rank matrix, a structure that arises when latent-variable marginalization is combined with conditioning on linear measurements. The proposed convex estimator replaces the sample covariance by the centered Gaussian measure-transformed (MT) covariance, which preserves the signed graph of the sparse component under the nominal model, and penalizes the low-rank component by the nuclear norm of a congruence transform, an atomic norm that encodes structural side information. Our main result is a primal--dual witness theorem: under restricted invertibility and irrepresentability conditions on the Fisher information, the raw convex optimizer is unique, has no false edges, recovers the signs of all sufficiently strong edges, and has exactly the true rank and inertia. These conditions reduce to the graphical-lasso conditions when the low-rank part is absent, and we verify them from primitive incoherence and near-isotropy assumptions. Over a class on which they hold uniformly, we prove information-theoretic limits for Frobenius estimation, signed graph recovery, and inertia recovery. In particular, inertia recovery requires $N\gtrsim p/\nu\_{\min}^2$ samples, where $\nu\_{\min}$ is the smallest nonzero eigenvalue modulus of the low-rank part; the spectral beta-min condition of the witness theorem is necessary up to a $\sqrt{\log p}$ factor; and the Frobenius risk attains the minimax rate up to a factor $\sqrt{\mu(1+\min\{d,r\})\log p}$, where $\mu$ is the incoherence parameter, $d$ the maximal degree, and $r$ the rank. We further quantify robustness under Huber contamination, with a bias bound that is sharp for the MT functional and vanishes for remote outliers, and give a globally convergent linearized ADMM with closed-form updates.
