---
title: "COD10K-C: Benchmarking Robustness of Camouflaged Object Detection Under Natural Image Corruptions"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2606.02603
priority: medium
status: unread
interest: medium
next_step: skim
---
# COD10K-C: Benchmarking Robustness of Camouflaged Object Detection Under Natural Image Corruptions
> 原文: [https://arxiv.org/abs/2606.02603](https://arxiv.org/abs/2606.02603)

arXiv:2606.02603v1 Announce Type: new
Abstract: Camouflaged object detection has improved substantially, but most standard benchmarks evaluate models only on clean images. This is not realistic because real cameras often capture blur, sensor noise, weather effects, and compression artifacts. We present COD10K-C, a corruption robustness benchmark based on COD10K. It includes 8 corruption types and 5 severity levels, giving 40 conditions and 81,040 evaluation pairs in total. We evaluate three popular camouflaged object detection models, SINet-v2, PFNet, and ZoomNet, as well as a lightweight model called RobustCODLite. All models show clear performance drops on corrupted images. Motion blur and Gaussian blur cause the largest drops, with SINet-v2 losing 18.5 Dice points under motion blur. Brightness and fog are less harmful. RobustCODLite uses corruption augmentation, a frequency-prior branch, and an uncertainty-consistency loss. It retains 92.3% of its clean Dice score under corruption, compared with 87.7% for SINet-v2, 84.8% for ZoomNet, and 84.1% for PFNet. On the hardest corruptions, RobustCODLite matches or outperforms models that perform better on clean data. We will release the COD10K-C GitHub repository to support future research in robust camouflaged object detection.
