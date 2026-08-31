---
interest: medium
link: https://arxiv.org/abs/2608.27497
next_step: skim
priority: medium
slack_ts: '1788152842.237919'
source: cs.RO - Robotics
status: unread
title: 'Beyond Relative Geometry: Metric-Aware Geometry Perception for Robotics'
---
# Beyond Relative Geometry: Metric-Aware Geometry Perception for Robotics
> 原文: [https://arxiv.org/abs/2608.27497](https://arxiv.org/abs/2608.27497)

arXiv:2608.27497v1 Announce Type: new
Abstract: Recent embodied models increasingly leverage geometric representations to improve spatial reasoning and robotic manipulation. However, existing reconstruction methods only reconstruct relative geometry with arbitrary scales, causing predicted object dimensions and spatial distances to vary across scenes, viewpoints, and input configurations. This inconsistency prevents geometric perception from being directly aligned with robotic actions defined on the real-world scale. To address this limitation, we propose Metric-Aware Geometry Perception (MAGP), an end-to-end, plug-and-play framework for metric geometry reconstruction that can be seamlessly integrated into robotic policies. At its core, Metric Scale Equivariant Augmentation encourages the model to reconstruct metric geometry from camera parameters and depth observations, ensuring that the reconstructed geometry follows the metric scale specified by observations. Flexible Metric Conditioning further enables MAGP to support arbitrary view counts and combinations of camera and depth inputs, improving robustness to heterogeneous robotic sensing configurations. Together, these designs produce geometrically consistent reconstructions with stable object dimensions and spatial distances across scenes and sensing conditions. Experiments on ETH3D, MegaDepth, and ScanNet++ demonstrate that MAGP maintains strong relative geometry accuracy while reducing the absolute error by over an order of magnitude, from 2.01m to 0.07m. When integrated into multiple robotic policies, MAGP consistently improves performance on LIBERO, RoboTwin, and zero-shot LIBERO-Plus, with gains of up to 6.26% on RoboTwin. These results demonstrate the effectiveness and generalizability of metric geometry for robotic manipulation.
