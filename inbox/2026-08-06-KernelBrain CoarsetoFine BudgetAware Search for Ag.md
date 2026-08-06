---
title: "KernelBrain: Coarse-to-Fine, Budget-Aware Search for Agentic GPU Kernel Optimization"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.02611
priority: medium
status: unread
interest: medium
next_step: skim
---
# KernelBrain: Coarse-to-Fine, Budget-Aware Search for Agentic GPU Kernel Optimization
> 原文: [https://arxiv.org/abs/2608.02611](https://arxiv.org/abs/2608.02611)

arXiv:2608.02611v1 Announce Type: new
Abstract: Automating GPU kernel optimization remains difficult in practice: generated variants can violate correctness constraints, runtime measurements are noisy, and search often stalls early. We present a practical optimization agent that combines LLM-guided mutation, adaptive resource allocation, policy-gated evaluation, and profiler-informed diagnosis. The system screens many candidates with low-cost evaluation and allocates higher-fidelity budget only to promising survivors to optimize and evolve GPU kernels. On important Triton kernel generation tasks, this design improves both kernel quality and search efficiency, reaching 0.88x-6.72x speedup over PyTorch and up to 1.4x speedup over the state-of-the-art kernel agent, with up to 48% lower optimization time.
