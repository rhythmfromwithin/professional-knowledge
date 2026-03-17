---
title: "Variational Garrote for Sparse Inverse Problems"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.12562
priority: medium
status: unread
interest: medium
next_step: skim
---
# Variational Garrote for Sparse Inverse Problems
> 原文: [https://arxiv.org/abs/2603.12562](https://arxiv.org/abs/2603.12562)

arXiv:2603.12562v1 Announce Type: new
Abstract: Sparse regularization plays a central role in solving inverse problems arising from incomplete or corrupted measurements. Different regularizers correspond to different prior assumptions about the structure of the unknown signal, and reconstruction performance depends on how well these priors match the intrinsic sparsity of the data. This work investigates the effect of sparsity priors in inverse problems by comparing conventional L1 regularization with the Variational Garrote (VG), a probabilistic method that approximates L0 sparsity through variational binary gating variables. A unified experimental framework is constructed across multiple reconstruction tasks including signal resampling, signal denoising, and sparse-view computed tomography. To enable consistent comparison across models with different parameterizations, regularization strength is swept across wide ranges and reconstruction behavior is analyzed through train-generalization error curves. Experiments reveal characteristic bias-variance tradeoff patterns across tasks and demonstrate that VG frequently achieves lower minimum generalization error and improved stability in strongly underdetermined regimes where accurate support recovery is critical. These results suggest that sparsity priors closer to spike-and-slab structure can provide advantages when the underlying coefficient distribution is strongly sparse. The study highlights the importance of prior-data alignment in sparse inverse problems and provides empirical insights into the behavior of variational L0-type methods across different information bottlenecks.
