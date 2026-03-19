---
title: "An Efficient Heterogeneous Co-Design for Fine-Tuning on a Single GPU"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.16428
priority: medium
status: unread
interest: medium
next_step: skim
---
# An Efficient Heterogeneous Co-Design for Fine-Tuning on a Single GPU
> 原文: [https://arxiv.org/abs/2603.16428](https://arxiv.org/abs/2603.16428)

arXiv:2603.16428v1 Announce Type: new
Abstract: Fine-tuning Large Language Models (LLMs) has become essential for domain adaptation, but its memory-intensive property exceeds the capabilities of most GPUs. To address this challenge and democratize LLM fine-tuning, we present SlideFormer, a novel system designed for single-GPU environments. Our innovations are: (1) A lightweight asynchronous engine that treats the GPU as a sliding window and overlaps GPU computation with CPU updates and multi-tier I/O. (2) A highly efficient heterogeneous memory management scheme significantly reduces peak memory usage. (3) Optimized Triton kernels to solve key bottlenecks and integrated advanced I/O. This collaborative design enables fine-tuning of the latest 123B+ models on a single RTX 4090, supporting up to 8x larger batch sizes and 6x larger models. In evaluations, SlideFormer achieves 1.40x to 6.27x higher throughput while roughly halving CPU/GPU memory usage compared to baselines, sustaining >95% peak performance on both NVIDIA and AMD GPUs.
