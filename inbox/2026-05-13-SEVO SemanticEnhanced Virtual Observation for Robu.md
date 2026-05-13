---
title: "SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.11114
priority: medium
status: unread
interest: medium
next_step: skim
---
# SEVO: Semantic-Enhanced Virtual Observation for Robust VLA Manipulation via Active Illumination and Data-Centric Collection
> 原文: [https://arxiv.org/abs/2605.11114](https://arxiv.org/abs/2605.11114)

arXiv:2605.11114v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) and imitation-learning policies trained via community toolchains on low-cost hardware frequently fail when deployed outside the training environment. Existing evaluations, including the original ACT and SmolVLA benchmarks, demonstrate high success rates under controlled, fixed backgrounds, yet community practitioners report near-zero transfer to new environments. We present SEVO (Semantic-Enhanced Virtual Observation), a data-centric approach that improves cross-environment manipulation robustness without modifying the policy architecture. SEVO transforms the raw RGB camera stream through three mechanisms: (1) body-fixed cameras whose combined fields of view cover the full manipulation workspace, (2) active red-spectrum illumination that physically normalizes object appearance, and (3) real-time YOLO segmentation overlay that provides a background-invariant semantic cue. Critically, we show that a diversified data collection protocol (systematically varying lighting, backgrounds, and distractors during teleoperation) is the single most important factor for generalization. We target transparent water bottles, objects that visually blend with their surroundings, and select a simple pick-and-place task to enable hundreds of controlled real-robot trials across two mobile platforms. The full pipeline achieves 95% grasp success with ACT and 83% with SmolVLA in the training environment, transferring to novel environments at 85% and 75%. Without SEVO, the same policies achieve only 75%/70% in training and collapse to 30-35% in novel environments. Our results demonstrate that principled observation design and environmental diversity during data collection, not model scaling, enable low-cost robots to operate reliably in everyday household environments.
