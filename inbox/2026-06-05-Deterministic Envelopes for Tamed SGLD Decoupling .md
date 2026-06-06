---
interest: medium
link: https://arxiv.org/abs/2606.05242
next_step: skim
priority: medium
slack_ts: '1780718910.638549'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Deterministic Envelopes for Tamed SGLD: Decoupling Stochastic-Gradient Noise
  and Localizing Taming'
---
# Deterministic Envelopes for Tamed SGLD: Decoupling Stochastic-Gradient Noise and Localizing Taming
> 原文: [https://arxiv.org/abs/2606.05242](https://arxiv.org/abs/2606.05242)

arXiv:2606.05242v1 Announce Type: new
Abstract: Stochastic-gradient Langevin algorithms often use tamed denominators to stabilize non-globally Lipschitz drifts. This paper shows that when the denominator depends on the same stochastic-gradient realization as the numerator, the taming step changes the stochastic oracle itself and can create a stationary bias even if the original stochastic gradient is unbiased. We propose a structure-preserving framework for designing tamed denominators. It fixes the denominator before the oracle noise is sampled and uses localized deterministic envelopes to avoid unnecessary taming in typical regions. These kernels keep the stabilizing effect of taming while avoiding the bias introduced by a gradient-dependent denominator. Our theory explains how the stationary error splits into the bias caused by oracle-dependent taming and the remaining error introduced by deterministic stabilization. Within this deterministic-envelope family, the analysis identifies a far-tail condition that explains the limitation of local soft envelopes and motivates a hybrid member: soft in the typical region, but protected by hard-tail control on rare excursions. Experiments confirm the predicted stationary distortions of random denominators, the bias reduction of deterministic-envelope designs, and the stabilizing effect of the hybrid construction.
