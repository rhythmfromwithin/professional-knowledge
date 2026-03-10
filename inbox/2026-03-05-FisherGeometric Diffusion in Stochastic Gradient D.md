---
interest: medium
link: https://arxiv.org/abs/2603.02417
next_step: skim
priority: medium
slack_ts: '1773132452.486239'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Fisher-Geometric Diffusion in Stochastic Gradient Descent: Optimal Rates,
  Oracle Complexity, and Information-Theoretic Limits'
---
# Fisher-Geometric Diffusion in Stochastic Gradient Descent: Optimal Rates, Oracle Complexity, and Information-Theoretic Limits
> 原文: [https://arxiv.org/abs/2603.02417](https://arxiv.org/abs/2603.02417)

arXiv:2603.02417v1 Announce Type: new
Abstract: We develop a Fisher-geometric theory of stochastic gradient descent (SGD) in which mini-batch noise is an intrinsic, loss-induced matrix -- not an exogenous scalar variance. Under exchangeable sampling, the mini-batch gradient covariance is pinned down (to leading order) by the projected covariance of per-sample gradients: it equals projected Fisher information for well-specified likelihood losses and the projected Godambe (sandwich) matrix for general M-estimation losses. This identification forces a diffusion approximation with Fisher/Godambe-structured volatility (effective temperature tau = eta/b) and yields an Ornstein-Uhlenbeck linearization whose stationary covariance is given in closed form by a Fisher-Lyapunov equation. Building on this geometry, we prove matching minimax upper and lower bounds of order Theta(1/N) for Fisher/Godambe risk under a total oracle budget N; the lower bound holds under a martingale oracle condition (bounded predictable quadratic variation), strictly subsuming i.i.d. and exchangeable sampling. These results imply oracle-complexity guarantees for epsilon-stationarity in the Fisher dual norm that depend on an intrinsic effective dimension and a Fisher/Godambe condition number rather than ambient dimension or Euclidean conditioning. Experiments confirm the Lyapunov predictions and show that scalar temperature matching cannot reproduce directional noise structure.
