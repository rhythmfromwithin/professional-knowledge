---
interest: medium
link: https://arxiv.org/abs/2606.13723
next_step: skim
priority: medium
slack_ts: '1781500246.024079'
source: cs.CV - Computer Vision
status: unread
title: 'Morphology-Aware Sample Assignment: Overcoming IoU Insensitivity for Surface
  Defect Detection'
---
# Morphology-Aware Sample Assignment: Overcoming IoU Insensitivity for Surface Defect Detection
> 原文: [https://arxiv.org/abs/2606.13723](https://arxiv.org/abs/2606.13723)

arXiv:2606.13723v1 Announce Type: new
Abstract: Intersection-over-Union (IoU), as a pivotal metric for evaluating the spatial alignment between candidate proposals and ground-truth annotations, directly determines the quality of positive sample sets and the training efficacy of visual detection models. Through theoretical modeling and analysis, we uncover a non-sensitive region on the IoU response curve, within which samples yield nearly identical IoU scores despite distinct geometric overlaps. To overcome this limitation, we introduce a set of morphological similarity metrics covering area, shape, and aspect ratio, to refine the positive sample assignment process, thereby ensuring more discriminative and reliable matching. A supplementary matching score is derived via mean-based aggregation of these multidimensional similarities, compensating for the intrinsic limitation of IoU in representing structural correspondence. Theoretically, incorporating morphological similarity reshapes the response distribution of the matching function, yielding both effective directional gradients and polygon-like iso-response contours, which tightly confine high-response regions around each ground-truth instance and substantially enhance the precision of positive sample selection. Experiments based on the YOLOv9 framework demonstrate consistent performance gains on both NEUDET and GC10- DET datasets. Notably, the proposed approach is fully plug-and-play and incurs zero additional inference overhead, thereby ensuring deployment efficiency for industrial visual inspection.
