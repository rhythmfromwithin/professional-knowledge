---
interest: medium
link: https://arxiv.org/abs/2607.07862
next_step: skim
priority: medium
slack_ts: '1783827429.261899'
source: cs.DC - Distributed Computing
status: unread
title: 'CTA-Pipelining: A Latency-Oriented Spatial Scaling Method for Multi-GPU Systems'
---
# CTA-Pipelining: A Latency-Oriented Spatial Scaling Method for Multi-GPU Systems
> 原文: [https://arxiv.org/abs/2607.07862](https://arxiv.org/abs/2607.07862)

arXiv:2607.07862v1 Announce Type: new
Abstract: The evolution of compute infrastructure has transformed multi-GPU systems into tightly integrated shared-memory structures. However, current software still mostly treats these coherent interconnects simply as high-speed networks. Simultaneously, the demand for serving Large Language Models under latency constraints has shifted GPU workload optimization from being throughput-driven to latency-bound, necessitating latency-oriented scaling methods beyond Tensor Parallelism (TP).
Thus, we introduce CTA-pipelining, an execution paradigm designed to exploit shared-memory multi-GPU systems. As a latency-oriented spatial scaling technique, CTA-pipelining leverages dependencies at the Cooperative Thread Array level, enabling concurrent execution of dependent kernels across GPUs. We demonstrate its capability using CUTLASS, cuBLAS, and NCCL libraries on 8-GPU H200 and B200 systems. Results show on 2-layer GEMM, representing the MLP operation, CTA-pipelining reduces latency by up to 31.8% compared to micro-batching, and 29.6% compared to TP. It can also be combined with TP as an orthogonal scaling dimension to further push the latency boundary.
