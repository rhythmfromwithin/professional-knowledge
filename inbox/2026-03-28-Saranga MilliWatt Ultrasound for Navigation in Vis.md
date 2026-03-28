---
interest: medium
link: https://arxiv.org/abs/2603.24699
next_step: skim
priority: medium
slack_ts: '1774666243.838409'
source: cs.RO - Robotics
status: unread
title: 'Saranga: MilliWatt Ultrasound for Navigation in Visually Degraded Environments
  on Palm-Sized Aerial Robots'
---
# Saranga: MilliWatt Ultrasound for Navigation in Visually Degraded Environments on Palm-Sized Aerial Robots
> 原文: [https://arxiv.org/abs/2603.24699](https://arxiv.org/abs/2603.24699)

arXiv:2603.24699v1 Announce Type: new
Abstract: Tiny palm-sized aerial robots possess exceptional agility and cost-effectiveness in navigating confined and cluttered environments. However, their limited payload capacity directly constrains the sensing suite on-board the robot, thereby limiting critical navigational tasks in Global Positioning System (GPS)-denied wild scenes. Common methods for obstacle avoidance use cameras and LIght Detection And Ranging (LIDAR), which become ineffective in visually degraded conditions such as low visibility, dust, fog or darkness. Other sensors, such as RAdio Detection And Ranging (RADAR), have high power consumption, making them unsuitable for tiny aerial robots. Inspired by bats, we propose Saranga, a low-power ultrasound-based perception stack that localizes obstacles using a dual sonar array. We present two key solutions to combat the low Peak Signal-to-Noise Ratio of $-4.9$ decibels: physical noise reduction and a deep learning based denoising method. Firstly, we present a practical way to block propeller induced ultrasound noise on the weak echoes. The second solution is to train a neural network to utilize the \textcolor{black}{long horizon of ultrasound echoes} for finding signal patterns under high amounts of uncorrelated noise where classical methods were insufficient. We generalize to the real world by using a synthetic data generation pipeline and limited real noise data for training. We enable a palm-sized aerial robot to navigate in visually degraded conditions of dense fog, darkness, and snow in a cluttered environment with thin and transparent obstacles using only on-board sensing and computation. We provide extensive real world results to demonstrate the efficacy of our approach.
