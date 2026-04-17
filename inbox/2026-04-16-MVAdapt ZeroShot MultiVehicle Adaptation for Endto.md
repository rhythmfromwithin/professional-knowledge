---
interest: medium
link: https://arxiv.org/abs/2604.11854
next_step: skim
priority: medium
slack_ts: '1776396649.669789'
source: cs.RO - Robotics
status: unread
title: 'MVAdapt: Zero-Shot Multi-Vehicle Adaptation for End-to-End Autonomous Driving'
---
# MVAdapt: Zero-Shot Multi-Vehicle Adaptation for End-to-End Autonomous Driving
> 原文: [https://arxiv.org/abs/2604.11854](https://arxiv.org/abs/2604.11854)

arXiv:2604.11854v1 Announce Type: new
Abstract: End-to-End (E2E) autonomous driving models are usually trained and evaluated with a fixed ego-vehicle, even though their driving policy is implicitly tied to vehicle dynamics. When such a model is deployed on a vehicle with different size, mass, or drivetrain characteristics, its performance can degrade substantially; we refer to this problem as the vehicle-domain gap. To address it, we propose MVAdapt, a physics-conditioned adaptation framework for multi-vehicle E2E driving. MVAdapt combines a frozen TransFuser++ scene encoder with a lightweight physics encoder and a cross-attention module that conditions scene features on vehicle properties before waypoint decoding. In the CARLA Leaderboard 1.0 benchmark, MVAdapt improves over naive transfer and multi-embodiment adaptation baselines on both in-distribution and unseen vehicles. We further show two complementary behaviors: strong zero-shot transfer on many unseen vehicles, and data-efficient few-shot calibration for severe physical outliers. These results suggest that explicitly conditioning E2E driving policies on vehicle physics is an effective step toward more transferable autonomous driving models. All codes are available at https://github.com/hae-sung-oh/MVAdapt
