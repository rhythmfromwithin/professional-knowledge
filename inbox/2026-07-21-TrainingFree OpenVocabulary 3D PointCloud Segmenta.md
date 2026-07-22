---
interest: medium
link: https://arxiv.org/abs/2607.15331
next_step: skim
priority: medium
slack_ts: '1784690756.319969'
source: cs.CV - Computer Vision
status: unread
title: Training-Free Open-Vocabulary 3D Point-Cloud Segmentation on the Generalized
  Few-Shot Benchmark
---
# Training-Free Open-Vocabulary 3D Point-Cloud Segmentation on the Generalized Few-Shot Benchmark
> 原文: [https://arxiv.org/abs/2607.15331](https://arxiv.org/abs/2607.15331)

arXiv:2607.15331v1 Announce Type: new
Abstract: Generalized few-shot 3D point-cloud segmentation (GFS-PCS) asks a model to segment a scene into many base classes seen at training time and a set of novel classes. The state of the art reaches novel classes by reconciling a dense but noisy 3D vision-language prior with the few-shot support, but it pays for this with base 3D labels, per-episode training, and the support annotations themselves. We ask how far the same reconciliation can go with none of these: no training, no 3D labels, and not even the few-shot support. We pair a frozen 3D vision-language model (RegionPLC) as a dense prior with a frozen promptable concept segmenter (SAM3), prompted by the bare novel class names and lifted from posed RGB views, and reconcile the two by cross-view consistency: a point becomes novel only when enough of the views that see it agree. On the ScanNet200 GFS-PCS benchmark this fully training-free, open-vocabulary pipeline improves novel mIoU by +2.6 over the training-free dense prior while holding base accuracy within 0.5, and recovers a third (33%) of the novel-class gap to the trained state of the art that uses far more supervision. We further show that injecting the few-shot support into the pipeline, as a fusion gate and as a prototypical dense classifier, adds nothing over consistency alone and in fact degrades it through the classifier, which is why the method needs no support at all. On the harder ScanNet++ benchmark, where the dense prior is far weaker on novel classes, the same pipeline nearly doubles novel mIoU (+15.7, from 16.2 to 31.9) at a 1.7 base cost, lifting the harmonic mean from 21.5 to 31.1
