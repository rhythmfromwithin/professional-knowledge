---
interest: medium
link: https://arxiv.org/abs/2611.22759
next_step: skim
priority: medium
slack_ts: '1794985140.114869'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Robust Actor-Critic Learning under Transport and Divergence Uncertainty
---
# Robust Actor-Critic Learning under Transport and Divergence Uncertainty
> 原文: [https://arxiv.org/abs/2611.22759](https://arxiv.org/abs/2611.22759)

arXiv:2611.22759v1 Announce Type: new
Abstract: Learning reliable control policies requires accounting for uncertainty in transition dynamics and errors introduced by function estimation and action generation. We develop an actor--critic method for discounted robust Markov decision processes with continuous states and actions and an unknown nominal transition law. We consider transition uncertainty sets defined by Wasserstein distance, total variation, Kullback--Leibler divergence, or Pearson chi-square divergence. A conditional diffusion model is fitted once to offline transitions. At each subsequent iteration, we estimate the robust action-value function from current-policy observations using a shared-target minimax criterion, then update a generative actor through exponentially weighted score matching. Regularization preserves exploration and provides the density regularity needed for conditional distribution estimation. Under coverage and regularity conditions, we establish finite-sample bounds for critic estimation, the learned conditional action law, and the robust return of the implemented policy. The bounds distinguish critic estimation error, uncertainty in the nominal transition model, and policy regularization, and characterize how the four robustness radii affect the resulting guarantees.
