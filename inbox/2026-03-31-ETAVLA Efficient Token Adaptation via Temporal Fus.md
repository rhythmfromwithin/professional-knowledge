---
interest: medium
link: https://arxiv.org/abs/2603.25766
next_step: skim
priority: medium
slack_ts: '1775014233.000139'
source: cs.RO - Robotics
status: unread
title: 'ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification
  for Vision-Language-Action Models'
---
# ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2603.25766](https://arxiv.org/abs/2603.25766)

arXiv:2603.25766v1 Announce Type: new
Abstract: The integration of Vision-Language-Action (VLA) models into autonomous driving systems offers a unified framework for interpreting complex scenes and executing control commands. However, the necessity to incorporate historical multi-view frames for accurate temporal reasoning imposes a severe computational burden, primarily driven by the quadratic complexity of self-attention mechanisms in Large Language Models (LLMs). To alleviate this bottleneck, we propose ETA-VLA, an Efficient Token Adaptation framework for VLA models. ETA-VLA processes the past $n$ frames of multi-view images and introduces a novel Intra-LLM Sparse Aggregator (ILSA). Drawing inspiration from human driver attention allocation, ILSA dynamically identifies and prunes redundant visual tokens guided by textual queries and temporal consistency. Specifically, we utilize a text-guided scoring mechanism alongside a diversity-preserving sparsification strategy to select a sparse subset of critical tokens, ensuring comprehensive awareness of the driving scene. Extensive experiments on the NAVSIM v2 demonstrate that ETA-VLA achieves driving performance comparable to state-of-the-art baselines while reducing computational FLOPs by approximately 32\%. Notably, our method prunes 85% of visual tokens and reduces inference FLOPs by 61\%, but still retaining 94% of the original accuracy on the NAVSIM v2 benchmark.
