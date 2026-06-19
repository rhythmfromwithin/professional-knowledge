---
title: "Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.19357
priority: medium
status: unread
interest: medium
next_step: skim
---
# Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots
> 原文: [https://arxiv.org/abs/2606.19357](https://arxiv.org/abs/2606.19357)

arXiv:2606.19357v1 Announce Type: new
Abstract: We built a robot called the Robotroller that actuates an Atari CX40+ controller and a device called the Atari Devbox that renders the game frame and the reward signal from the Arcade Learning Environment on a screen. The Robotroller and the Atari Devbox, together with an off-the-shelf camera and a desktop computer, constitute a system that can be used to study reinforcement learning algorithms in the physical world. We call the full system Physical Atari. In this paper, we detail the key decisions that make Physical Atari a robust and accessible platform. To make the system robust, we designed the Robotroller so that all movement is done through bearings, which reduces wear. Additionally, we wrote software that monitors the state of the servos at a high frequency and intervenes to limit stress. To make the system accessible, we used affordable off-the-shelf components and parts that can be manufactured using consumer 3D printers. Physical Atari can be built for under $1,000 and has been used for weeks of non-stop reinforcement learning experiments without any mechanical failures. We used it to validate that reinforcement learning algorithms can learn directly on robots and show that even small distribution shifts between learning and deployment can significantly degrade the performance of policies. Our results underscore the importance of on-device adaptation for strong performance on robots.
