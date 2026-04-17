---
title: "Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.13327
priority: medium
status: unread
interest: medium
next_step: skim
---
# Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel
> 原文: [https://arxiv.org/abs/2604.13327](https://arxiv.org/abs/2604.13327)

arXiv:2604.13327v1 Announce Type: new
Abstract: Modern GPU workloads, especially large language model (LLM) inference, suffer from kernel launch overheads and coarse synchronization that limit inter-kernel parallelism. Recent megakernel techniques fuse multiple operators into a single persistent kernel to eliminate launch gaps and expose inter-kernel parallelism, but struggle to handle dynamic shapes and data-dependent computation in real workloads. We present Event Tensor, a unified compiler abstraction for dynamic megakernels. Event Tensor encodes dependencies between tiled tasks, and enables first-class support for both shape and data-dependent dynamism. Built atop this abstraction, our Event Tensor Compiler (ETC) applies static and dynamic scheduling transformations to generate high-performance persistent kernels. Evaluations show that ETC achieves state-of-the-art LLM serving latency while significantly reducing system warmup overhead.
