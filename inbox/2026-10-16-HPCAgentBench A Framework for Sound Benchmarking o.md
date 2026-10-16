---
title: "HPCAgent-Bench: A Framework for Sound Benchmarking of Code-Optimizing Agents, Harnesses, and Skills"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.20673
priority: low
status: unread
interest: medium
next_step: skim
---
# HPCAgent-Bench: A Framework for Sound Benchmarking of Code-Optimizing Agents, Harnesses, and Skills
> 原文: [https://arxiv.org/abs/2610.20673](https://arxiv.org/abs/2610.20673)

arXiv:2610.20673v1 Announce Type: new
Abstract: Coding agents are increasingly used to optimize code, but existing benchmarks fix one accelerator, programming model or harness, so they cannot isolate what each component contributes or show whether added skills and tools repay their cost. We present HPCAgent-Bench with 689 kernels in three tracks: loop-level optimization challenges, kernels extracted from HPC codes, and machine-learning models. The framework specifies each kernel once in NumPy, derives C and Fortran references, accepts submissions through a common C ABI or Python interface, and runs them on CPUs or GPUs, on one or multiple nodes. An external judge checks correctness on hidden fuzzed inputs and times each submission, closing paths agents use to exploit the testing system. We introduce two metrics for reporting results: \textit{intervention efficacy} measures an intervention, such as adding a tool, through paired runs on speedup, success rate and cost, and \textit{weighted token cost} reports input, cached-input and output tokens under explicit weights. Agents reach up to $4.2\times$ speedup over automatic parallelizers, and their optimizations transfer to another machine: $93$--$99\%$ of answers without device-specific code remain correct, and per-kernel speedups keep a rank correlation of $r\_s\ge0.84$. Across 40 matched setups, interventions significantly change speedup only twice but token cost by up to $3.0\times$. Because token weighting decides whether a saving is significant, we state the weights and release every token count as a standard for cost reporting. We provide the first comprehensive, broad and hardened benchmark for the sound evaluation of agentic optimization, with transparent cost metrics.
