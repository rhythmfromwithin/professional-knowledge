---
interest: medium
link: https://arxiv.org/abs/2610.40723
next_step: skim
priority: medium
slack_ts: '1793597886.025199'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'INLA for Adaptive UAV Sampling of Radio Environment Maps in IoT Networks:
  Prior Width Governs Accuracy and Calibration'
---
# INLA for Adaptive UAV Sampling of Radio Environment Maps in IoT Networks: Prior Width Governs Accuracy and Calibration
> 原文: [https://arxiv.org/abs/2610.40723](https://arxiv.org/abs/2610.40723)

arXiv:2610.40723v1 Announce Type: new
Abstract: We study adaptive UAV sampling for radio environment map (REM) construction from non-Gaussian IoT observations. Integrated nested Laplace approximation(INLA) updates a Mat\'ern GMRF posterior, with waypoints selected by entropy pre-screening and Sherman--Morrison lookahead over the reachable set. We show that the likelihood-induced Skew-Normal correction has a sextic entropy effect, explaining its limited influence on waypoint selection. Across 19 retained ray-traced windows,Random and lawnmower sampling cost a median 18.0\% and 14.0\% more residual NMSE than posterior-informed sampling, equivalently reductions of 15.3\% and 12.3\% when referred to those baselines, while differences among informative rules remain unresolved. Widening the prior shadowing standard deviation from 6.0 to 10.025\,dB improves NMSE and credible-interval coverage, with monotone improvement over a 4--16\,dB sweep on this corpus and no observed turning point, although overconfidence persists. Online width estimation from the UAV's own counts yields about 6.5\,dB without recovering the gain. Across 30 measured LoRaWAN propagation windows paired with simulated counts and scored only on received cells, the margin over non-adaptive sampling reproduces, the training-derived width minimizes the tested interval score, and GP-UCB has nominally $3$--$5\%$ lower NMSE. The results show substantial, corpus-dependent sensitivity to prior specification, while fine differences among acquisition rules have limited or unresolved effects, the preferred width depends on the corpus, scored cells and model mismatch.
