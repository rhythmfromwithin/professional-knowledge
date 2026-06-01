---
interest: medium
link: https://arxiv.org/abs/2605.29138
next_step: skim
priority: medium
slack_ts: '1780290087.617239'
source: cs.RO - Robotics
status: unread
title: Multi-Resolution End-to-End Deep Neural Network for Optimizing Latency-Accuracy
  Tradeoff in Autonomous Driving
---
# Multi-Resolution End-to-End Deep Neural Network for Optimizing Latency-Accuracy Tradeoff in Autonomous Driving
> 原文: [https://arxiv.org/abs/2605.29138](https://arxiv.org/abs/2605.29138)

arXiv:2605.29138v1 Announce Type: new
Abstract: Latency-accuracy tradeoffs are fundamental in real-time applications of deep neural networks (DNNs) for cyber-physical systems. In autonomous driving, in particular, safety depends on both prediction quality and the end-to-end delay from sensing to actuation. We observe that (1) when latency is accounted for, the latency-optimal network configuration varies with scene context and compute availability; and (2) a single fixed-resolution model becomes suboptimal as conditions change.
We present a multi-resolution, end-to-end deep neural network for the CARLA urban driving challenge using monocular camera input. Our approach employs a convolutional neural network (CNN) that supports multiple input resolutions through per-resolution batch normalization, enabling runtime selection of an ideal input scale under a latency budget, as well as resolution retargeting, which allows multi-resolution training without access to the original training dataset.
We implement and evaluate our multi-resolution end-to-end CNN in CARLA to explore the latency-safety frontier. Results show consistent improvements in per-route safety metrics - lane invasions, red-light infractions, and collisions - relative to fixed-resolution baselines.
