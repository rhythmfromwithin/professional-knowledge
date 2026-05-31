---
interest: medium
link: https://arxiv.org/abs/2605.28849
next_step: skim
priority: high
slack_ts: '1780202383.101329'
source: cs.AI - Artificial Intelligence
status: unread
title: Behavior-Induced Mirror-Prox Temporal-Difference Learning for Faster Off-Policy
  Prediction
---
# Behavior-Induced Mirror-Prox Temporal-Difference Learning for Faster Off-Policy Prediction
> 原文: [https://arxiv.org/abs/2605.28849](https://arxiv.org/abs/2605.28849)

arXiv:2605.28849v1 Announce Type: new
Abstract: Gradient temporal-difference methods provide stable off-policy prediction with linear function approximation, but their practical performance is strongly affected by the geometry induced by the auxiliary-variable metric. Existing Mirror-Prox TD methods typically use the feature covariance metric, whereas hybrid TD methods suggest that behavior-policy transition information can provide a more informative update geometry. This paper proposes a behavior-induced Mirror-Prox temporal-difference method, called STHTD-MP, which replaces the covariance metric in the primal-dual saddle-point formulation with the symmetric part of the behavior-policy Bellman matrix. The method keeps a single learning rate for the primal and auxiliary variables and applies a Mirror-Prox prediction-correction step to the resulting hybrid saddle-point operator. We provide a formal convergence analysis for fixed-policy linear prediction under standard stochastic approximation assumptions: the behavior-induced metric is positive definite, the joint mean system is Hurwitz, boundedness follows from a Lyapunov argument, and the stochastic recursion converges by the ODE method. We further derive projected-oracle ergodic gap bounds and an exact mean-operator comparison with GTD2-MP based on the spectral radius of the deterministic Mirror-Prox error matrix. The analysis shows that STHTD-MP can have a smaller mean contraction factor than GTD2-MP when the behavior-induced metric improves the saddle-point geometry. Exact numerical mean-operator analysis on two-state, Random Walk, and Boyan Chain benchmarks supports this condition, while Baird's counterexample is identified as a singular boundary case where the strict assumptions fail.
