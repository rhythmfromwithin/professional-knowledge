---
title: "A Bayesian Framework for Built-in Input Dimension Reduction for Gaussian Process Modeling"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.19498
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Bayesian Framework for Built-in Input Dimension Reduction for Gaussian Process Modeling
> 原文: [https://arxiv.org/abs/2607.19498](https://arxiv.org/abs/2607.19498)

arXiv:2607.19498v1 Announce Type: new
Abstract: Gaussian process (GP) modeling is widely used in computational science and engineering. However, fitting a GP to high-dimensional inputs remains challenging due to the curse of dimensionality. While various methods have been proposed to reduce input dimensionality, they typically follow a two-stage approach, performing dimension reduction and GP fitting separately. We introduce a Bayesian framework that seamlessly integrates dimensionality reduction with GP modeling and inference. Our approach, built on a hierarchical Bayesian model with priors on the Stiefel manifold, enforces orthonormality on the projection matrix and enables posterior inference via Hamiltonian Monte Carlo with geodesic flow. Additionally, we extend this framework by incorporating Deep Gaussian Processes (DGP) with built-in dimension reduction, providing a more flexible and powerful tool for complex datasets. Through extensive numerical studies, we demonstrate that while the proposed Bayesian method incurs higher computational costs, it improves predictive performance and uncertainty quantification, providing a principled and robust alternative to existing methods.
