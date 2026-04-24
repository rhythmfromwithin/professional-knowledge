---
interest: medium
link: https://arxiv.org/abs/2604.19982
next_step: skim
priority: low
slack_ts: '1777001713.676419'
source: cs.DB - Databases
status: unread
title: '3DPipe: A Pipelined GPU Framework for Scalable Generalized Spatial Join over
  Polyhedral Objects'
---
# 3DPipe: A Pipelined GPU Framework for Scalable Generalized Spatial Join over Polyhedral Objects
> 原文: [https://arxiv.org/abs/2604.19982](https://arxiv.org/abs/2604.19982)

arXiv:2604.19982v1 Announce Type: new
Abstract: Spatial join is a fundamental operation in spatial databases. With the rapid growth of 3D data in applications such as LiDAR-based object detection and 3D digital pathology, there is an increasing need to support spatial join over 3D datasets. However, existing techniques are largely designed for 2D data, leaving 3D spatial join underexplored and computationally expensive. We present 3DPipe, a pipelined GPU framework for scalable spatial join over polyhedral objects. 3DPipe exploits GPU parallelism across both filtering and refinement stages, incorporates a multi-level pruning strategy for efficient candidate reduction, and employs chunked streaming to handle datasets exceeding GPU memory. Its pipelined execution overlaps CPU data preparation, host-device data transfer, and GPU computation to improve throughput. Experiments show that 3DPipe achieves up to 9.0$\times$ speedup over the state-of-the-art GPU solution, TDBase, while maintaining excellent scalability. 3DPipe is open-sourced at https://github.com/lyuheng/3dpipe.
