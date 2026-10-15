---
title: "Parallel Sparse Outputs for Tensor Compilers"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.19308
priority: medium
status: unread
interest: medium
next_step: skim
---
# Parallel Sparse Outputs for Tensor Compilers
> 原文: [https://arxiv.org/abs/2610.19308](https://arxiv.org/abs/2610.19308)

arXiv:2610.19308v1 Announce Type: new
Abstract: Sparse tensor compilers are commonly used high-performance tools that optimize tensor algebra programs over notoriously complex sparse data structures. Despite the ever-increasing size and scale of sparse datasets, there exists astonishingly little research on developing a parallel sparse tensor compiler. Existing approaches fail to parallelize or make assumptions about access patterns or output formats that limit generality.
This paper presents Birdseed, the first tensor compiler to support all loop orderings over any standard sparse format in parallel. More specifically, Birdseed supports parallel sparse scatters and directly writes into list, bytemap, hash, and dense levels of fibertree sparse formats. Our approach exhibits asymptotic memory and time improvements over all previous work. We additionally demonstrate empirical speedups on challenging kernels to parallelize, such as histogram construction and SpMSpV.
