---
interest: medium
link: https://arxiv.org/abs/2609.10572
next_step: skim
priority: medium
slack_ts: '1789100118.307089'
source: cs.CV - Computer Vision
status: unread
title: Rethinking Handwritten Character Recognition
---
# Rethinking Handwritten Character Recognition
> 原文: [https://arxiv.org/abs/2609.10572](https://arxiv.org/abs/2609.10572)

arXiv:2609.10572v1 Announce Type: new
Abstract: Non-Latin handwritten character recognition (HCR) remains understudied. Dominant methods consider it as generic image classification, which uses model scale to implicitly learn stroke structure. Structural-prior efficiency---the principle that explicitly encoding script-geometric regularities as architectural inductive biases can be both more accurate and require fewer parameters. We introduce GraphemeNet, a unified multi-script architecture, governed by two orthogonal binary axes. Axis 1 operationalises stroke-level geometric regularity via Persistent Scaffold Injection (PSI): a script-specific asymmetric convolution injects a stroke scaffold as a weighted residual at every encoder stage, continuously anchoring learned features to script geometry---distinct from skip connections, auxiliary losses, or attention reweighting. Axis 2 selects between global average pooling with gated fusion and cross-scale attention with a Stroke Topology Module (STM), depending on whether glyph discrimination requires spatial relational reasoning. A Linear Capsule Routing (LCR) with $O(n)$ routing is shared universally. On fourteen benchmarks across eight writing systems, the architecture generalises with only scaffold and decoder topology varying per script, consistently challenging, outperforming published baselines, and establishing structural-prior efficiency as a broadly applicable principle for multi-script HCR.
