---
title: "Verifiable Foundation Models for Robot Safety"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2606.23754
priority: medium
status: unread
interest: medium
next_step: skim
---
# Verifiable Foundation Models for Robot Safety
> 原文: [https://arxiv.org/abs/2606.23754](https://arxiv.org/abs/2606.23754)

arXiv:2606.23754v1 Announce Type: new
Abstract: Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. In this paper, we present FEARL (Foundation-Enabled Assured Robot Learning), a framework that addresses this tension through a modular architectural decomposition. FEARL separates the policy into a large Controller (C) responsible for high-dimensional perception and task reasoning, and a small Safety module (S) that receives low-dimensional observations from dedicated safety sensors together with a bounded context embedding from C and produces the final action. Since many robot safety requirements, such as collision avoidance and workspace boundary constraints, can be expressed over these safety sensor observations, formal verification can be applied to S rather than to the full foundation-model backbone. This makes formal analysis tractable with existing tools while preserving the Controller's expressive power for task reasoning. To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. We further transfer the learned policy from one of our simulated tasks to a physical robot, suggesting that the low-dimensional safety interface supports practical sim-to-real transfer.
