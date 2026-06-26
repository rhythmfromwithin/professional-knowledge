---
interest: medium
link: https://arxiv.org/abs/2606.26168
next_step: skim
priority: high
slack_ts: '1782447549.329109'
source: cs.LG - Machine Learning
status: unread
title: 'Implementation of reinforcement learning in chemical reaction networks: application
  to phototaxis as curiosity-driven exploration'
---
# Implementation of reinforcement learning in chemical reaction networks: application to phototaxis as curiosity-driven exploration
> 原文: [https://arxiv.org/abs/2606.26168](https://arxiv.org/abs/2606.26168)

arXiv:2606.26168v1 Announce Type: new
Abstract: Living systems navigate environments using noisy and incomplete sensory signals. In unicellular algae, phototaxis is often modeled as a mechanistic run--tumble process driven by stimulus--response rules. However, such descriptions overlook how organisms actively sample their environment to reduce sensory ambiguity. From a minimal cognition perspective, we reframe this navigation as a subjective, information-driven sensorimotor process. To this end, we propose a framework linking a Partially Observable Markov Decision Process (POMDP) with biochemical reaction dynamics. Environmental variables are hidden, while the cell updates a minimal internal state from each observation through a memoryless Bayesian step. These internal dynamics balance orienting toward light with exploratory reorientation and can be implemented through Chemical-Reaction-Network Ordinary Differential Equations (CRN--ODEs). Our model includes a biophysical observation process for photoreception and a chemically computable polynomial bound on information gain. Using Inverse Reinforcement Learning (IRL) on 30 experimentally recorded Chlamydomonas trajectories, we infer the behavioral objective consistent with observed phototactic motion and benchmark the resulting dynamics with standard Stochastic Simulation Algorithm (SSA) baselines. Our model reproduces the empirical alignment-to-light distribution, comparable to objective SSA baselines on this dataset. Within this framework, run--tumble alternation emerges as an information-acquisition strategy: tumbling reorients the cell to sample new sensory configurations and resolve sensor ambiguity, demonstrating how intracellular biochemical networks can support adaptive information-seeking behavior in cellular navigation.
