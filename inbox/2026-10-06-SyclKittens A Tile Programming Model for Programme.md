---
interest: medium
link: https://arxiv.org/abs/2610.04277
next_step: skim
priority: medium
slack_ts: '1791351192.073139'
source: cs.DC - Distributed Computing
status: unread
title: 'SyclKittens: A Tile Programming Model for Programmers and Coding Agents on
  Intel GPUs'
---
# SyclKittens: A Tile Programming Model for Programmers and Coding Agents on Intel GPUs
> 原文: [https://arxiv.org/abs/2610.04277](https://arxiv.org/abs/2610.04277)

arXiv:2610.04277v1 Announce Type: new
Abstract: New AI accelerators arrive before the kernels that make them fast, because peak kernel performance requires architecture-specific expertise in operand pipelines and data-movement techniques. Coding agents can now write, compile, and tune kernels on their own, so they could greatly accelerate kernel development and optimization. What agents produce depends on the interfaces they are given. These interfaces may expose a machine's raw capabilities or encode the known-good methods for exploiting its hardware features efficiently. We test the performance impact of these two interfaces on Intel GPUs through controlled experiments with three coding models on three kernels. With raw SYCL and execution feedback, Opus 4.8, the strongest of the three models tested, writes a single-GPU GEMM kernel reaching only 57.5% of Intel's tuned oneDNN library. We present SyclKittens, a hardware-aware tile programming model for Intel GPUs that encodes these known-good methods, so its operations place operands in matrix-engine layouts, prefetch through the L1 cache, and communicate over the fabric that links GPU stacks into a node. With SyclKittens under the same agent, task, and feedback budget, the agent reaches 82.1%, showing that encoded methods turn hardware capabilities into performance. Workload-specific policies stay programmable, and engineers and agents jointly refine these schedules in SyclKittens to build a kernel suite that reaches ~96% of oneDNN in geometric mean across GEMM shapes. The suite runs Llama-3.1-8B inference 1.59x faster than torch.compile on one GPU and up to 2.91x faster than a matched multi-GPU decode path on Intel's oneCCL. SyclKittens is open source and available at https://github.com/intel/SyclKittens.
