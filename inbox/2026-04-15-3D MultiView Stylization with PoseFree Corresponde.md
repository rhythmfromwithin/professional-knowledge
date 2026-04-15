---
interest: medium
link: https://arxiv.org/abs/2604.09639
next_step: skim
priority: medium
slack_ts: '1776223656.077479'
source: cs.CV - Computer Vision
status: unread
title: 3D Multi-View Stylization with Pose-Free Correspondences Matching for Robust
  3D Geometry Preservation
---
# 3D Multi-View Stylization with Pose-Free Correspondences Matching for Robust 3D Geometry Preservation
> 原文: [https://arxiv.org/abs/2604.09639](https://arxiv.org/abs/2604.09639)

arXiv:2604.09639v1 Announce Type: new
Abstract: Artistic style transfer is well studied for images and videos, but extending it to multi-view 3D scenes remains difficult because stylization can disrupt correspondences needed by geometry-aware pipelines. Independent per-view stylization often causes texture drift, warped edges, and inconsistent shading, degrading SLAM, depth prediction, and multi-view reconstruction. This thesis addresses multi-view stylization that remains usable for downstream 3D tasks without assuming camera poses or an explicit 3D representation during training.
We introduce a feed-forward stylization network trained with per-scene test-time optimization under a composite objective coupling appearance transfer with geometry preservation. Stylization is driven by an AdaIN-inspired loss from a frozen VGG-19 encoder, matching channel-wise moments to a style image. To stabilize structure across viewpoints, we propose a correspondence-based consistency loss using SuperPoint and SuperGlue, constraining descriptors from a stylized anchor view to remain consistent with matched descriptors from the original multi-view set. We also impose a depth-preservation loss using MiDaS/DPT and use global color alignment to reduce depth-model domain shift. A staged weight schedule introduces geometry and depth constraints.
We evaluate on Tanks and Temples and Mip-NeRF 360 using image and reconstruction metrics. Style adherence and structure retention are measured by Color Histogram Distance (CHD) and Structure Distance (DSD). For 3D consistency, we use monocular DROID-SLAM trajectories and symmetric Chamfer distance on back-projected point clouds. Across ablations, correspondence and depth regularization reduce structural distortion and improve SLAM stability and reconstructed geometry; on scenes with MuVieCAST baselines, our method yields stronger trajectory and point-cloud consistency while maintaining competitive stylization.
