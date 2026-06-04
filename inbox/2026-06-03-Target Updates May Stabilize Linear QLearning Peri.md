---
interest: medium
link: https://arxiv.org/abs/2606.02645
next_step: skim
priority: medium
slack_ts: '1780548667.545099'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Target Updates May Stabilize Linear Q-Learning: Periodic and Soft Dynamics'
---
# Target Updates May Stabilize Linear Q-Learning: Periodic and Soft Dynamics
> 原文: [https://arxiv.org/abs/2606.02645](https://arxiv.org/abs/2606.02645)

arXiv:2606.02645v1 Announce Type: new
Abstract: Periodic target updates in Q-learning and soft target updates in actor-critic methods are empirically well established stabilization mechanisms, but their precise theoretical explanation is still incomplete. This paper gives a rigorous and exact analysis of these mechanisms for Q-learning with linear function approximation (linear Q-learning) using the exact switched linear system (SLS) dynamics induced by the Bellman maximum and the joint spectral radius (JSR) of the resulting switching matrix families. Although linear Q-learning can fail to converge in general, we prove that, under explicit spectral and step-size conditions, periodic hard target updates and soft target updates can guarantee convergence to the exact projected Q-Bellman solution. The main analysis is carried out for deterministic linear Q-learning, where the target-update mechanism is most transparent. Once the corresponding JSR certificate is established for the mean recursion, the stochastic reinforcement-learning setting can be treated by replacing deterministic modes with sampled stochastic modes and adding the corresponding stochastic-noise analysis.
