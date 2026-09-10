---
interest: medium
link: https://arxiv.org/abs/2609.09210
next_step: skim
priority: medium
slack_ts: '1789013737.951509'
source: cs.RO - Robotics
status: unread
title: Identifying Habit, Physics, and Nuisance in Robot World Models
---
# Identifying Habit, Physics, and Nuisance in Robot World Models
> 原文: [https://arxiv.org/abs/2609.09210](https://arxiv.org/abs/2609.09210)

arXiv:2609.09210v1 Announce Type: new
Abstract: Teleoperated demonstrations are often multimodal even when the underlying dynamics are nearly deterministic given the executed action. We argue that this multimodality typically mixes three factors--operator habit in action selection, shared physics, and observation nuisance--and that entangled next-observation predictors absorb all three. We formalize the split with a structural causal model a=g(h,z,u), z'=f(z,a), o=r(z,c), and test it with complementary interventions: replacing or shuffling actions at fixed state sharply increases next-state error, whereas appearance and camera changes should not; habit-aware reverse scoring improves ranking of feasible pasts without rewriting the dynamics. The associated adaptation rule is to freeze a shared physics readout and update only a thin interface. On StackCube, DROID, and RH20T this rule improves low-shot transfer relative to training from scratch, retains cleaner dynamics under corrupted adaptation data, and extends from proprioception to pixel observations with multi-view and multi-step checks. We do not equate latent actions with operator habit, and we do not target large-scale video generation benchmarks.
