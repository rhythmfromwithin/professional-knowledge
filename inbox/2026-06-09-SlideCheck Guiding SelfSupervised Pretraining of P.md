---
interest: medium
link: https://arxiv.org/abs/2606.07590
next_step: skim
priority: medium
slack_ts: '1780978313.449999'
source: cs.CV - Computer Vision
status: unread
title: 'SlideCheck: Guiding Self-Supervised Pretraining of Pathology Foundation Models
  via Dataset Distributions'
---
# SlideCheck: Guiding Self-Supervised Pretraining of Pathology Foundation Models via Dataset Distributions
> 原文: [https://arxiv.org/abs/2606.07590](https://arxiv.org/abs/2606.07590)

arXiv:2606.07590v1 Announce Type: new
Abstract: Pathology foundation models are pretrained on large streams of WSI-derived patches, while supervision during data construction is often slide-level, sparse, or heterogeneous. This mismatch makes it difficult to understand and control which biological patterns enter the pretraining data. We propose SlideCheck, a lightweight pretraining data guidance tool built on frozen pathology foundation model patch features. Rather than serving as a standalone patch diagnostic model, SlideCheck provides explicit abnormality and malignancy scores for organizing, filtering, and auditing pathology pretraining data. SlideCheck uses a dual-head MLP to separately model broad abnormal morphology and malignant evidence. A regularized feature-space scorer provides a supervised anchor for patch-level evidence estimation, while score-attention agreement combines patch scores with WSI-level MIL attention to mine high-confidence pseudo labels. The same scores are then used to construct broad-positive ViT pretraining subsets, where a patch is selected if either abnormality or malignancy evidence exceeds a threshold. Experiments show that SlideCheck-defined data distributions influence the downstream behavior of self-supervised ViT pretraining, indicating that biological composition is an important controllable factor in pathology foundation model development. Curated subsets can approach full-data performance, suggesting that explicitly scored patch pools may support more efficient and auditable pretraining data construction. These findings position SlideCheck as a data guidance and auditing layer for transforming large, undifferentiated patch pools into controllable and reusable pretraining datasets.
