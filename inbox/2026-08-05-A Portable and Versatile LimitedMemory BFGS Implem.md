---
interest: medium
link: https://arxiv.org/abs/2608.00196
next_step: skim
priority: medium
slack_ts: '1785986409.424459'
source: cs.DC - Distributed Computing
status: unread
title: A Portable and Versatile Limited-Memory BFGS Implementation in PETSc/TAO
---
# A Portable and Versatile Limited-Memory BFGS Implementation in PETSc/TAO
> 原文: [https://arxiv.org/abs/2608.00196](https://arxiv.org/abs/2608.00196)

arXiv:2608.00196v1 Announce Type: new
Abstract: The limited-memory BFGS (L-BFGS) Hessian update scheme is the critical kernel in many quasi-Newton optimization algorithms. The most common approach to implementing L-BFGS uses $2m$ sequential rank-1 updates as part of solving a linear system when there are $m$ history steps. The performance of this approach suffers when the latency of synchronization is significant, and its poor temporal locality increases the memory traffic when vectors do not fit in cache. The compact dense representation of L-BFGS results in an approach that has minimal synchronization latency and better temporal locality, but it requires an additional pass over the basis vectors and an additional basis that must be recomputed when the $B\_0$ matrix changes as in variable-metric methods. In the Portable Extensible Toolkit for Scientific Computation and the Toolkit for Advanced Optimization (PETSc/TAO), we have implemented an intermediate dense formulation of BFGS that retains most of the good characteristics of both the recursive and compact dense approaches. We report single-node performance tests of these implementations on the U.S. Department of Energy's Polaris and Frontier machines, testing both GPU-based and CPU-based computations.
