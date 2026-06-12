---
interest: medium
link: https://arxiv.org/abs/2606.12499
next_step: skim
priority: medium
slack_ts: '1781239678.912399'
source: cs.RO - Robotics
status: unread
title: Action-Effect Memory Pretraining for Robot Manipulation
---
# Action-Effect Memory Pretraining for Robot Manipulation
> 原文: [https://arxiv.org/abs/2606.12499](https://arxiv.org/abs/2606.12499)

arXiv:2606.12499v1 Announce Type: new
Abstract: We present AEM, an Action-Effect Memory pretraining framework for robot manipulation that learns compact temporal representations from vision-action history. Unlike prior robot representation pretraining methods that mainly focus on single-frame visual encoding, AEM targets the temporal nature of manipulation, where the current observation alone is often insufficient under partial observability. AEM models manipulation as an action-driven interaction process by interleaving visual and action features and applying masked modeling to recover missing content from incomplete histories, thereby learning action-conditioned state evolution. The Mamba-encoded output of the final vision token is used as a compact history representation, serving as the global context for decoding and downstream control. This design preserves a single-vector temporal bottleneck while keeping inference efficient. We evaluate AEM with Diffusion Policy and Flow Policy. AEM consistently improves manipulation performance in both simulation and real-world settings, outperforming baselines across clean scenes, cluttered and random scenes, and non-Markovian tasks. Ablation studies further show that history-aware pretraining surpasses single-frame pretraining and direct frame stacking, while reducing inference latency and computational cost.
