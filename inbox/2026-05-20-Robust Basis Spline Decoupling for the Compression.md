---
interest: medium
link: https://arxiv.org/abs/2605.18794
next_step: skim
priority: high
slack_ts: '1779423489.997759'
source: cs.LG - Machine Learning
status: unread
title: Robust Basis Spline Decoupling for the Compression of Transformer Models
---
# Robust Basis Spline Decoupling for the Compression of Transformer Models
> 原文: [https://arxiv.org/abs/2605.18794](https://arxiv.org/abs/2605.18794)

arXiv:2605.18794v1 Announce Type: new
Abstract: Decoupling is a powerful modeling paradigm for representing multivariate functions as compositions of linear transformations and univariate nonlinear functions. A single-layer decoupling can be viewed as a fully connected neural network with a single hidden layer and flexible activation functions, providing a direct link with neural networks. Because of this, the use of decoupling methods has gained increasing attention in neural network domains, particularly compression, since it enables structured approximations with reduced parameter complexity. Existing tensor-based decoupling methods typically rely on polynomial or piecewise-linear parameterizations of the internal nonlinear functions, which can suffer from numerical instability or limited expressiveness. In this work, we introduce a B-spline-based decoupling framework that generalizes these existing approaches. By exploiting the local support and flexible smoothness control of B-splines, the proposed formulation yields a more numerically stable and expressive representation. We derive a constrained coupled matrix-tensor factorization and propose a robust alternating least-squares algorithm, called R-CMTF-BSD, incorporating normalization and Tikhonov regularization. The proposed method is validated through experiments on synthetic data and transformer model compression. Results on the Vision and Swin Transformer architectures demonstrate that B-spline decoupling enables substantial parameter reduction while maintaining competitive accuracy, making the R-CMTF-BSD algorithm a promising tool for structured neural network compression.
