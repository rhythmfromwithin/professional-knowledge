---
interest: medium
link: https://arxiv.org/abs/2607.00095
next_step: skim
priority: high
slack_ts: '1783050942.622449'
source: cs.LG - Machine Learning
status: unread
title: 'SNAP-FM: Sparse Nonlinear Accelerated Projection for Physics-Constrained Generative
  Modeling'
---
# SNAP-FM: Sparse Nonlinear Accelerated Projection for Physics-Constrained Generative Modeling
> 原文: [https://arxiv.org/abs/2607.00095](https://arxiv.org/abs/2607.00095)

arXiv:2607.00095v1 Announce Type: new
Abstract: Generative models have emerged as scalable surrogates for physical simulation, yet they offer no guarantee that their outputs respect the conservation laws, boundary conditions, and nonlinear invariants that govern the underlying physics. Constrained sampling closes this gap, enforcing such constraints exactly at inference time without retraining, but at a computational cost: projection, correction, and trajectory-optimization steps are repeated during sampling, with these steps becoming expensive for nonlinear constraints. Standard ML frameworks exacerbate this: their dense tensor algebra and limited sparse solver composability obscure the structure that physical constraints naturally induce, making efficient batched nonlinear optimization difficult to realize in practice. We address this bottleneck by exploiting the structure that sample-wise batching and local PDE couplings induce in the projection subproblems -- namely, block-sparse Jacobian and KKT systems -- exposing this structure using ExaModels.jl and solving the resulting sparse nonlinear programs with MadNLP.jl and GPU sparse factorization. Applied to Physics-Constrained Flow Matching (PCFM), on PDE benchmarks with linear, nonlinear, one-dimensional, and two-dimensional constraints, this approach accelerates nonlinear constraint projection while maintaining constraint satisfaction. These results show that sparse GPU nonlinear optimization is a practical foundation for constrained generative sampling in scientific machine learning.
