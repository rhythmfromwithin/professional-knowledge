---
interest: medium
link: https://arxiv.org/abs/2608.24959
next_step: skim
priority: medium
slack_ts: '1787914963.989029'
source: cs.RO - Robotics
status: unread
title: 'GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model'
---
# GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model
> 原文: [https://arxiv.org/abs/2608.24959](https://arxiv.org/abs/2608.24959)

arXiv:2608.24959v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models encode visual observations as flat 2D patch tokens that carry no intrinsic geometric structure, and augmenting them with dense monocular depth injects per-pixel scalar values that encode neither surface orientation nor geometric confidence. This leaves the policy with limited structured spatial reasoning for action prediction. We propose GaussVLA, a Mamba-based VLA that incorporates two custom modules: Gaussian Spatial Tokenizer (GST) to lift frozen semantic and depth features into compact 3D Gaussian tokens, pools geometrically salient regions with learned queries, and \emph{Depth-Aware Chain-of-Thought (DA-CoT)} that performs structured, non-autoregressive geometric reasoning under language and flow-time conditioning. Across both simulation and real-world evaluations, GaussVLA demonstrates strong spatial-manipulation performance while remaining parameter-efficient. On LIBERO, it achieves 93.5% average success and 100.0% success on the Spatial suite with only 200M parameters, improving over SpatialVLA by 19.7% relative average success while remaining significantly more parameter-efficient.
