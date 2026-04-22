---
interest: medium
link: https://arxiv.org/abs/2604.15451
next_step: skim
priority: medium
slack_ts: '1776828595.620639'
source: cs.CV - Computer Vision
status: unread
title: Weak-to-Strong Knowledge Distillation Accelerates Visual Learning
---
# Weak-to-Strong Knowledge Distillation Accelerates Visual Learning
> 原文: [https://arxiv.org/abs/2604.15451](https://arxiv.org/abs/2604.15451)

arXiv:2604.15451v1 Announce Type: new
Abstract: Large-scale visual learning is increasingly limited by training cost. Existing knowledge distillation methods transfer from a stronger teacher to a weaker student for compression or final-accuracy improvement. We instead investigate distillation to accelerate the training of strong students. We propose a generalizable plug-and-play recipe that freezes a weaker teacher, applies distillation only in early training, and turns it off once the student reaches and surpasses teacher-level performance. For ImageNet and CIFAR classification, this strategy reaches target thresholds much earlier, with up to 4.8 times speedup measured by epochs.
We confirm that the method generalizes to other tasks and report 1.7 times epoch speedup for object detection on the COCO dataset, and 2.5 times earlier target-FID crossing for diffusion generation on the CIFAR-10 dataset, measured in steps. These findings validate our method as a universal speedup mechanism for visual learning.
