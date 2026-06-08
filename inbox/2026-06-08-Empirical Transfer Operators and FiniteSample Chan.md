---
interest: medium
link: https://arxiv.org/abs/2606.06785
next_step: skim
priority: medium
slack_ts: '1780894165.513939'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Empirical Transfer Operators and Finite-Sample Change Detection for Noisy Expanding
  Interval Maps
---
# Empirical Transfer Operators and Finite-Sample Change Detection for Noisy Expanding Interval Maps
> 原文: [https://arxiv.org/abs/2606.06785](https://arxiv.org/abs/2606.06785)

arXiv:2606.06785v1 Announce Type: new
Abstract: We study finite-sample change detection for one-dimensional noisy dynamical systems using partition-based empirical approximations of stationary behaviour. Given observations from an interval-valued process, we partition the state space, estimate a finite transition matrix from observed transitions between partition elements, and apply a small Doeblin-type regularisation to ensure a unique stationary distribution.
From an initial reference segment, we compute a baseline empirical stationary distribution \(\widehat{\pi}\_{0,\rho}\). For each later sliding window, we compute \(\widehat{\pi}\_{t,\rho}\) and define the score \[ S\_t=\|\widehat{\pi}\_{t,\rho}-\widehat{\pi}\_{0,\rho}\|\_1. \] Large values of \(S\_t\) indicate a change in stationary behaviour relative to the baseline. The statistic detects changes in invariant density or stationary law, but not all possible changes in transition dynamics.
Under explicit assumptions on empirical transition concentration, finite-state stationary distribution stability, partition approximation, regularisation bias, and noise stability, we derive a finite-sample bound for the empirical stationary density. The bound separates sampling error, regularisation bias, partition approximation error, and noise bias. We then obtain a single-window false-alarm guarantee and a sufficient detection condition when the invariant density changes by more than the estimation error. We illustrate the method on synthetic noisy beta-map change-point experiments.
