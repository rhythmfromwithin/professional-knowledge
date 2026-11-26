---
title: "Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.33352
priority: medium
status: unread
interest: medium
next_step: skim
---
# Why Does Sensor Depth Fail Learned Manipulation Policies? Finding the Failure Mode with ACT
> 原文: [https://arxiv.org/abs/2611.33352](https://arxiv.org/abs/2611.33352)

arXiv:2611.33352v1 Announce Type: new
Abstract: Learned manipulation policies, from task-specific imitation policies to vision-language-action (VLA) models, rely primarily on RGB images. While some studies report gains from sensor depth, others avoid depth cameras because of measurement noise. Depth cameras introduce both noise and missing depth values (holes), whose relative effects remain unclear. In this study, we calibrate a sensor model using a real wrist-mounted stereo camera and separately evaluate noise and holes on RGB-D imitation policies with three visual encoders in simulation. We found that complete depth improves success by approximately ten percentage points, and most of this gain persists even at twenty times the camera's noise level. In contrast, holes covering about one-sixth of the wrist image eliminate the detectable benefit of depth. The validity mask strongly influences depth reliance: marking a small fraction of pixels as invalid reduces reliance, while filling holes and marking them valid restores most of the benefit. Policies trained on clean depth also lose performance when holes appear only at deployment, sometimes falling below RGB-only performance. These findings suggest that depth cameras for learned policies should therefore be judged by depth coverage more than measurement precision.
