---
title: "Magnetic Indoor Localization through CNN Regression and Rotation Invariance"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.22896
priority: medium
status: unread
interest: medium
next_step: skim
---
# Magnetic Indoor Localization through CNN Regression and Rotation Invariance
> 原文: [https://arxiv.org/abs/2604.22896](https://arxiv.org/abs/2604.22896)

arXiv:2604.22896v1 Announce Type: new
Abstract: Indoor positioning is an essential technology for a wide range of applications in GNSS-denied environments, including indoor navigation and IoT systems. Combining convolutional neural networks (CNNs) and magnetic field-based features offers a low-cost, infrastructure-free solution for precise positioning. While magnetic fingerprints are a promising approach for indoor positioning, models trained on raw 3D magnetometer data are highly sensitive to device orientation. We address this by using two rotation invariant features derived from the 3D magnetic field: the norm (Mn) and the projection onto the gravity axis (Mg). We train a lightweight 7-layer dilated CNN (MagNetS/XL) on magnetic sequences to directly regress (x, y) positions. Using the MagPie dataset (three buildings, handheld trajectories), we systematically evaluate fixed and random rotations of test and/or train data. Raw 3D inputs (Mx, My , Mz) exhibit isotropic error increases under fixed 90{\deg} rotations and further degrade with growing random rotations. In contrast, 2D (Mn, Mg) inputs maintain rotation invariant accuracy and surpass the 3D inputs once rotation exceeds building-specific thresholds for three reference buildings: 0{\deg} for Loomis (large), 5{\deg} for Talbot (medium), and 6{\deg} for CSL (small). MagNetXL achieves or exceeds state-of-the-art accuracy on the MagPie dataset, and MagNetS delivers similar performance with roughly one third of the parameters, favoring mobile deployment. These results show that the robustness gained from rotation invariant inputs outweighs the loss of input dimensionality in realistic usage, allowing mapping and localization without orientation alignment or added infrastructure.
