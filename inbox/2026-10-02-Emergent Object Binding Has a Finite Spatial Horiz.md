---
interest: medium
link: https://arxiv.org/abs/2610.00006
next_step: skim
priority: medium
slack_ts: '1791091826.078089'
source: cs.CV - Computer Vision
status: unread
title: Emergent Object Binding Has a Finite Spatial Horizon
---
# Emergent Object Binding Has a Finite Spatial Horizon
> 原文: [https://arxiv.org/abs/2610.00006](https://arxiv.org/abs/2610.00006)

arXiv:2610.00006v1 Announce Type: new
Abstract: Pretrained Vision Transformers encode whether two image patches belong to the same object. This IsSameObject signal is decodable from frozen patch embeddings at high accuracy, which suggests that object binding emerges from self-supervised pretraining alone. We show that this single accuracy number hides the structure of the signal. Binding is local: the probability that two patches of the same object are decoded as bound falls off monotonically with the distance between them and levels off at a nonzero floor, a falloff well described by an exponential with a finite length scale. This decay holds across object sizes, across three families of probe, on both ADE20K and COCO, and across DINO and CLIP backbones, which indicates that it is a property of the representation rather than of the decoder. Reading binding as local spatial coherence with a finite range accounts for a set of behaviors that the aggregate score leaves unexplained: binding weakens on large objects, separates distinct objects of the same class less reliably than objects of different classes, and groups object parts with their wholes. It is, by contrast, unaffected by occlusion once object size is controlled. We map each behavior with confounds controlled. As a preliminary observation, the horizon and its floor are organized at different depths in DINOv2 and DINOv3, which we report as suggestive given the small number of layers probed and the confound between the two models.
