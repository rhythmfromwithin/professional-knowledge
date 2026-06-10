---
interest: medium
link: https://arxiv.org/abs/2606.10129
next_step: skim
priority: low
slack_ts: '1781065404.022439'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Discovering Interpretable Multi-Parameter Control Policies for Evolutionary
  Algorithms Using Deep Reinforcement Learning
---
# Discovering Interpretable Multi-Parameter Control Policies for Evolutionary Algorithms Using Deep Reinforcement Learning
> 原文: [https://arxiv.org/abs/2606.10129](https://arxiv.org/abs/2606.10129)

arXiv:2606.10129v1 Announce Type: cross
Abstract: While deep Reinforcement Learning (deep-RL) has been increasingly applied to parameter control in evolutionary algorithms, rigorous theoretical analysis of parameter control remains largely restricted to single-parameter settings, owing to the difficulty of deriving effective, interpretable multi-parameter policies amenable to formal study. We demonstrate how deep-RL can be leveraged to overcome this barrier, using the (1+($\lambda$,$\lambda$))-genetic algorithm optimizing OneMax, one of the few problems where a super-constant speedup of dynamic control has been formally proven, as a representative case study. We first show that standard approaches struggle to converge in this multi-parameter setting, and introduce algorithm-agnostic enhancements targeting action-space decomposition, reward shifting, and long-horizon discounting. With these in place, we compare common deep-RL methods and find that Double Deep Q-Networks uniquely avoid the policy collapse observed in Proximal Policy Optimization, yielding trajectories suitable for downstream analysis. Crucially, we move beyond the ``black-box'' nature of neural networks by distilling the learned behaviors into a transparent, symbolic control policy. This resulting policy does not only offer interpretability for future theoretical analysis but also yields exceptional performance, consistently outperforming existing baselines across a wide range of problem sizes.
