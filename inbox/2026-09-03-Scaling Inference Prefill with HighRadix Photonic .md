---
title: "Scaling Inference Prefill with High-Radix Photonic Interconnects"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.01821
priority: medium
status: unread
interest: medium
next_step: skim
---
# Scaling Inference Prefill with High-Radix Photonic Interconnects
> 原文: [https://arxiv.org/abs/2609.01821](https://arxiv.org/abs/2609.01821)

arXiv:2609.01821v1 Announce Type: new
Abstract: With the rise of inference as today's dominant AI workload, the industry is transitioning to high-bandwidth photonic interconnects to meet the large scale-up requirements of increasingly complex Mixture-of-Experts (MoE) models. This paper quantifies the benefits of 3D-integrated photonic interconnects for inference prefill by analyzing tradeoffs between high-concurrency throughput for Large Language Model (LLM) chat and the large context windows typically required for reasoning and agentic AI. We simulate three MoE models: short context (1K--8K tokens), medium context (128K tokens), and long context (1M tokens). We evaluate this workload across existing copper-based GPU systems and one with high bandwidth integrated photonics. We show 2.1--3.2x latency improvements in the stressed high-batch regimes and 2.8--5.8x improvements over baselines in communication-limited configurations. 3D photonics enable the 1152-GPU footprint required to lower time-to-first-token, yielding 2.2--4.5x speedups across production-grade platforms when electrical systems cross their inherent scale-up-pod limits.
