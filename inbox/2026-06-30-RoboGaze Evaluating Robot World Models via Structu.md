---
interest: medium
link: https://arxiv.org/abs/2606.28385
next_step: skim
priority: medium
slack_ts: '1782792825.267779'
source: cs.RO - Robotics
status: unread
title: 'RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis'
---
# RoboGaze: Evaluating Robot World Models via Structured Vision-Language Analysis
> 原文: [https://arxiv.org/abs/2606.28385](https://arxiv.org/abs/2606.28385)

arXiv:2606.28385v1 Announce Type: new
Abstract: Recent advances in robot world models enable synthetic video generation for embodied prediction and planning. However, evaluating these videos is challenging: visually realistic outputs often violate physical laws, temporal consistency, or task logic, while conventional metrics and monolithic Vision-Language Model (VLM) judges fail to generalize or provide precise diagnostic value. We present RoboGaze, a training-free, multi-agent VLM framework that provides structured, interpretable evaluation for generated robot-manipulation videos. Given a task instruction and video, RoboGaze operates via a three-stage pipeline: task-scene grounding, dimension-specific specialist routing, and critic-based verification. It outputs temporally localized glitch reports categorized under a novel 6-dimension, 30-type robotics-specific taxonomy. To benchmark RoboGaze, we introduce a human-validated dataset of 382 clips spanning simulated and real-world multi-view manipulation. Evaluating eight open-source and proprietary VLM backbones, RoboGaze dramatically outperforms zero-shot baselines, improving description-F1 by up to +43 points and temporal alignment (F1 x IoU) by up to +37 points, closing approximately 85% of the gap to the human ceiling. Furthermore, its critic verifier mitigates the "cry-wolf" false-positive flaw of standard VLMs, lifting clean-clip accuracy from under 25% to over 80%. RoboGaze offers a scalable, highly interpretable diagnostic tool for the rigorous evaluation of robot world models.
