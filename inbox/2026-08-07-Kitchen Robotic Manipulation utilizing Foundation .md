---
interest: medium
link: https://arxiv.org/abs/2608.04042
next_step: skim
priority: medium
slack_ts: '1786072112.409069'
source: cs.RO - Robotics
status: unread
title: Kitchen Robotic Manipulation utilizing Foundation Models
---
# Kitchen Robotic Manipulation utilizing Foundation Models
> 原文: [https://arxiv.org/abs/2608.04042](https://arxiv.org/abs/2608.04042)

arXiv:2608.04042v1 Announce Type: new
Abstract: Deploying robots in everyday human environments requires perception systems that are both robust and adaptable to diverse, dynamic conditions. In this work, we present a modular perception pipeline for household manipulation tasks, with a focus on dishware handling in kitchen environments. The pipeline integrates open-vocabulary object detection, multi-view segmentation, instance-aware 3D reconstruction, and a 2D-3D feature fusion strategy for 6D pose estimation and grasp planning. Its modular design enables systematic substitution of multiple visual and geometric foundation models, allowing us to identify the best-performing configuration through extensive evaluation on a custom kitchen dataset. The best-performing configuration (LLMDet + SAMv2 + DINOv2 + GeoTransformer) achieves an ADI of 89.12\% on the 20-scene kitchen benchmark with cluttered and occluded conditions. Furthermore, real-world demonstrations confirm that the best configuration can be deployed on physical robots without environment-specific retraining, successfully executing tasks such as sink-to-dishwasher transfer and cup stacking. It validates the adaptability and scalability of the pipeline and highlights its potential as a practical framework for household robotic systems. Our code and supplementary materials are available at https://raivlab.github.io/FM\_kitchen .
