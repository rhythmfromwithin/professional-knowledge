---
title: "Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.14822
priority: medium
status: unread
interest: medium
next_step: skim
---
# Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2608.14822](https://arxiv.org/abs/2608.14822)

arXiv:2608.14822v1 Announce Type: new
Abstract: Vision-language-action (VLA) models have improved the flexibility and generality of robotic manipulation, yet they remain fragile to online disruptions, such as changes in task goal, scene configuration, or robot state. Existing recovery methods often require failure data, policy retraining, or external corrective agents, introducing additional data requirements and execution risks. We propose Counterfactual Realignment (CoRe), a training-free framework that recovers a frozen VLA at inference time without failure data. Upon detecting a deviation, CoRe imagines how the policy would continue toward the current goal from a recent viable state, using synthesized observations in place of physical execution, and then minimally realigns the robot and scene to rejoin this imagined continuation before returning control to the policy. Recovery is therefore planned without physical trial-and-error, preserves completed task progress, and handles both mid-episode instruction changes and physical perturbations in a unified manner. Extensive experiments across multiple simulators, VLA backbones, and real-world settings show that CoRe improves success rates by up to 85.0 percentage points to near-nominal levels while reducing physical restorations by 42.2%, without policy fine-tuning or failure-specific recovery training.
