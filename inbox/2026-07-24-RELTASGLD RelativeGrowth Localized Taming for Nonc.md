---
interest: medium
link: https://arxiv.org/abs/2607.19544
next_step: skim
priority: medium
slack_ts: '1784863648.411989'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'RELTA-SGLD: Relative-Growth Localized Taming for Nonconvex Stochastic-Gradient
  Langevin Learning'
---
# RELTA-SGLD: Relative-Growth Localized Taming for Nonconvex Stochastic-Gradient Langevin Learning
> 原文: [https://arxiv.org/abs/2607.19544](https://arxiv.org/abs/2607.19544)

arXiv:2607.19544v1 Announce Type: new
Abstract: We introduce RELTA-SGLD, a taming scheme that stabilizes superlinear stochastic-gradient updates while reducing unnecessary suppression of the original learning drift. A threshold determines where the taming turns on, while a relative-growth principle derived from the one-step Lyapunov stability condition determines the required taming strength. Together, they produce a lighter $\lambda$-scale denominator and preserve a nonvanishing far-tail return. As a consequence, we prove polynomial moment stability and first-order stationary accuracy in both $W\_1$ and $W\_2$ for nonconvex SGLD with superlinearly growing stochastic-gradient oracles, improving the corresponding half-order and quarter-order bounds for comparable stochastic-gradient tamed schemes. On Fashion-MNIST under active stabilization pressure, RELTA improves the mean learning metrics over both untamed SGLD and TUSLA and remains competitive with a tuned AdamW reference. In an ordinary-training regime, its lighter localized denominator reduces unnecessary perturbation of the original update and maintains nearly untamed learning dynamics.
