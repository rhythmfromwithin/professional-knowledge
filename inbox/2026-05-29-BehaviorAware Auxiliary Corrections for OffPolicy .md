---
interest: medium
link: https://arxiv.org/abs/2605.28855
next_step: skim
priority: high
slack_ts: '1780028399.281859'
source: cs.AI - Artificial Intelligence
status: unread
title: Behavior-Aware Auxiliary Corrections for Off-Policy Temporal-Difference Prediction
---
# Behavior-Aware Auxiliary Corrections for Off-Policy Temporal-Difference Prediction
> 原文: [https://arxiv.org/abs/2605.28855](https://arxiv.org/abs/2605.28855)

arXiv:2605.28855v1 Announce Type: new
Abstract: Temporal-difference learning with function approximation can be unstable under off-policy sampling. TDC stabilizes off-policy TD through an auxiliary covariance correction, and TDRC further regularizes this correction in a single-timescale recursion. This paper studies a behavior-aware replacement of the auxiliary covariance geometry in the linear prediction setting, which is the standard local model for understanding the feature-space dynamics of value-function approximation. We first replace the TDC auxiliary matrix (C) by the behavior Bellman matrix (A\_\mu), yielding BA-TDC, and then regularize the same behavior-aware equation to obtain BA-TDRC. This two-step construction separates the contribution of behavior-aware geometry from the contribution of regularization. The linear analysis also provides a tractable model for an auxiliary-geometry design question that arises in neural-network value approximation, where feature covariances and temporal transition matrices jointly shape the last-layer correction dynamics. We give a finite-state mean-system formulation, prove fixed-point preservation and almost-sure convergence under a Hurwitz stability condition on the instantiated mean system, and compare deterministic mean rates through the spectral radius of the exact linear error recursion. Experiments on the two-state counterexample, Baird's counterexample, Random Walk, and Boyan Chain show that the behavior-aware replacement can be highly beneficial by itself on some tasks, but that regularization is necessary for robust performance across harder settings.
