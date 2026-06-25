---
interest: medium
link: https://arxiv.org/abs/2606.25111
next_step: skim
priority: medium
slack_ts: '1782360753.572039'
source: cs.RO - Robotics
status: unread
title: 'ADM-Fusion: Adaptive Deep Multi-Sensor Fusion for Robust Ego-Motion Estimation
  in Diverse Conditions'
---
# ADM-Fusion: Adaptive Deep Multi-Sensor Fusion for Robust Ego-Motion Estimation in Diverse Conditions
> 原文: [https://arxiv.org/abs/2606.25111](https://arxiv.org/abs/2606.25111)

arXiv:2606.25111v1 Announce Type: new
Abstract: Robust multi-sensor fusion is essential for reliable autonomy in diverse and degraded environments, where sensor reliability can fluctuate rapidly. Because different modalities fail in distinct ways, effective fusion should adaptively balance complementary cues rather than rely on fixed weighting. This adaptability is particularly important for ego-motion estimation, since accurate updates depend on the consistent integration of complementary sensor information. We propose ADM-Fusion, an end-to-end deep learning based multi-sensor fusion method designed to adapt to environmental changes and sensor degradation. ADM-Fusion employs an adaptive sensor mixture-of-experts framework with content-aware routing to dynamically assign weights to sensor inputs in real time. The system further incorporates separate translation and rotation branches, coupled through a cross-task attention mechanism to preserve task-specific specialization while enabling information sharing. ADM-Fusion is trained on the CARLA-LOC simulated dataset and subsequently fine-tuned on KITTI real-world data, demonstrating effective simulation-to-real transfer. Experiments show that ADM-Fusion remains robust under degraded conditions while maintaining competitive performance against existing methods.
