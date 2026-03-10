---
title: "The Volterra signature"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.04525
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Volterra signature
> 原文: [https://arxiv.org/abs/2603.04525](https://arxiv.org/abs/2603.04525)

arXiv:2603.04525v1 Announce Type: new
Abstract: Modern approaches for learning from non-Markovian time series, such as recurrent neural networks, neural controlled differential equations or transformers, typically rely on implicit memory mechanisms that can be difficult to interpret or to train over long horizons. We propose the Volterra signature $\mathrm{VSig}(x;K)$ as a principled, explicit feature representation for history-dependent systems. By developing the input path $x$ weighted by a temporal kernel $K$ into the tensor algebra, we leverage the associated Volterra--Chen identity to derive rigorous learning-theoretic guarantees. Specifically, we prove an injectivity statement (identifiability under augmentation) that leads to a universal approximation theorem on the infinite dimensional path space, which in certain cases is achieved by linear functionals of $\mathrm{VSig}(x;K)$. Moreover, we demonstrate applicability of the kernel trick by showing that the inner product associated with Volterra signatures admits a closed characterization via a two-parameter integral equation, enabling numerical methods from PDEs for computation. For a large class of exponential-type kernels, $\mathrm{VSig}(x;K)$ solves a linear state-space ODE in the tensor algebra. Combined with inherent invariance to time reparameterization, these results position the Volterra signature as a robust, computationally tractable feature map for data science. We demonstrate its efficacy in dynamic learning tasks on real and synthetic data, where it consistently improves classical path signature baselines.
