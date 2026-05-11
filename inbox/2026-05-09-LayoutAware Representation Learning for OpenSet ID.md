---
interest: medium
link: https://arxiv.org/abs/2605.05215
next_step: skim
priority: medium
slack_ts: '1778472601.693579'
source: cs.CV - Computer Vision
status: unread
title: Layout-Aware Representation Learning for Open-Set ID Fraud Discovery
---
# Layout-Aware Representation Learning for Open-Set ID Fraud Discovery
> 原文: [https://arxiv.org/abs/2605.05215](https://arxiv.org/abs/2605.05215)

arXiv:2605.05215v1 Announce Type: new
Abstract: Identity-document fraud detection is not a stationary binary classification problem. Adaptive attackers modify templates and fabrication pipelines, making historical fraud labels stale, and successful forgeries recur at scale as coherent campaigns. We therefore study layout-aware representation learning for open-set fraud discovery rather than only closed-set classification. We adapt DINOv3 to the document domain via context-aware SimMIM fine-tuning and supervised metric learning with composite loss that encourages inter-class separability and intra-class compactness. The model is trained with U.S. IDs only. With a lightweight MLP and softmax classifier, the embedding achieves 99.83% layout classification accuracy on Canadian layouts. Moreover, on a dataset of 20,448 Canadian IDs, embedding-space analysis surfaces 276 adaptive physical-fraud cases, including 222 not surfaced by incumbent detectors. The embedding supports similarity-based expansion from a single confirmed seed to additional related cases not linked by conventional metadata graphs. The layout-aware document embeddings provide a production-aligned basis for discovering novel and campaign-scale fraud under distribution shift.
