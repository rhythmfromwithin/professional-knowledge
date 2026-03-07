---
title: "DuaLip-GPU Technical Report"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.04621
priority: medium
status: unread
---
# DuaLip-GPU Technical Report
> 原文: [https://arxiv.org/abs/2603.04621](https://arxiv.org/abs/2603.04621)

arXiv:2603.04621v1 Announce Type: new
Abstract: Large-scale linear programs (LPs) arise in many decision systems, including ranking, allocation, and matching problems that must be solved repeatedly at massive scale. Prior work such as ECLIPSE and LinkedIn's open-source DuaLip showed that ridge-regularized dual ascent with first-order methods can scale to these settings. However, the original implementation was tightly coupled to a small number of schemas and built on a CPU-centric Scala/Spark stack, limiting extensibility and preventing effective use of modern accelerators.
We present a redesigned solver architecture that decouples problem specification from the optimization engine and targets GPU execution. The system uses an operator-centric programming model in which LP formulations are expressed through composable primitives for dual objective evaluation and blockwise projection operators for decomposable constraint families. This design allows new formulations to be added locally while reusing a shared optimization loop, diagnostics, and distributed infrastructure.
To realize the available parallelism, we develop GPU execution techniques tailored to sparse matching constraints, including constraint-aligned sparse layouts, batched projection kernels, and a distributed design that communicates only dual variables. Further, we improve the underlying ridge-regularized dual ascent method with Jacobi-style row normalization, primal scaling, and a continuation scheme for the regularization parameter.
On extreme-scale matching workloads, the GPU implementation achieves at least a 10x wall-clock speedup over the prior distributed CPU DuaLip solver under matched stopping criteria, while maintaining convergence guarantees.
