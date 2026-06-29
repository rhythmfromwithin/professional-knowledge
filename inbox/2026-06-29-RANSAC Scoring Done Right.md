---
interest: medium
link: https://arxiv.org/abs/2606.27385
next_step: skim
priority: high
slack_ts: '1782708431.550099'
source: cs.LG - Machine Learning
status: unread
title: RANSAC Scoring Done Right
---
# RANSAC Scoring Done Right
> 原文: [https://arxiv.org/abs/2606.27385](https://arxiv.org/abs/2606.27385)

arXiv:2606.27385v1 Announce Type: new
Abstract: The most widely used RANSAC variants score candidate models by counting inliers or summing per-point scores that saturate beyond a residual threshold. Every such score requires a user-supplied parameter that is a function of the inlier scale, which must itself be estimated from contaminated data. We remove this dependence by reversing the usual order of inference: rather than estimating the scale and then scoring against it, we marginalize the inlier scale analytically in closed form under a conjugate Inverse-Gamma prior for a fixed inlier partition, then optimize over partitions. A single closed-form expression spans the non-informative Jeffreys limit and informative empirical-Bayes priors, so the same score adapts across data-rich and data-scarce regimes without any change to the algorithm. The proposed RANSAC score is the first in which the inlier scale is genuinely absent from the formula. The score admits O(N log N ) computation via sort-and-sweep. On a benchmark of nearly 70 000 image pairs spanning different two-view estimation problems and both engineered and learned feature pipelines, the proposed score exceeds the state of the art (RANSAC, MSAC, GaU, MAGSAC): it stays nearly flat under threshold miscalibration where baselines degrade, reaches near-optimal accuracy from as few as two validation pairs where baselines need ont he order of 100 times more,. and tightens its prior regularization as validation data grows scarce.
