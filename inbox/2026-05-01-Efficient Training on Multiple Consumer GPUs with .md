---
interest: medium
link: https://arxiv.org/abs/2604.27085
next_step: skim
priority: medium
slack_ts: '1777692909.348369'
source: cs.DC - Distributed Computing
status: unread
title: Efficient Training on Multiple Consumer GPUs with RoundPipe
---
# Efficient Training on Multiple Consumer GPUs with RoundPipe
> 原文: [https://arxiv.org/abs/2604.27085](https://arxiv.org/abs/2604.27085)

arXiv:2604.27085v1 Announce Type: new
Abstract: Fine-tuning Large Language Models (LLMs) on consumer-grade GPUs is highly cost-effective, yet constrained by limited GPU memory and slow PCIe interconnects. Pipeline parallelism combined with CPU offloading mitigates these hardware bottlenecks by reducing communication overhead. However, existing PP schedules suffer from an inherent limitation termed the weight binding issue. Binding uneven model stages (e.g., the LM head is large) to GPUs limits the pipeline's throughput to that of the GPU with the heaviest load, leading to severe pipeline bubbles.
In this paper, we propose RoundPipe, a novel pipeline schedule that breaks the weight binding constraint on consumer GPU servers. RoundPipe treats GPUs as a pool of stateless execution workers and dynamically dispatches computation stages across devices in a round-robin manner, achieving a near-zero-bubble pipeline. To ensure training correctness and system efficiency, RoundPipe integrates a priority-aware transfer scheduling engine, a fine-grained distributed event-based synchronization protocol, and an automated layer partitioning algorithm. Evaluations on an 8$\times$ RTX 4090 server demonstrate that RoundPipe achieves 1.48--2.16$\times$ speedups over state-of-the-art baselines when fine-tuning 1.7B to 32B models. Remarkably, RoundPipe enables LoRA fine-tuning of the Qwen3-235B model with 31K sequence length on a single server.
RoundPipe is publicly available as an open-source Python library with comprehensive documentation.
