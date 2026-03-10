---
title: "Do We Need Tensor Cores for Stencil Computations?"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.00477
priority: medium
status: unread
interest: medium
next_step: skim
---
# Do We Need Tensor Cores for Stencil Computations?
> 原文: [https://arxiv.org/abs/2603.00477](https://arxiv.org/abs/2603.00477)

arXiv:2603.00477v1 Announce Type: new
Abstract: Stencil computation constitutes a cornerstone of scientific computing, serving as a critical kernel in domains ranging from fluid dynamics to weather simulation. While stencil computations are conventionally regarded as memory-bound and thus unsuitable for compute-centric Tensor Cores, recent empirical studies have demonstrated significant speedups after applying Tensor Cores, forming an apparent contradiction.
This paper resolves this contradiction by conducting a systematic performance analysis of stencil computations on Tensor Cores. We begin by revisiting the adaptation of stencils onto Tensor Cores, quantifying the computational redundancy introduced by the transformations required to satisfy hardware constraints. These metrics are subsequently integrated into an enhanced performance model that explicitly accounts for the arithmetic intensity shifts driven by temporal fusion. Guided by this formulation, we derive analytical criteria to determine the suitability of Tensor Cores for varying stencil workloads. By classifying operational regions, we identify the specific \textit{sweet spot} for effective acceleration and further demonstrate how Sparse Tensor Cores expand this profitable design space. Extensive evaluations on NVIDIA GPUs across SOTA implementations, including DRStencil, EBISU, ConvStencil, and SPIDER, validate our performance model and analytical criteria. These results demonstrate the effectiveness of our approach in guiding stencil performance optimization.
