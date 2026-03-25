---
interest: medium
link: https://arxiv.org/abs/2603.18039
next_step: skim
priority: low
slack_ts: '1774407042.279059'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Sharpness Aware Surrogate Training for Spiking Neural Networks
---
# Sharpness Aware Surrogate Training for Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2603.18039](https://arxiv.org/abs/2603.18039)

arXiv:2603.18039v1 Announce Type: new
Abstract: Surrogate gradients are a standard tool for training spiking neural networks (SNNs), but conventional hard forward or surrogate backward training couples a nonsmooth forward model with a biased gradient estimator. We study sharpness aware Surrogate Training (SAST), which applies sharpness aware Minimization (SAM) to a surrogate forward SNN trained by backpropagation. In this formulation, the optimization target is an ordinary smooth empirical risk, so the training gradient is exact for the auxiliary model being optimized. Under explicit boundedness and contraction assumptions, we derive compact state stability and input Lipschitz bounds, establish smoothness of the surrogate objective, provide a first order SAM approximation bound, and prove a nonconvex convergence guarantee for stochastic SAST with an independent second minibatch. We also isolate a local mechanism proposition, stated separately from the unconditional guarantees, that links per sample parameter gradient control to smaller input gradient norms under local Jacobian conditioning. Empirically, we evaluate clean accuracy, hard spike transfer, corruption robustness, and training overhead on N-MNIST and DVS Gesture. The clearest practical effect is transfer gap reduction: on N-MNIST, hard spike accuracy rises from 65.7% to 94.7% (best at $\rho=0.30$) while surrogate forward accuracy remains high; on DVS Gesture, hard spike accuracy improves from 31.8% to 63.3% (best at $\rho=0.40$). We additionally specify the compute matched, calibration, and theory alignment controls required for a final practical assessment.
