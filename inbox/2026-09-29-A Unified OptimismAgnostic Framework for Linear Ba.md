---
title: "A Unified Optimism-Agnostic Framework for Linear Bandits over Spherical Action Sets"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.32149
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Unified Optimism-Agnostic Framework for Linear Bandits over Spherical Action Sets
> 原文: [https://arxiv.org/abs/2609.32149](https://arxiv.org/abs/2609.32149)

arXiv:2609.32149v1 Announce Type: new
Abstract: Linear bandits model sequential decision-making problems with noisy rewards that are linear in the decision variable, where an agent must simultaneously learn about an unknown parameter that governs the mean rewards, while maximizing (expected) rewards over time. Two prominent algorithmic families--upper confidence bound (UCB) and Thompson sampling (TS)--achieve a balance of exploration (to estimate said parameter) and exploitation (utilization of knowledge about it) across time. The quality of estimation of that parameter depends on the eigenvalues of a design matrix. In this paper, we begin by showing that if the inference quality obtained from exploration, encoded in the minimum eigenvalue of the design matrix, grows $\gtrsim \sqrt{t}$ with time $t$, while actions remain sufficiently concentrated for exploitation, then an algorithm produces optimal high-probability $\mathcal{O}(\sqrt{T}\log T)$-regret rate over a time-horizon $T$ for spherical action sets. This analysis is algorithm-agnostic and follows an alternative route to the classical optimism-based elliptical-potential argument for regret analysis. Then, we illustrate that variants of UCB and TS satisfy the inference and concentration properties and in turn, enjoy optimal regret rate. In effect, our results provide a modular framework that can be used to analyze linear bandit algorithms and explicitly connect quality of parameter estimation to optimal regret accumulation.
