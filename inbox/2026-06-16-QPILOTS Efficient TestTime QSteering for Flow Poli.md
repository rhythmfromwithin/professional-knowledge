---
interest: medium
link: https://arxiv.org/abs/2606.14801
next_step: skim
priority: high
slack_ts: '1781586973.968279'
source: cs.LG - Machine Learning
status: unread
title: 'QPILOTS: Efficient Test-Time Q-Steering for Flow Policies'
---
# QPILOTS: Efficient Test-Time Q-Steering for Flow Policies
> 原文: [https://arxiv.org/abs/2606.14801](https://arxiv.org/abs/2606.14801)

arXiv:2606.14801v1 Announce Type: new
Abstract: Flow-matching and diffusion policies are expressive action generators, but optimizing them with temporal-difference reinforcement learning (RL) remains difficult. Effective policy extraction requires exploiting the critic's action gradient, yet directly backpropagating this signal through a multi-step denoising process can be numerically unstable. Existing methods work around this either by discarding gradient information, distilling the policy into a simpler one-step actor, or repeatedly fine-tuning the denoising policy as the critic improves. We propose QPILOTS, a method that leaves the original policy unmodified and steers the denoising process at inference time. At each denoising step, instead of evaluating the critic on the noisy intermediate action where critic predictions are unreliable, we first project that intermediate state to an estimate of the final clean action and compute the critic gradient there. We introduce two variants: QPILOTS-U uses a fast single-point approximation, while QPILOTS-M draws differentiable posterior samples via a learned auxiliary network. On a standard offline-to-online RL benchmark, QPILOTS achieves the best aggregate performance, reaching an average success rate of 90% across 50 tasks. We also apply QPILOTS to steer a large, frozen, pretrained Vision-Language Action (VLA) foundation model, outperforming or matching prior inference-time approaches across six manipulation tasks in simulation.
