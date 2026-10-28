---
title: "E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.36011
priority: medium
status: unread
interest: medium
next_step: skim
---
# E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling
> 原文: [https://arxiv.org/abs/2610.36011](https://arxiv.org/abs/2610.36011)

arXiv:2610.36011v1 Announce Type: new
Abstract: World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-native world-action model built directly on 3D foundation models. E0.5 introduces two key innovations. First, it adopts a 3D foundation model as the primary backbone, making 3D geometry the native representation for both world modeling and action prediction. Second, it explicitly predicts future 3D states together with actions, enabling the model to capture geometric world dynamics beyond action-only modeling or future video prediction. Experiments on RoboTwin 2.0 first demonstrate the effectiveness of E0.5 without embodied-data pretraining, achieving success rates of 89.90\% and 50.09\% under clean and randomized settings, respectively. Building on these results, we further pretrain E0.5 on more than 160k robot trajectories from AgiBotWorld-Beta, jointly learning robot actions and future geometry within the pretrained 3D foundation. This embodied pretraining improves mean real-world manipulation success rates by approximately 15 and 7 percentage points on AgileX Piper and Zerith H1, respectively. Together, these results demonstrate the potential of geometry-native foundations to acquire robot interaction knowledge and transfer it to physical manipulation. E0.5 embodies this geometry-native approach as a member of the VWA family of world-action models.
