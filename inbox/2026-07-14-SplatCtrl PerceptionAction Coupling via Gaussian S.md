---
title: "SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.08948
priority: medium
status: unread
interest: medium
next_step: skim
---
# SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control
> 原文: [https://arxiv.org/abs/2607.08948](https://arxiv.org/abs/2607.08948)

arXiv:2607.08948v1 Announce Type: new
Abstract: Robotic manipulators excel in structured environments but face substantial challenges in unstructured and dynamic settings. This paper presents SplatCtrl, a unified framework for real-time scene reconstruction and reactive robot motion generation to enable collision-free robotic arm control in previously unseen and continuously changing environments. Building on 3D Gaussian Splatting (3D-GS), we introduce a hybrid voxel-based filtering and dynamic Gaussian relocation strategy that supports efficient scene reconstruction from RGB-D streams while accommodating environmental changes. For safe and reactive control, we further propose a method for deriving continuous signed distance functions from isotropic Gaussians, providing stable and differentiable collision probability estimates that bridge classical distance fields with the modern implicit representation. These continuous distance metrics are incorporated into control barrier functions, resulting in a unified perception-action coupling framework that supports smooth and reliable real-time motion generation in response to scene changes. Experimental validation in simulation, on physical robot, and within shared human-robot workspace demonstrates the framework's effectiveness, achieving integrated scene reconstruction and reactive control in uncertain, and dynamic environments.
