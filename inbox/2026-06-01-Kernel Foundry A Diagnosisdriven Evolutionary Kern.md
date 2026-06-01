---
title: "Kernel Foundry: A Diagnosis-driven Evolutionary Kernel Optimizer with Multi-Experts"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.30359
priority: low
status: unread
interest: medium
next_step: skim
---
# Kernel Foundry: A Diagnosis-driven Evolutionary Kernel Optimizer with Multi-Experts
> 原文: [https://arxiv.org/abs/2605.30359](https://arxiv.org/abs/2605.30359)

arXiv:2605.30359v1 Announce Type: new
Abstract: Generating high-performance GPU kernels remains challenging due to the need for both correctness and hardware-aware optimization. While large language models (LLMs) show promise in code generation, they often fail to produce kernels that are both correct and efficient.
We propose Kernel Foundry, a diagnosis-driven evolutionary framework for automatic GPU kernel optimization. Our method combines expert-guided, retrieval-augmented initialization with a multi-island evolutionary search, where candidate kernels are iteratively refined using structured diagnostic feedback. A centralized experience library accumulates reusable optimization knowledge to guide subsequent evolution, while explicit mechanisms prevent cheating behaviors that bypass kernel-level computation.
Experiments on KernelBench show that our method consistently improves both correctness and performance over strong baselines, achieving up to 100% correctness on Level~2.
