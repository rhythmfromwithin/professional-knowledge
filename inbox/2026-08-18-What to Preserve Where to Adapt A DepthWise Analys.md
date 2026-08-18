---
interest: medium
link: https://arxiv.org/abs/2608.13660
next_step: skim
priority: medium
slack_ts: '1787017194.459969'
source: cs.CV - Computer Vision
status: unread
title: 'What to Preserve, Where to Adapt: A Depth-Wise Analysis of Forgetting in Continual
  Gynecological Image Segmentation'
---
# What to Preserve, Where to Adapt: A Depth-Wise Analysis of Forgetting in Continual Gynecological Image Segmentation
> 原文: [https://arxiv.org/abs/2608.13660](https://arxiv.org/abs/2608.13660)

arXiv:2608.13660v1 Announce Type: new
Abstract: Medical image segmentation models are typically trained under the assumption that all data are available simultaneously. However, in clinical practice, datasets often arrive sequentially, requiring models to adapt continuously to evolving data distributions. We study this problem in gynecological image segmentation, where substantial heterogeneity across imaging modalities, anatomical structures, and annotation protocols creates a particularly challenging continual learning setting. Under these large distribution shifts, existing continual learning methods struggle to preserve previously learned knowledge, leading to catastrophic forgetting. To better understand forgetting in this setting, we investigate how different encoder--decoder regions influence segmentation performance and forgetting during continual gynecological segmentation. Through block-wise ablation analysis, we observe that ablating early encoder and late decoder regions results in the largest performance degradation, indicating that segmentation performance depends unevenly across the network hierarchy. Using controlled adaptation experiments, we further show that forgetting remains limited when updates are restricted to bottleneck-adjacent regions, but increases sharply once shallower encoders and decoders become trainable, even when only a small subset of parameters is updated. These findings suggest that forgetting in the encoder-decoder architecture is strongly influenced by where updates occur across network depth during continual learning. Full code and analysis pipelines will be made publicly available upon acceptance.
