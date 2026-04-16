---
interest: medium
link: https://arxiv.org/abs/2604.12083
next_step: skim
priority: medium
slack_ts: '1776310490.146159'
source: cs.DC - Distributed Computing
status: unread
title: Accelerating Microswimmer Simulations via a Heterogeneous Pipelined Parallel-in-Time
  Framework
---
# Accelerating Microswimmer Simulations via a Heterogeneous Pipelined Parallel-in-Time Framework
> 原文: [https://arxiv.org/abs/2604.12083](https://arxiv.org/abs/2604.12083)

arXiv:2604.12083v1 Announce Type: new
Abstract: Simulating large-scale microswimmer dynamics in viscous fluid poses significant challenges due to the coupled high spatial and temporal complexity. Conventional high-performance computing (HPC) methods often address these two dimensions in isolation, leaving a critical gap for synergistic acceleration. This paper introduces a heterogeneous CPU--GPU computing framework specifically optimized for the long-time simulation of filamentous microswimmers in viscous fluid. We propose a two-level parallelization strategy: (1) high-intensity GPU kernels to resolve the quadratic spatial interactions given by the Method of Regularized Stokeslets (MRS), and (2) a distributed MPI-GPU pipelined Parareal architecture to exploit temporal concurrency. By mapping the asynchronous pipeline onto multiple GPU devices, our framework effectively overlaps coarse and fine propagators, overcoming the serial bottlenecks of traditional Parareal method. Furthermore, we employ a GPU-optimized numerical routine for computing the matrix square root arising in the numerical scheme of the filamentous microswimmer simulations. Theoretical analysis of the efficiency improvement of the pipelined Parareal is presented. Numerical experiments demonstrate that the proposed framework achieves order-of-magnitude speedups over CPU-only methods, providing a scalable pathway for simulating complex emergent behaviors in large-scale biology and physics systems.
