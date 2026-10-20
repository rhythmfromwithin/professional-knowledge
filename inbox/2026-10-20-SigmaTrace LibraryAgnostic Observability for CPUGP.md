---
title: "SigmaTrace: Library-Agnostic Observability for CPU/GPU-Initiated RDMA Communication"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.24328
priority: medium
status: unread
interest: medium
next_step: skim
---
# SigmaTrace: Library-Agnostic Observability for CPU/GPU-Initiated RDMA Communication
> 原文: [https://arxiv.org/abs/2610.24328](https://arxiv.org/abs/2610.24328)

arXiv:2610.24328v1 Announce Type: new
Abstract: RDMA networking enables low-latency, high-bandwidth communication on large systems. Despite its adoption, however, observability is lacking. Existing tools target specific communication libraries or only report aggregated data, missing per-operation behavior. The gap is widest for GPU-initiated networking, whose in-kernel RDMA operations are invisible to the host.
We present SigmaTrace, a library-agnostic RDMA profiling framework providing fine-grained, per-operation visibility for CPU and GPU-initiated networking. It traces operations at the libibverbs/mlx5dv layers, the common denominator beneath communication libraries on InfiniBand and RoCE, and employs a low-overhead memory interposition technique that, to our knowledge, gives the first observability into GPU-initiated RDMA without source patching or binary instrumentation.
Host-side tracing adds 1.3% overhead on NCCL AllReduce at 128 GPUs and under 2% on RCCL at 1024 GPUs. On a persistent-kernel BFS and Mixture-of-Experts inference, SigmaTrace exposes an in-kernel barrier spread and 2.13x inter-node traffic skew invisible to existing profilers.
