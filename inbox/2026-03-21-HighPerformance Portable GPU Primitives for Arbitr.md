---
interest: medium
link: https://arxiv.org/abs/2603.18695
next_step: skim
priority: medium
slack_ts: '1774060667.331239'
source: cs.DC - Distributed Computing
status: unread
title: High-Performance Portable GPU Primitives for Arbitrary Types and Operators
  in Julia
---
# High-Performance Portable GPU Primitives for Arbitrary Types and Operators in Julia
> 原文: [https://arxiv.org/abs/2603.18695](https://arxiv.org/abs/2603.18695)

arXiv:2603.18695v1 Announce Type: new
Abstract: Portable GPU frameworks such as Kokkos and RAJA reduce the burden of cross-architecture development but typically incur measurable overhead on fundamental parallel primitives relative to vendor-optimized libraries. We present KernelForge.jl, a Julia library that implements scan, mapreduce, and matrix-vector primitives through a two-layer portable architecture: KernelIntrinsics.jl provides backend-agnostic abstractions for warp-level shuffles, memory fences, and vectorized memory access, while KernelForge.jl builds high-performance algorithms exclusively on top of these interfaces. Evaluated on an NVIDIA A40 and an AMD MI300X, KernelForge.jl matches or exceeds CUB kernel execution time on scan and mapreduce on the A40, and matches cuBLAS throughput on matrix-vector operations across most tested configurations-demonstrating, as a proof of concept, that portable JIT-compiled abstractions can achieve vendor-level throughput without sacrificing generality.
