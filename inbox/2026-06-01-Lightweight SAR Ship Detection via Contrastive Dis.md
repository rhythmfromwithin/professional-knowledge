---
title: "Lightweight SAR Ship Detection via Contrastive Distillation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.30380
priority: medium
status: unread
interest: medium
next_step: skim
---
# Lightweight SAR Ship Detection via Contrastive Distillation
> 原文: [https://arxiv.org/abs/2605.30380](https://arxiv.org/abs/2605.30380)

arXiv:2605.30380v1 Announce Type: new
Abstract: Deep convolutional and transformer-based detectors achieve strong performance for SAR ship detection but are often computationally prohibitive for real-time or onboard deployment. Lightweight models offer improved efficiency yet struggle to capture the complex structural relationships inherent in SAR backscatter. Most existing SAR knowledge-distillation approaches rely on feature or logit matching, which enforces localized activation similarity while neglecting the geometric relationships among object representations. We propose a Structured Unified Relational knowledGE distillation framework for SAR Ship detection (SURGE) that transfers relational geometry from a powerful teacher detector to a compact student detector using a contrastive InfoNCE objective in a shared projection embedding space. To the best of our knowledge, this work presents the first transformer-based SAR ship detector knowledge distillation framework in SAR domain. The framework is architecture-agnostic in the sense that it provides a common region-level distillation interface for two-stage, one-stage and transformer-based detectors without modifying their deployed architectures. Experiments on the SSDD and HRSID benchmarks demonstrate that the proposed method yields substantial improvements for two-stage detectors, achieving up to 6.2 mAP and 8.0 AP75 gains over baseline student and even surpassing teacher performance
