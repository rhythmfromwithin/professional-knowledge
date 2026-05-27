---
title: "Xe-Forge: Multi-Stage LLM-Powered Kernel Optimization for Intel GPU"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.26118
priority: medium
status: unread
interest: medium
next_step: skim
---
# Xe-Forge: Multi-Stage LLM-Powered Kernel Optimization for Intel GPU
> 原文: [https://arxiv.org/abs/2605.26118](https://arxiv.org/abs/2605.26118)

arXiv:2605.26118v1 Announce Type: new
Abstract: Porting deep learning algorithms to new hardware accelerators requires developers to repeatedly apply the same low-level optimizations -- quantization, memory access coalescing, tile size tuning, and architecture-specific workarounds -- to every Triton kernel in their code-base. This manual, repetitive effort is a major bottleneck: each kernel demands the same cycle of trial-and-error profiling against hardware constraints that vary across devices, yet the underlying optimization patterns remain largely consistent. We present Xe-Forge, a multi-stage LLM-powered pipeline that automates this process for Intel GPU. Given a functionally correct Triton kernel, the system applies up to nine optimization stages -- from algorithmic restructuring and operator fusion through block pointer modernization, GPU-specific tuning, and open-ended discovery -- each driven by a Chain-of-Verification-and-Refinement (CoVeR) agent that generates candidates, validates them on real hardware, and iterates on failures. A curated knowledge base encodes Intel GPU constraints (power-of-two warp counts, GRF modes, SLM sizing) that are absent from LLM training data, keeping the model within architecturally valid bounds. We evaluate Xe-Forge on 97 Level-2 KernelBench kernels and Flash Attention on the Intel Arc Pro B70, achieving a 1.17x geometric mean speedup over PyTorch eager with 67% of kernels improving, nine kernels exceeding 5x (up to 82x), and 2--13.3x speedups on Flash Attention across all tested configurations without regression -- demonstrating that structured domain knowledge with hardware-in-the-loop verification can systematically eliminate the repetitive porting effort that currently gates algorithm deployment on new accelerators.
