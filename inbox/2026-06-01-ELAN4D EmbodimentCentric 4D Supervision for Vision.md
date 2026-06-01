---
interest: medium
link: https://arxiv.org/abs/2605.30484
next_step: skim
priority: medium
slack_ts: '1780290095.370049'
source: cs.RO - Robotics
status: unread
title: 'ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models
  via Plug-and-Play Adaptation'
---
# ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation
> 原文: [https://arxiv.org/abs/2605.30484](https://arxiv.org/abs/2605.30484)

arXiv:2605.30484v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models have shown promise for robotic manipulation, yet most existing policies operate reactively by directly regressing actions from current observations, without explicitly modeling future dynamics. This limits their ability to generalize under out-of-distribution perturbations. To address this issue, we propose ELAN4D, an embodiment-centric, 4D-aware training framework that enhances VLA policies with future robot keypoint tracks as predictive spatio-temporal supervision. Using only forward kinematics from proprioceptive states, we derive 3D displacement tracks of robot keypoints, such as joints and the end-effector, with negligible preprocess cost. These tracks provide metric and compact supervision without requiring external trackers or reconstruction. A plug-and-play auxiliary branch with a lightweight track decoder injects this 4D signal into the action expert while preserving the pretrained vision-language backbone through gradient isolation. The track decoder is discarded during inference, leaving the base policy interface unchanged. Extensive experiments on LIBERO, LIBERO-Plus, RoboTwin2.0 and real-world manipulation tasks demonstrate that ELAN4D consistently improves over strong VLA baselines, achieving the best overall performance and substantial gains under out-of-distribution perturbations, including camera, background, and layout shifts. These results highlight the effectiveness of embodiment-centric 4D supervision for building more robust and generalizable manipulation policies.
