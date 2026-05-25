---
title: "Extending Deep Event Visual Odometry with Sparse Point-Cloud Export"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.22890
priority: medium
status: unread
interest: medium
next_step: skim
---
# Extending Deep Event Visual Odometry with Sparse Point-Cloud Export
> 原文: [https://arxiv.org/abs/2605.22890](https://arxiv.org/abs/2605.22890)

arXiv:2605.22890v1 Announce Type: new
Abstract: Event cameras are well suited for visual odometry under high-speed motion and challenging lighting conditions due to their low latency, high temporal resolution, and high dynamic range. Deep Event Visual Odometry (DEVO) demonstrated that monocular event-only odometry can achieve strong performance by combining sparse patch tracking, learned patch selection, recurrent correspondence refinement, and differentiable bundle adjustment. In this project, we extend DEVO with a sparse point-cloud export pipeline. Rather than modifying the core odometry formulation, our approach exposes the internal 3D structure already estimated by DEVO and converts it into an explicit point-cloud representation for visualization and further processing. In addition, we implement a practical workflow for data export, format conversion, and point-cloud cleanup. The resulting system preserves the original visual odometry pipeline while enabling sparse geometric scene output. Experiments on the BOARD SLOW sequence show that the exported sparse cloud is locally consistent with EMVS reconstructions, achieving high precision at a 5 cm threshold, while also highlighting the expected limitations in density, completeness, and sensitivity to accumulated odometry noise.
