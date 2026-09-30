---
interest: medium
link: https://arxiv.org/abs/2609.32026
next_step: skim
priority: medium
slack_ts: '1790745126.961669'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Continuous-Time Trajectory Generation from Discrete Observations with Stochasticity
---
# Continuous-Time Trajectory Generation from Discrete Observations with Stochasticity
> 原文: [https://arxiv.org/abs/2609.32026](https://arxiv.org/abs/2609.32026)

arXiv:2609.32026v1 Announce Type: new
Abstract: Physical systems evolve continuously in time, yet their states are typically observed only at discrete times. Generating trajectories consistent with their probability densities from such observations therefore requires capturing the continuous-time evolution rather than only learning transition mappings between consecutive observations. We propose PhiBE-Flow, a framework that directly estimates the probability velocity field induced by the stochastic differential equation (SDE) which governs this continuous-time distributional evolution. PhiBE-Flow learns from discrete observations using a model-free approach requiring neither known SDE coefficients nor score estimation. We establish convergence guarantees for the method, accounting for both time-discretization and finite-sample errors. We evaluate PhiBE-Flow on systems of increasing complexity, from controlled stochastic numerical systems to Navier--Stokes dynamics and real-world videos. Our results show that PhiBE-Flow accurately recovers probability flows of stochastic dynamics, preserves multiscale physical statistics, and improves video generation performance over representative baselines. The code is available at https://github.com/R1fe/PhiBE-Flow.
