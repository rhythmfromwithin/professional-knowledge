---
interest: medium
link: https://arxiv.org/abs/2606.02937
next_step: skim
priority: low
slack_ts: '1780548660.259579'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'BEAST3D: Animal behavioral analysis and neural encoding from multi-view video
  via Gaussian splatting'
---
# BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting
> 原文: [https://arxiv.org/abs/2606.02937](https://arxiv.org/abs/2606.02937)

arXiv:2606.02937v1 Announce Type: new
Abstract: Multi-view video recordings are increasingly used to capture the 3D movements of animals in experimental settings, yet extracting rich 3D representations from these recordings remains challenging. Supervised pose estimation requires extensive manual annotation, while general-purpose 3D reconstruction models trained on generic scene datasets fail on the specialized imagery and sparse-view setting of laboratory experiments. We address these limitations with BEAST3D, a self-supervised pretraining framework that learns 3D visual representations from unlabeled, calibrated multi-view video. BEAST3D uses a vision transformer to predict 3D Gaussian splats that reconstruct held-out views through differentiable rendering, while simultaneously segmenting the animal from the background. BEAST3D reconstructs 3D structure with as few as four views by conditioning directly on known camera parameters--unlike general-purpose models, which must estimate camera geometry from dense overlapping viewpoints that are seldom available in lab settings. Through comprehensive evaluation across four species, we demonstrate that BEAST3D produces rich, viewpoint-invariant features that transfer effectively to three downstream tasks: novel view synthesis, which validates the quality of the learned 3D representations; multi-view pose estimation, which provides the sparse keypoint trajectories widely used in behavioral analysis; and neural encoding, which relates 3D behavioral features to simultaneously recorded neural activity. BEAST3D thus establishes a versatile framework for behavioral analysis that leverages 3D structure in modern multi-view laboratory recordings.
