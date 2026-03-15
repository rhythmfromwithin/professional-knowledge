---
interest: medium
link: https://arxiv.org/abs/2603.04470
next_step: skim
priority: medium
slack_ts: '1773544811.599079'
source: cs.RO - Robotics
status: unread
title: Efficient Autonomous Navigation of a Quadruped Robot in Underground Mines on
  Edge Hardware
---
# Efficient Autonomous Navigation of a Quadruped Robot in Underground Mines on Edge Hardware
> 原文: [https://arxiv.org/abs/2603.04470](https://arxiv.org/abs/2603.04470)

arXiv:2603.04470v1 Announce Type: new
Abstract: Embodied navigation in underground mines faces significant challenges, including narrow passages, uneven terrain, near-total darkness, GPS-denied conditions, and limited communication infrastructure. While recent learning-based approaches rely on GPU-accelerated inference and extensive training data, we present a fully autonomous navigation stack for a Boston Dynamics Spot quadruped robot that runs entirely on a low-power Intel NUC edge computer with no GPU and no network connectivity requirements. The system integrates LiDAR-inertial odometry, scan-matching localization against a prior map, terrain segmentation, and visibility-graph global planning with a velocity-regulated local path follower, achieving real-time perception-to-action at consistent control rates. After a single mapping pass of the environment, the system handles arbitrary goal locations within the known map without any environment-specific training or learned components. We validate the system through repeated field trials using four target locations of varying traversal difficulty in an experimental underground mine, accumulating over 700 m of fully autonomous traverse with a 100% success rate across all 20 trials (5 repetitions x 4 targets) and an overall Success weighted by Path Length (SPL) of 0.73 \pm 0.09.
