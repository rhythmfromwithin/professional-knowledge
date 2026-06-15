---
interest: medium
link: https://arxiv.org/abs/2606.13796
next_step: skim
priority: medium
slack_ts: '1781500247.023439'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral
  Characterization'
---
# Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization
> 原文: [https://arxiv.org/abs/2606.13796](https://arxiv.org/abs/2606.13796)

arXiv:2606.13796v1 Announce Type: new
Abstract: Recursive training of generative models on their own outputs can lead to model collapse, a compounding drift away from the true data distribution. Existing theoretical works bound finite-round error accumulation in the context of diffusion models, but two questions remain open:~what distribution does the recursion converge to, and how fast? We answer both, isolating a mechanism distinct from imperfect learning: even with perfect score estimation and exact sampling, the early stopping of the reverse diffusion (required for numerical stability) drives a progressive drift away from the data distribution. We prove that this recursion converges geometrically to a unique limiting distribution, which admits a closed-form characterization as an infinite mixture of increasingly Gaussian-smoothed versions of the data distribution. A Hermite spectral decomposition of this limit reveals that recursive training acts as a low-pass filter: higher-order modes, which encode fine non-Gaussian structure, are attenuated much more strongly than coarse modes. This spectral picture motivates annealed truncation schedules that progressively shrink truncation times across retraining rounds; we prove that any schedule converging to $0$ asymptotically eliminates recursive compounding. Finally, we show our idealized characterization is robust: in the presence of discretization and score estimation errors, the learned distribution remains in a Wasserstein-2 ball around the ideal limit, with mode-dependent contraction rates that contract high-order errors faster than low-order ones. We validate the theory on synthetic Gaussian mixtures and CIFAR-10.
