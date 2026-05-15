---
interest: medium
link: https://arxiv.org/abs/2605.12561
next_step: skim
priority: high
slack_ts: '1778817951.923439'
source: cs.LG - Machine Learning
status: unread
title: 'Learning When to Act: Communication-Efficient Reinforcement Learning via Run-Time
  Assurance'
---
# Learning When to Act: Communication-Efficient Reinforcement Learning via Run-Time Assurance
> 原文: [https://arxiv.org/abs/2605.12561](https://arxiv.org/abs/2605.12561)

arXiv:2605.12561v1 Announce Type: new
Abstract: Safe reinforcement learning (RL) typically asks $\textit{what}$ an agent should do. We ask $\textit{when}$ it needs to act, and show that a single policy can jointly learn control inputs and communication-efficient timing decisions under a pointwise Lyapunov safety shield. We focus on stabilization around a known equilibrium, where CARE-based LQR backups, Lyapunov certificates, and classical Lyapunov-STC are well defined, enabling clean comparison against analytical baselines. A run-time assurance (RTA) layer overrides the policy via a one-step-ahead Lyapunov prediction and a precomputed LQR backup, providing a strictly stronger guarantee than constrained MDP methods that enforce safety only in expectation. On an inverted pendulum, cart--pole, and planar quadrotor, the learned policy achieves $1.91\times$, $1.45\times$, and $3.51\times$ higher mean inter-sample interval (MSI) than a Lyapunov-triggered baseline; a fixed LQR controller at the same average rate is unstable on all three plants, showing that adaptive timing, not a lower average rate, makes sparsity safe. A CARE-derived Lyapunov reward transfers across environments without redesign, with a single weight $w\_c$ controlling the stability--communication tradeoff; ablations confirm the RTA shield is essential, with its removal reducing MSI by $1.27$--$1.84\times$ and degrading state norms. A preference-conditioned extension recovers the full tradeoff frontier from one model at $\tfrac{2}{11}$ of training compute, and SAC experiments show the results are algorithm-agnostic across discrete and continuous domains. A 12-state 3D quadrotor case study extends the framework to higher-dimensional systems where classical STC is intractable, and robustness to $\pm30\%$ mass variation and disturbances shows graceful degradation, with the RTA absorbing what the learned policy cannot.
