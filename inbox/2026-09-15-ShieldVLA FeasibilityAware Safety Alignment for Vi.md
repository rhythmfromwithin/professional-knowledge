---
interest: medium
link: https://arxiv.org/abs/2609.13231
next_step: skim
priority: medium
slack_ts: '1789532922.380469'
source: cs.RO - Robotics
status: unread
title: 'ShieldVLA: Feasibility-Aware Safety Alignment for Vision-Language-Action Models'
---
# ShieldVLA: Feasibility-Aware Safety Alignment for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2609.13231](https://arxiv.org/abs/2609.13231)

arXiv:2609.13231v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models demonstrate strong generalization in robotic manipulation and navigation, but existing fine-tuning methods provide limited safety guarantees. Current approaches primarily rely on Lagrangian optimization that enforces safety through soft penalties on expected cumulative cost, often resulting in residual constraint violations or overly conservative behavior. Moreover, learning safety in visual domains is challenging due to the absence of dense per-step safety annotations. We propose ShieldVLA, a safety-aligned fine-tuning framework for VLA models based on Hamilton-Jacobi (HJ) reachability. ShieldVLA learns a model-free approximation of the HJ reachability value function directly from visual observations to estimate the safe operating region. The learned safety critic gates policy optimization by separating reward maximization within feasible regions from recovery near unsafe states, avoiding persistent reward-cost trade-offs. To enable scalable supervision in visual environments, we introduce rubric-based VLM safety scores that convert semantic safety feedback into structured critic targets without requiring manual cost labels. Across five navigation and manipulation benchmarks spanning multiple VLA backbones, ShieldVLA reduces cumulative safety cost by 57% on average and improves task success rate by +0.13 over SafeVLA.
