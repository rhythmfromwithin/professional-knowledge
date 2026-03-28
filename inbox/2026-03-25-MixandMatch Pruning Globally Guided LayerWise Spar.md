---
interest: medium
link: https://arxiv.org/abs/2603.20280
next_step: skim
priority: medium
slack_ts: '1774666184.403539'
source: cs.CV - Computer Vision
status: unread
title: 'Mix-and-Match Pruning: Globally Guided Layer-Wise Sparsification of DNNs'
---
# Mix-and-Match Pruning: Globally Guided Layer-Wise Sparsification of DNNs
> 原文: [https://arxiv.org/abs/2603.20280](https://arxiv.org/abs/2603.20280)

arXiv:2603.20280v1 Announce Type: new
Abstract: Deploying deep neural networks (DNNs) on edge devices requires strong compression with minimal accuracy loss. This paper introduces Mix-and-Match Pruning, a globally guided, layer-wise sparsification framework that leverages sensitivity scores and simple architectural rules to generate diverse, high-quality pruning configurations. The framework addresses a key limitation that different layers and architectures respond differently to pruning, making single-strategy approaches suboptimal. Mix-and-Match derives architecture-aware sparsity ranges, e.g., preserving normalization layers while pruning classifiers more aggressively, and systematically samples these ranges to produce ten strategies per sensitivity signal (magnitude, gradient, or their combination). This eliminates repeated pruning runs while offering deployment-ready accuracy-sparsity trade-offs. Experiments on CNNs and Vision Transformers demonstrate Pareto-optimal results, with Mix-and-Match reducing accuracy degradation on Swin-Tiny by 40% relative to standard single-criterion pruning. These findings show that coordinating existing pruning signals enables more reliable and efficient compressed models than introducing new criteria.
