---
interest: medium
link: https://arxiv.org/abs/2609.30270
next_step: skim
priority: high
slack_ts: '1790659450.833179'
source: cs.LG - Machine Learning
status: unread
title: 'HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device,
  Edge, and Cloud LLM Inference'
---
# HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device, Edge, and Cloud LLM Inference
> 原文: [https://arxiv.org/abs/2609.30270](https://arxiv.org/abs/2609.30270)

arXiv:2609.30270v1 Announce Type: new
Abstract: On-device inference with small language models keeps user data local, works offline, and incurs no per-query cost, so the on-device tier is preferred when it is adequate. It is thermally constrained, however, and I find the constraint is sharper than a slowdown: on a flagship Snapdragon device, sustained on-device generation destabilizes the GPU inference runtime, which crashes or silently wedges after a few consecutive queries. The failure lies in the current toolchain (OpenCL kernel compilation and long-prompt prefill on the mobile GPU), recurs even when the device is cool, and is worst for long generations. Multi-tier routers across on-device, edge, and cloud models can relieve this pressure, but existing routers are thermal-blind and typically evaluated in simulation or on non-mobile hardware. I present HybridInfer, a thermal-aware reinforcement-learning router for a three-tier hierarchy (on-device Llama 3.2 3B, edge Llama 3.1 8B with retrieval, cloud GPT-4o) that uses the phone's thermal headroom and a query-complexity estimate as state and selects a tier by an offline-trained Q-learning policy. Its reward trades quality against latency, cost, and a thermal penalty, plus a locality bonus crediting on-device execution. I show this bonus is a precondition for thermal-aware routing: without it the optimal policy offloads every query. On a real Android benchmark of 210 prompts, the learned router attains significantly higher quality than two hand-tuned heuristics (paired Wilcoxon, p < 0.02) at the lowest cost of any adaptive condition. Always-on-device conditions match per-query quality on servable queries but are three to six times slower and fail on long queries, so routing wins on latency, reliability, and coverage rather than quality. To my knowledge this is the first use of on-device thermal headroom to select among LLM inference tiers of differing capability on real hardware.
