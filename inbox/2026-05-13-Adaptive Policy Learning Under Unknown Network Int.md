---
interest: medium
link: https://arxiv.org/abs/2605.11191
next_step: skim
priority: medium
slack_ts: '1778731259.038759'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Adaptive Policy Learning Under Unknown Network Interference
---
# Adaptive Policy Learning Under Unknown Network Interference
> 原文: [https://arxiv.org/abs/2605.11191](https://arxiv.org/abs/2605.11191)

arXiv:2605.11191v1 Announce Type: new
Abstract: Adaptive experimentation under unknown network interference requires solving two coupled problems: (i) learning the underlying dynamics of interference among units and (ii) using these dynamics to inform treatment allocation in order to maximize a cumulative outcome of interest (e.g. revenue). Existing adaptive experimentation methods either assume the interference network is fully known or bypass the network by operating on coarse cluster-level randomizations. We develop a Thompson sampling algorithm that jointly learns the interference network and adaptively optimizes individual-level treatment allocations via a Gibbs sampler. The algorithm returns both an optimized treatment policy and an estimate of the interference network; the latter supports downstream causal analyses such as estimation of direct, indirect, and total treatment effects. For additive spillover models, we show that total reward is linear in the treatment vector with coefficients given by an $n$-dimensional latent score. We prove a Bayesian regret bound of order $\sqrt{nT \cdot B \log(en/B)}$ for exact posterior sampling; empirically, our Gibbs-based approximate sampler achieves regret consistent with this rate and remains sublinear when the additive spillovers assumption is violated. For general Neighborhood Interference, where this reduction is unavailable, we analyze an explore-then-commit variant with $O(n^2 \log T)$ graph-discovery cost. An information-theoretic $\Omega(n \log T)$ lower bound complements both results. Empirically, our method achieves more than an order-of-magnitude reduction in regret in head-to-head comparisons. On two real-world networks, the algorithm achieves sublinear regret and yields downstream effect estimates with small RMSE relative to the truth.
