---
title: "VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.19370
priority: medium
status: unread
interest: medium
next_step: skim
---
# VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models
> 原文: [https://arxiv.org/abs/2603.19370](https://arxiv.org/abs/2603.19370)

arXiv:2603.19370v1 Announce Type: new
Abstract: Video action models are an appealing foundation for Vision--Language--Action systems because they can learn visual dynamics from large-scale video data and transfer this knowledge to downstream robot control. Yet current diffusion-based video predictors are trained with likelihood-surrogate objectives, which encourage globally plausible predictions without explicitly optimizing the precision-critical visual dynamics needed for manipulation. This objective mismatch often leads to subtle errors in object pose, spatial relations, and contact timing that can be amplified by downstream policies. We propose VAMPO, a post-training framework that directly improves visual dynamics in video action models through policy optimization. Our key idea is to formulate multi-step denoising as a sequential decision process and optimize the denoising policy with rewards defined over expert visual dynamics in latent space. To make this optimization practical, we introduce an Euler Hybrid sampler that injects stochasticity only at the first denoising step, enabling tractable low-variance policy-gradient estimation while preserving the coherence of the remaining denoising trajectory. We further combine this design with GRPO and a verifiable non-adversarial reward. Across diverse simulated and real-world manipulation tasks, VAMPO improves task-relevant visual dynamics, leading to better downstream action generation and stronger generalization. The homepage is https://vampo-robot.github.io/VAMPO/.
