---
interest: medium
link: https://arxiv.org/abs/2610.33174
next_step: skim
priority: medium
slack_ts: '1793164455.338979'
source: cs.RO - Robotics
status: unread
title: 'Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust
  Visual SLAM'
---
# Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM
> 原文: [https://arxiv.org/abs/2610.33174](https://arxiv.org/abs/2610.33174)

arXiv:2610.33174v1 Announce Type: new
Abstract: Rapid illumination transitions can disturb Visual SLAM (VSLAM) by saturating images before the Automatic Exposure (AE) policy adapts, removing the visual correspondences needed to maintain tracking. Our proposed methods mitigate this disturbance at two levels: B-Adapt acquires adaptive exposure brackets to cover the scene dynamic range while promoting photometric overlap, and BVSLAM directly uses the multi-exposure sequence as constraints in a factor graph state estimator without relying on High Dynamic Range (HDR) merging. We evaluate both methods against state-of-the-art approaches in nominal environments and during a repeated tunnel-exit transition at an emulated vehicle speed of 32 m s-1. In the tunnel, combining our B-Adapt with BVSLAM reduces the state estimation error by 78 % compared with AE images. These results suggest that bracketing efficiently improves visual pose estimation robustness to rapid illumination disturbances while retaining low error under nominal conditions. Our code is available at https://github.com/norlab-ulaval/bracketing-shows-the-way.
