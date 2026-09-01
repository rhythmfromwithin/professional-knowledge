---
title: "Understanding Temporal Semantic Stability in Open-Vocabulary UAV Perception through Metric 3D Fusion"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.28665
priority: medium
status: unread
interest: medium
next_step: skim
---
# Understanding Temporal Semantic Stability in Open-Vocabulary UAV Perception through Metric 3D Fusion
> 原文: [https://arxiv.org/abs/2608.28665](https://arxiv.org/abs/2608.28665)

arXiv:2608.28665v1 Announce Type: new
Abstract: Recent open-vocabulary segmentation models have advanced semantic perception for UAVs, but predictions from moving aerial platforms can remain temporally inconsistent across repeated observations of the same physical scene. We investigate temporal semantic stability by associating frame-wise predictions with persistent world-space locations through metric 3D fusion. We introduce a voxel-level evaluation framework that jointly characterises final semantic agreement, Semantic Belief Drift (SBD), Observation Persistence (OP), and semantic uncertainty. Experiments on UAVid-3D reveal substantial frame-wise semantic flicker and show that high aggregate world-space agreement can overstate temporal stability when locations have limited repeated-observation support. Persistence-stratified analysis shows that recurrent voxels expose greater semantic disagreement, while belief drift decreases as additional evidence accumulates. This behaviour is observed across two segmentation backbones and remains consistent under variations in voxel resolution, geometric association, and temporal sampling density. Conditions that reduce world-space recurrence can increase apparent aggregate stability, demonstrating that semantic consistency must be interpreted together with observation support. Our findings highlight observation persistence as an essential conditioning variable for evaluating long-horizon semantic reliability.
