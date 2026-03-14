---
interest: medium
link: https://arxiv.org/abs/2603.11071
next_step: skim
priority: medium
slack_ts: '1773456146.972899'
source: cs.RO - Robotics
status: unread
title: 'TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers'
---
# TinyNav: End-to-End TinyML for Real-Time Autonomous Navigation on Microcontrollers
> 原文: [https://arxiv.org/abs/2603.11071](https://arxiv.org/abs/2603.11071)

arXiv:2603.11071v1 Announce Type: new
Abstract: Autonomous navigation typically relies on power-intensive processors, limiting accessibility in low-cost robotics. Although microcontrollers offer a resource-efficient alternative, they impose strict constraints on model complexity. We present TinyNav, an end-to-end TinyML system for real-time autonomous navigation on an ESP32 microcontroller. A custom-trained, quantized 2D convolutional neural network processes a 20-frame sliding window of depth data to predict steering and throttle commands. By avoiding 3D convolutions and recurrent layers, the 23k-parameter model achieves 30 ms inference latency. Correlation analysis and Grad-CAM validation indicate consistent spatial awareness and obstacle avoidance behavior. TinyNav demonstrates that responsive autonomous control can be deployed directly on highly constrained edge devices, reducing reliance on external compute resources.
