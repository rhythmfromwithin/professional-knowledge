---
title: "Securing Multimodal AI through Internal Information Decomposition"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2607.21600
priority: high
status: unread
interest: medium
next_step: skim
---
# Securing Multimodal AI through Internal Information Decomposition
> 原文: [https://arxiv.org/abs/2607.21600](https://arxiv.org/abs/2607.21600)

arXiv:2607.21600v1 Announce Type: new
Abstract: Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards. This motivates using cross-modal consistency as a detection signal rather than inspecting each modality in isolation. Our key observation is that benign inputs induce compatible predictive behavior from text-only and vision-only reasoning that stabilizes when fused, whereas adversarial manipulation disrupts this consistency, causing abnormal multimodal behavior. Existing defenses that examine raw inputs or outputs overlook this internal fusion process, rendering them brittle and computationally expensive. We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency. Unlike approaches that rely on scalar confidence metrics, FlowGuard derives FlowVectors inspired by Partial Information Decomposition that quantify cross-modal redundancy, synergy, and modality-specific dominance, capturing whether fused multimodal predictions remain aligned with unimodal semantic evidence. In a one-class classification problem trained solely on benign data, FlowGuard reduces Attack Success Rates from >90% to <15% on unseen attacks, with <3% utility loss and up to a 6 times latency reduction. Our results demonstrate that monitoring cross-modal consistency offers an efficient and effective defense for multimodal reasoning.
