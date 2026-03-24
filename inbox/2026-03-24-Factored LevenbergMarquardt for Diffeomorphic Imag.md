---
title: "Factored Levenberg-Marquardt for Diffeomorphic Image Registration: An efficient optimizer for FireANTs"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.19371
priority: medium
status: unread
interest: medium
next_step: skim
---
# Factored Levenberg-Marquardt for Diffeomorphic Image Registration: An efficient optimizer for FireANTs
> 原文: [https://arxiv.org/abs/2603.19371](https://arxiv.org/abs/2603.19371)

arXiv:2603.19371v1 Announce Type: new
Abstract: FireANTs introduced a novel Eulerian descent method for plug-and-play behavior with arbitrary optimizers adapted for diffeomorphic image registration as a test-time optimization problem, with a GPU-accelerated implementation. FireANTs uses Adam as its default optimizer for fast and more robust optimization. However, Adam requires storing state variables (i.e. momentum and squared-momentum estimates), each of which can consume significant memory, prohibiting its use for significantly large images. In this work, we propose a modified Levenberg-Marquardt (LM) optimizer that requires only a single scalar damping parameter as optimizer state, that is adaptively tuned using a trust region approach. The resulting optimizer reduces memory by up to 24.6% for large volumes, and retaining performance across all four datasets. A single hyperparameter configuration tuned on brain MRI transfers without modification to lung CT and cross-modal abdominal registration, matching or outperforming Adam on three of four benchmarks. We also perform ablations on the effectiveness of using Metropolis-Hastings style rejection step to prevent updates that worsen the loss function.
