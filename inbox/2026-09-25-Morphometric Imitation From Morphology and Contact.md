---
title: "Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.28660
priority: medium
status: unread
interest: medium
next_step: skim
---
# Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy
> 原文: [https://arxiv.org/abs/2609.28660](https://arxiv.org/abs/2609.28660)

arXiv:2609.28660v1 Announce Type: new
Abstract: Human hand-object interactions (HOIs) provide a rich source of demonstrations for dexterous manipulation, but learning directly from them presents challenges in bridging morphology gaps, ensuring dynamical feasibility, and sim-to-real deployment. We present Morphometric Imitation, a three-stage framework that transforms reconstructed HOIs into zero-shot sim-to-real visuomotor policies. First, morphometric optimization (MMO) kinematically retargets human motion across hand morphologies while preserving demonstrated contacts. Second, residual reinforcement learning (RL) refines the kinematic reference using object pose and contact information from the human motion to produce dynamically feasible robot demonstrations. Third, these demonstrations are distilled into visuomotor policies. Across three robot hands and ten HOIs, MMO improves contact F1 over the strongest of five baselines by at least 8 points for every hand, while also improving the success rate of downstream dynamic retargeting by as much as 35 points. Ablations on the residual RL show complementary benefits from using object pose and contact information. Finally, the visuomotor policies achieve 89.3% zero-shot success in 300 real-world trials on 30 objects. Project page: $\href{https://morphometricimitation.github.io}{\text{this https URL}}$
