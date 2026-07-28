---
interest: medium
link: https://arxiv.org/abs/2607.20653
next_step: skim
priority: medium
slack_ts: '1785208694.389969'
source: cs.RO - Robotics
status: unread
title: 'PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable
  Dynamics'
---
# PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics
> 原文: [https://arxiv.org/abs/2607.20653](https://arxiv.org/abs/2607.20653)

arXiv:2607.20653v1 Announce Type: new
Abstract: Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge. Existing approaches typically rely on per-object optimization to fit material parameters, which can be slow and cannot generalize, while end-to-end learned alternatives extrapolate poorly and often violate basic physical structure. We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks. A material refinement module, Material from Motion (MfM), infers per-particle elasticity from visual observations, grounding the simulator in object-specific physics. A residual correction module, Residual from Dynamics (RfD), learns the discrepancy and predicts corrections to the simulator's internal dynamics, absorbing systematic biases that the analytical model cannot capture. This design also supports online material identification on novel objects. MfM adapts from limited interactions, and its predictive uncertainty steers further exploration toward the regions where its estimate is least confident. Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural signal for future confidence-guided exploration.
