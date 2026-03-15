---
interest: medium
link: https://arxiv.org/abs/2603.08800
next_step: skim
priority: medium
slack_ts: '1773544824.384399'
source: cs.CV - Computer Vision
status: unread
title: 'Granulon: Awakening Pixel-Level Visual Encoders with Adaptive Multi-Granularity
  Semantics for MLLM'
---
# Granulon: Awakening Pixel-Level Visual Encoders with Adaptive Multi-Granularity Semantics for MLLM
> 原文: [https://arxiv.org/abs/2603.08800](https://arxiv.org/abs/2603.08800)

arXiv:2603.08800v1 Announce Type: new
Abstract: Recent advances in multimodal large language models largely rely on CLIP-based visual encoders, which emphasize global semantic alignment but struggle with fine-grained visual understanding. In contrast, DINOv3 provides strong pixel-level perception yet lacks coarse-grained semantic abstraction, leading to limited multi-granularity reasoning. To address this gap, we propose Granulon, a novel DINOv3-based MLLM with adaptive granularity augmentation. Granulon introduces a text-conditioned granularity Controller that dynamically adjusts the visual abstraction level according to the semantic scope of the textual input, and an Adaptive Token Aggregation module that performs granularity-guided pooling and relation-aware clustering to produce compact, semantically rich visual tokens. This design enables unified "pixel-to-fine-to-coarse" reasoning within a single forward pass. Extensive and interpretable experiments demonstrate that Granulon improves accuracy by ~30% and reduces hallucination by ~20%, outperforming all visual encoders under identical settings.
