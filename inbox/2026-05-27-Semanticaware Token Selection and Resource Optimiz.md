---
interest: medium
link: https://arxiv.org/abs/2605.26120
next_step: skim
priority: medium
slack_ts: '1780113868.500019'
source: cs.DC - Distributed Computing
status: unread
title: Semantic-aware Token Selection and Resource Optimization for Communication-efficient
  Split Federated Fine-tuning in Edge Intelligence
---
# Semantic-aware Token Selection and Resource Optimization for Communication-efficient Split Federated Fine-tuning in Edge Intelligence
> 原文: [https://arxiv.org/abs/2605.26120](https://arxiv.org/abs/2605.26120)

arXiv:2605.26120v1 Announce Type: new
Abstract: Deploying large Transformer-based vision models on resource-limited mobile devices at network edge is severely constrained by hardware limitations and dynamic wireless environments. While federated learning (FL) enables collaborative training without sharing raw data, strictly local fine-tuning of such massive models remains computationally prohibitive for edge devices. Split federated learning (SFL) alleviates this burden by offloading deep layers to the edge server, yet it suffers from heavy communication overhead when transmitting high-dimensional activation tokens. To address this bottleneck, we propose ST-SFLora, a semantic token-based split federated LoRA fine-tuning framework. We introduce a new metric, \emph{Semantic Transmission Efficiency} (STE), to balance semantic retention and transmission cost. Based on STE, we formulate a joint resource optimization problem that dynamically determines token selection, uplink bandwidth allocation, and transmit power under latency and energy constraints. The resulting mixed-integer nonconvex problem is efficiently solved via an alternating algorithm. Experiments on multiple benchmarks demonstrate that ST-SFLora achieves the lowest client-side resource consumption among baselines while delivering a favorable trade-off between communication efficiency and model performance.
