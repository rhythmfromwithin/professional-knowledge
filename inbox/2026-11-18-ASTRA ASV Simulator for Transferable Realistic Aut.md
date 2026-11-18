---
interest: medium
link: https://arxiv.org/abs/2611.21789
next_step: skim
priority: medium
slack_ts: '1794985133.935549'
source: cs.RO - Robotics
status: unread
title: 'ASTRA: ASV Simulator for Transferable Realistic Autonomy'
---
# ASTRA: ASV Simulator for Transferable Realistic Autonomy
> 原文: [https://arxiv.org/abs/2611.21789](https://arxiv.org/abs/2611.21789)

arXiv:2611.21789v1 Announce Type: new
Abstract: Autonomy development for marine autonomous surface vehicles (ASVs) remains challenging because field testing is costly and difficult to reproduce. Existing marine simulation tools provide mature capabilities in vessel dynamics, robotics integration, and visual rendering, but these strengths are emphasized differently across platforms. This paper presents ASTRA, an ASV simulation framework built in NVIDIA Isaac Sim that combines marine vehicle dynamics, photorealistic perception, and Robot Operating System (ROS 2) autonomy interfaces within a common environment. ASTRA incorporates a Fossen-style marine dynamics model together with geometry-based buoyancy and programmable spectral wave disturbances, enabling non-planar hydrostatic and wave-induced motion. The simulator reproduces the sensor configuration of a physical BlueBoat testbed, including GPS, IMU, LiDAR, and RGB-D sensing exposed through ROS 2. This allows localization, perception, planning, and control software to be developed against interfaces consistent with the physical platform. The BlueBoat's existing ROS 2 localization and perception modules were ported directly into ASTRA, while targeted zero-propulsion experiments were used to verify the implemented wave-body coupling. The simulated roll response was consistent with the expected non-oscillatory hydrostatic behavior, and heave remained highly coherent with the generated wave field, with approximately unity gain at the dominant wave frequency in the tested sea states. ASTRA is intended as an open-source testbed for marine autonomy development, simulation-based benchmarking, and sim-to-real experimentation.
