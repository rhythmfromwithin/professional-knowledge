---
interest: medium
link: https://arxiv.org/abs/2608.17173
next_step: skim
priority: medium
slack_ts: '1787362732.952649'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Policy Optimization and Statistical Inference for Online Contextual Matrix
  Games
---
# Policy Optimization and Statistical Inference for Online Contextual Matrix Games
> 原文: [https://arxiv.org/abs/2608.17173](https://arxiv.org/abs/2608.17173)

arXiv:2608.17173v1 Announce Type: new
Abstract: Online decision making often requires navigating a landscape shaped by both dynamic contexts and strategic interactions. In competitive pricing, for example, hotels must account for both dynamic contextual factors and rivals' strategic responses. Existing approaches address only part of this challenge: contextual bandits optimize single-agent decisions using observable features but ignore multi-player interactions, while online matrix games capture strategic behavior through Nash equilibrium but assume fixed payoffs, ignoring contextual information. How should agents act then when strategic payoffs evolve with contextual signals? We introduce \emph{online contextual matrix games} to integrate contextual information into multi-player online games. We further propose \emph{OnGameLearn}, an online learning algorithm that efficiently balances exploration and exploitation across both player actions and contexts. This approach comes with statistical guarantees: tail bounds for the estimated payoff matrix, the convergence of the estimated Nash equilibrium, the asymptotic normality of the parameter estimators, and the sublinear regret bound. We also develop the notion of \emph{policy value} in matrix games and develop a doubly robust, $\sqrt{T}$-consistent estimator for it. Across simulated studies and a real-world hotel pricing application, we find that OnGameLearn effectively navigates the intertwined challenges of strategic and contextual decision-making.
