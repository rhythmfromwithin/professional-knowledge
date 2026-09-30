---
interest: medium
link: https://arxiv.org/abs/2609.30358
next_step: skim
priority: medium
slack_ts: '1790745122.536219'
source: cs.RO - Robotics
status: unread
title: 'TinyCVIO: A Constellation-Aided Visual-Inertial Odometry System for Nanodrones'
---
# TinyCVIO: A Constellation-Aided Visual-Inertial Odometry System for Nanodrones
> 原文: [https://arxiv.org/abs/2609.30358](https://arxiv.org/abs/2609.30358)

arXiv:2609.30358v1 Announce Type: new
Abstract: Nanodrones require accurate, real-time state estimation under severe sensing and computational constraints. We present TinyCVIO, a visual-inertial odometry system that co-designs miniature sensing, visual processing, and estimation for a commodity dual-core microcontroller with 520 kB SRAM. Lightweight LED constellations provide known geometry without surveyed positions or yaw angles, assuming placement on a common level plane. A streaming visual frontend tracks LED observations from a millimeter-scale camera at 29.2 FPS, while a rigid-board measurement model retains inter-LED constraints and streaming QR bounds estimation workspace for a fixed filter-state size. Across 19 hand-held hardware-in-the-loop datasets, the rigid-board model reduces mean absolute trajectory error by 27% relative to planar points. The complete system runs onboard a Crazyflie across nine flights at three speeds, achieving 3.5-3.7 cm mean absolute trajectory error and 0.50-0.60% relative pose error over 10 m segments, with mean estimate latency of 15.7-16.3 ms.
