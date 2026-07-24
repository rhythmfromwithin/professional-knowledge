---
title: "Native Multi-Dimensional Subquadratic Operators via Input Dependent Long Convolutions"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.19378
priority: high
status: unread
interest: medium
next_step: skim
---
# Native Multi-Dimensional Subquadratic Operators via Input Dependent Long Convolutions
> 原文: [https://arxiv.org/abs/2607.19378](https://arxiv.org/abs/2607.19378)

arXiv:2607.19378v1 Announce Type: new
Abstract: Subquadratic alternatives to attention require compromises when applied to multi-dimensional data: standard convolutions lack global receptive fields and input dependency, while recurrent models require rasterizing data such as images, volumes, and partial differential equation (PDE) into an ad-hoc $1\rm D$ scan order that violates their spatial structure. We introduce \textit{HyenaND}, a subquadratic, global, input-dependent operator that acts directly on the native geometry of multidimensional data through convolutions with implicitly parametrized global, input-dependent multi-dimensional convolutional kernels. Our CUDA implementation, \texttt{nSubQ}, fuses the FFT-convolution path to turn HyenaND's $\mathcal{O}(L \log L)$ scaling into wall-clock speedups. Across long-context genomics, computer vision, medical imaging, and PDE modeling, pure HyenaND stacks match the accuracy of strong attention baselines, while hybrid configurations that interleave HyenaND and attention layers outperform both pure attention and strong recurrence-based hybrids.
