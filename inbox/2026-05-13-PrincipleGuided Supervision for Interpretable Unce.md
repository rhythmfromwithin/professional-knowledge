---
interest: medium
link: https://arxiv.org/abs/2605.10984
next_step: skim
priority: medium
slack_ts: '1778644967.485769'
source: cs.CV - Computer Vision
status: unread
title: Principle-Guided Supervision for Interpretable Uncertainty in Medical Image
  Segmentation
---
# Principle-Guided Supervision for Interpretable Uncertainty in Medical Image Segmentation
> 原文: [https://arxiv.org/abs/2605.10984](https://arxiv.org/abs/2605.10984)

arXiv:2605.10984v1 Announce Type: new
Abstract: Uncertainty quantification complements model predictions by characterizing their reliability, which is essential for high-stakes decision making such as medical image segmentation. However, most existing methods reduce uncertainty to a scalar confidence estimate, leaving its spatial distribution semantically underconstrained. In this work, we focus on uncertainty interpretability, namely, whether estimated uncertainty behaves in a human-understandable manner with respect to sources of ambiguity. We identify three perception-aligned principles requiring the spatial distribution of uncertainty to reflect: (1) image contrast between structures, (2) severity of image corruption, and (3) geometric complexity in anatomical structures. Accordingly, we develop a principle-guided uncertainty supervision framework (PriUS) based on evidential learning, in which the corresponding supervision objectives are explicitly enforced during training. We further introduce quantitative metrics to measure the consistency between predicted uncertainty and image attributes that induce ambiguity. Experiments on ACDC, ISIC, and WHS datasets showed that, compared with state-of-the-art methods, PriUS produced more consistent uncertainty estimates while maintaining competitive segmentation performance.
