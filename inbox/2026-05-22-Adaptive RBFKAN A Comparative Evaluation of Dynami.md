---
interest: medium
link: https://arxiv.org/abs/2605.21534
next_step: skim
priority: medium
slack_ts: '1779596221.062169'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Adaptive RBF-KAN: A Comparative Evaluation of Dynamic Shape Parameters in
  Kolmogorov-Arnold Networks'
---
# Adaptive RBF-KAN: A Comparative Evaluation of Dynamic Shape Parameters in Kolmogorov-Arnold Networks
> 原文: [https://arxiv.org/abs/2605.21534](https://arxiv.org/abs/2605.21534)

arXiv:2605.21534v1 Announce Type: new
Abstract: Kolmogorov-Arnold Networks (KANs) approximate multivariate functions using learnable univariate edge functions, typically parameterized by B-spline bases. Although effective, spline-based implementations can be computationally expensive. A modified version of KANs, called FastKAN, improves efficiency by replacing splines with Gaussian radial basis functions (RBFs), but it relies on a fixed kernel and shape parameter. In this work, we extend the RBF-based KAN framework by introducing a broader family of radial basis kernels and by initializing the kernel shape parameter using leave-one-out cross-validation (LOOCV). To the best of our knowledge, this is the first study that integrates LOOCV-based kernel scale estimation with deep KAN training. We also introduce Mat\'ern and Wendland kernels into the KAN framework for the first time, enabling more flexible basis representations beyond the Gaussian kernel used in FastKAN. The LOOCV estimate provides a data-driven initialization of the kernel scale, which is subsequently refined during network training. The proposed adaptive RBF-KAN is evaluated on several two-dimensional benchmark functions. The results highlight the importance of kernel selection and adaptive shape parameters, with different kernels showing advantages for smooth functions, discontinuities, and oscillatory patterns. Overall, combining LOOCV-based initialization with adaptive kernel learning provides a practical strategy for improving RBF-based KAN models.
