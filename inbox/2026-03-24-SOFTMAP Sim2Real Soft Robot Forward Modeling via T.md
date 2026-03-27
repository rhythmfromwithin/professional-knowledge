---
interest: medium
link: https://arxiv.org/abs/2603.19384
next_step: skim
priority: medium
slack_ts: '1774581537.580449'
source: cs.RO - Robotics
status: unread
title: 'SOFTMAP: Sim2Real Soft Robot Forward Modeling via Topological Mesh Alignment
  and Physics Prior'
---
# SOFTMAP: Sim2Real Soft Robot Forward Modeling via Topological Mesh Alignment and Physics Prior
> 原文: [https://arxiv.org/abs/2603.19384](https://arxiv.org/abs/2603.19384)

arXiv:2603.19384v1 Announce Type: new
Abstract: While soft robot manipulators offer compelling advantages over rigid counterparts, including inherent compliance, safe human-robot interaction, and the ability to conform to complex geometries, accurate forward modeling from low-dimensional actuation commands remains an open challenge due to nonlinear material phenomena such as hysteresis and manufacturing variability. We present SOFTMAP, a sim-to-real learning framework for real-time 3D forward modeling of tendon-actuated soft finger manipulators. SOFTMAP combines four components: (1) As-Rigid-As-Possible (ARAP)-based topological alignment that projects simulated and real point clouds into a shared, topologically consistent vertex space; (2) a lightweight MLP forward model pretrained on simulation data to map servo commands to full 3D finger geometry; (3) a residual correction network trained on a small set of real observations to predict per-vertex displacement fields that compensate for sim-to-real discrepancies; and (4) a closed-form linear actuation calibration layer enabling real-time inference at 30 FPS. We evaluate SOFTMAP on both simulated and physical hardware, achieving state-of-the-art shape prediction accuracy with a Chamfer distance of 0.389 mm in simulation and 3.786 mm on hardware, millimeter-level fingertip trajectory tracking across multiple target paths, and a 36.5% improvement in teleoperation task success over the baseline. Our results show that SOFTMAP provides a data-efficient approach for 3D forward modeling and control of soft manipulators.
