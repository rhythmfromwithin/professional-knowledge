---
title: "DeViGrasp: Robust Visual Mobile Grasping for Quadruped Manipulators under Degraded Perception"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.22278
priority: medium
status: unread
interest: medium
next_step: skim
---
# DeViGrasp: Robust Visual Mobile Grasping for Quadruped Manipulators under Degraded Perception
> 原文: [https://arxiv.org/abs/2609.22278](https://arxiv.org/abs/2609.22278)

arXiv:2609.22278v1 Announce Type: new
Abstract: Quadruped manipulators enable mobile grasping in complex environments, yet their whole-body control policies remain vulnerable to unreliable onboard visual perception. Existing methods are typically developed under relatively reliable observations and have not systematically examined how occlusion, segmentation-mask dropout, depth noise, and target-localization jitter affect grasp reasoning and target tracking. To address this gap, we introduce DeViGrasp-Bench, a benchmark for mobile grasping under degraded vision that incorporates controlled visual degradations, seen and unseen objects, multiple difficulty levels, and complex terrains, and evaluates task success, execution efficiency, and action smoothness. We further propose DeViGrasp-Net, a teacher--student framework that combines state-conditioned grasp reasoning with reliability-aware temporal target estimation. The privileged teacher attends to offline grasp candidates conditioned on object, robot, end-effector, and task states, while the deployable student fuses dual-view segmented-depth observations with current, memory, and recovery target hypotheses through Target Hold Memory and Temporal Memory Attention. DeViGrasp-Net outperforms VBC across degradation levels, unseen objects, and complex terrains, and surpasses an adapted DQ-Net across all evaluated degradation levels. Under the Difficult setting, it achieves a success rate of 62.3\%, improving upon VBC and DQ-Net by 16.1 and 4.3 percentage points, respectively; under the Hard setting, its margin over DQ-Net increases to 10.5 percentage points. Ablation studies confirm the complementary benefits of grasp-aware supervision and reliability-aware temporal memory.
