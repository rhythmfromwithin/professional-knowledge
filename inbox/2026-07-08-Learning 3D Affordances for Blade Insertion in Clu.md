---
title: "Learning 3D Affordances for Blade Insertion in Cluttered Stowing"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.02549
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning 3D Affordances for Blade Insertion in Cluttered Stowing
> 原文: [https://arxiv.org/abs/2607.02549](https://arxiv.org/abs/2607.02549)

arXiv:2607.02549v1 Announce Type: new
Abstract: Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade\_insertion. html.
