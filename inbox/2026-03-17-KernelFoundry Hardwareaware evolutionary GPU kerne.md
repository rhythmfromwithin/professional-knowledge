---
title: "KernelFoundry: Hardware-aware evolutionary GPU kernel optimization"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.12440
priority: medium
status: unread
interest: medium
next_step: skim
---
# KernelFoundry: Hardware-aware evolutionary GPU kernel optimization
> 原文: [https://arxiv.org/abs/2603.12440](https://arxiv.org/abs/2603.12440)

arXiv:2603.12440v1 Announce Type: new
Abstract: Optimizing GPU kernels presents a significantly greater challenge for large language models (LLMs) than standard code generation tasks, as it requires understanding hardware architecture, parallel optimization strategies, and performance profiling outputs. Most existing LLM-based approaches to kernel generation rely on simple prompting and feedback loops, incorporating hardware awareness only indirectly through profiling feedback. We introduce KernelFoundry, an evolutionary framework that efficiently explores the GPU kernel design space through three key mechanisms: (1) MAP-Elites quality-diversity search with kernel-specific behavioral dimensions to sustain exploration across diverse optimization strategies; (2) meta-prompt evolution, which co-evolves prompts with kernels to uncover task-specific optimization strategies, and (3) template-based parameter optimization to tune kernels to inputs and hardware. We evaluate this framework on KernelBench, robust-kbench, and custom tasks, generating SYCL kernels as a cross-platform GPU programming model and CUDA kernels for comparison to prior work. Our approach consistently outperforms the baseline methods, achieving an average speedup of 2.3x on KernelBench for SYCL. Moreover, KernelFoundry is implemented as a distributed framework with remote access to diverse hardware, enabling rapid benchmarking and featuring a flexible user input layer that supports kernel generation for a wide range of real-world use cases beyond benchmarking.
