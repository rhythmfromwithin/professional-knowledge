---
title: "From Inheritance to Saturation: Disentangling the Evolution of Visual Redundancy for Architecture-Aware MLLM Inference Acceleration"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.16462
priority: medium
status: unread
interest: medium
next_step: skim
---
# From Inheritance to Saturation: Disentangling the Evolution of Visual Redundancy for Architecture-Aware MLLM Inference Acceleration
> 原文: [https://arxiv.org/abs/2604.16462](https://arxiv.org/abs/2604.16462)

arXiv:2604.16462v1 Announce Type: new
Abstract: High-resolution Multimodal Large Language Models (MLLMs) face prohibitive computational costs during inference due to the explosion of visual tokens. Existing acceleration strategies, such as token pruning or layer sparsity, suffer from severe "backbone dependency", performing well on Vicuna or Mistral architectures (e.g., LLaVA) but causing significant performance degradation when transferred to architectures like Qwen. To address this, we leverage truncated matrix entropy to uncover a universal three-stage inference lifecycle, decoupling visual redundancy into universal Intrinsic Visual Redundancy (IVR) and architecture-dependent Secondary Saturation Redundancy (SSR). Guided by this insight, we propose HalfV, a framework that first mitigates IVR via a unified pruning strategy and then adaptively handles SSR based on its specific manifestation. Experiments demonstrate that HalfV achieves superior efficiency-performance trade-offs across diverse backbones. Notably, on Qwen25-VL, it retains 96.8\% performance at a 4.1$\times$ FLOPs speedup, significantly outperforming state-of-the-art baselines. Our code is available at https://github.com/civilizwa/HalfV.
