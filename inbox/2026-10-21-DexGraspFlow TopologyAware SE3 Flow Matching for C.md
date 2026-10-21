---
title: "DexGraspFlow: Topology-Aware SE(3) Flow Matching for Cross-Embodiment Dexterous Grasp Generation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.26962
priority: medium
status: unread
interest: medium
next_step: skim
---
# DexGraspFlow: Topology-Aware SE(3) Flow Matching for Cross-Embodiment Dexterous Grasp Generation
> 原文: [https://arxiv.org/abs/2610.26962](https://arxiv.org/abs/2610.26962)

arXiv:2610.26962v1 Announce Type: new
Abstract: Differences in hand geometry, joint parameterization, and kinematic topology pose challenges for cross-embodiment dexterous grasp generation. However, spatial relations among links alone are insufficient to fully capture the hand's kinematic topology. We propose DexGraspFlow, a conditional link-level $\mathrm{SE}(3)$ flow-matching framework integrating geometric relations and kinematic topology. The framework encodes local object geometry, link geometry, and current poses. A dual-stream DiT models link--link coordination and link--object interaction, while attention biases derived from kinematic-tree distances provide explicit structural information for modeling evolving geometric interactions. The model jointly learns translational and rotational velocity fields, integrates them to generate link poses, and recovers joint configurations through inverse kinematics. Additionally, inference-time palm-orientation guidance enables controllable grasp generation without retraining. Across three robotic hands and 30 object--hand pairs, DexGraspFlow achieves a 95.33\% average simulation success rate, with an average generation latency, including inverse kinematics, approximately 49\% lower than that of a state-of-the-art baseline. Further experiments demonstrate zero-shot adaptability to seven finger-removal variants and palm-orientation control. A model trained on demonstrations for the deployed hand achieves a 91\% success rate over 100 real-robot grasping trials, supporting the framework's applicability to physical grasp execution.
