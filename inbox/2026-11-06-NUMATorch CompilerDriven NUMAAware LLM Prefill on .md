---
interest: medium
link: https://arxiv.org/abs/2611.07105
next_step: skim
priority: medium
slack_ts: '1794116480.760639'
source: cs.DC - Distributed Computing
status: unread
title: 'NUMA-Torch: Compiler-Driven NUMA-Aware LLM Prefill on Multi-Socket CPUs'
---
# NUMA-Torch: Compiler-Driven NUMA-Aware LLM Prefill on Multi-Socket CPUs
> 原文: [https://arxiv.org/abs/2611.07105](https://arxiv.org/abs/2611.07105)

arXiv:2611.07105v1 Announce Type: new
Abstract: For sufficiently large transformer-based Large Language Models (LLMs), whose parameters cannot be retained in on-chip caches, prefill throughput on multi-socket CPUs is often limited by sustainable DRAM bandwidth rather than peak floating-point throughput. In the standard PyTorch compilation (i.e., TorchInductor) path, model weights are allocated without considering the Non-Uniform Memory Access (NUMA) topology: specifically, the affinity between memory banks and compute cores is disregarded. This causes a substantial fraction of weight accesses to traverse the inter-socket interconnect, severely degrading the effective memory bandwidth available to each socket. We address this bottleneck through a compiler-level solution that makes TorchInductor NUMA-aware. Treating each NUMA socket as an independent tensor-parallel partition, we introduce NUMA-aware Tensor Parallelism (NUMA-TP). This approach transparently shards weights across sockets and schedules compute kernels such that thread pools and memory allocations remain strictly local to their respective sockets using CPU affinity. We evaluate the approach on GPT-2 (117M, 345M, 762M) and BERT (Small, Large), which exercise standard multi-head attention and MLP, as well as Gemma 3 270M, which combines Multi-Query Attention with a GeGLU-gated MLP. By strictly enforcing data locality, our approach successfully mitigates cross-socket traffic, achieving prefill speedups of up to 2.63x on a dual-socket Haswell platform, up to 1.87x on a dual-socket Cascade Lake platform, and up to 2.27x on a four-socket Haswell-EX platform.
