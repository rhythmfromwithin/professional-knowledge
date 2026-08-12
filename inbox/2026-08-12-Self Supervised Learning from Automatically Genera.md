---
title: "Self Supervised Learning from Automatically Generated Demonstrations for Visual Robotic Manipulation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.07553
priority: medium
status: unread
interest: medium
next_step: skim
---
# Self Supervised Learning from Automatically Generated Demonstrations for Visual Robotic Manipulation
> 原文: [https://arxiv.org/abs/2608.07553](https://arxiv.org/abs/2608.07553)

arXiv:2608.07553v1 Announce Type: new
Abstract: Robotic manipulation often requires object specific programming, manual data annotation, or calibrated perception pipelines, which limits rapid deployment in practical settings. Learning from demonstration offers a more direct alternative, but collecting demonstrations can still demand human teleoperation or kinesthetic teaching. This paper presents a self supervised visual manipulation method in which a robot automatically generates demonstrations around a target pose and learns relative pose corrections directly from wrist mounted RGB images. The proposed pipeline uses ROS~2 and Isaac Sim to collect labeled image-pose pairs without requiring explicit camera to robot extrinsic calibration. Separate datasets are generated for planar refinement and coarse three dimensional approach, and a convolutional network is trained to regress relative translation and rotation from single frame RGB observations. During execution, a coarse to fine controller first approaches the object using models trained with height variation and then refines the final alignment using planar data. The method is evaluated both in simulation and on a real UR5e collaborative robot equipped with a gripper and a monocular camera. In simulation, the refinement stage reduces the final planar dispersion from 9.69 mm to 5.38 mm. In real world experiments, the system performs end to end grasp attempts on three physical objects and reaches success rates of 66.6% and 63.6% for two objects without object rotation, while still maintaining partial robustness under rotated conditions. These results show that automatically generated demonstrations can support practical visual manipulation with limited setup effort, while also exposing remaining challenges in depth prediction and object dependent generalization.
