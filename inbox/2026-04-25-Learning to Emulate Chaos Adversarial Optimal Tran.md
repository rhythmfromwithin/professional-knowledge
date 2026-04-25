---
interest: medium
link: https://arxiv.org/abs/2604.21097
next_step: skim
priority: medium
slack_ts: '1777087215.766149'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Learning to Emulate Chaos: Adversarial Optimal Transport Regularization'
---
# Learning to Emulate Chaos: Adversarial Optimal Transport Regularization
> 原文: [https://arxiv.org/abs/2604.21097](https://arxiv.org/abs/2604.21097)

arXiv:2604.21097v1 Announce Type: new
Abstract: Chaos arises in many complex dynamical systems, from weather to power grids, but is difficult to accurately model using data-driven emulators, including neural operator architectures. For chaotic systems, the inherent sensitivity to initial conditions makes exact long-term forecasts theoretically infeasible, meaning that traditional squared-error losses often fail when trained on noisy data. Recent work has focused on training emulators to match the statistical properties of chaotic attractors by introducing regularization based on handcrafted local features and summary statistics, as well as learned statistics extracted from a diverse dataset of trajectories. In this work, we propose a family of adversarial optimal transport objectives that jointly learn high-quality summary statistics and a physically consistent emulator. We theoretically analyze and experimentally validate a Sinkhorn divergence formulation (2-Wasserstein) and a WGAN-style dual formulation (1-Wasserstein). Our experiments across a variety of chaotic systems, including systems with high-dimensional chaotic attractors, show that emulators trained with our approach exhibit significantly improved long-term statistical fidelity.
