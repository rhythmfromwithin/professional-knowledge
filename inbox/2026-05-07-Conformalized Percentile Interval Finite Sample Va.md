---
interest: medium
link: https://arxiv.org/abs/2605.03233
next_step: skim
priority: medium
slack_ts: '1778125810.049769'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Conformalized Percentile Interval: Finite Sample Validity and Improved Conditional
  Performance'
---
# Conformalized Percentile Interval: Finite Sample Validity and Improved Conditional Performance
> 原文: [https://arxiv.org/abs/2605.03233](https://arxiv.org/abs/2605.03233)

arXiv:2605.03233v1 Announce Type: new
Abstract: Conformal prediction provides distribution-free predictive intervals with finite-sample marginal coverage. However, achieving conditional validity and interval efficiency (in terms of short interval length) remains challenging, particularly in complex settings with heteroskedasticity, skewed responses, or estimation errors. We propose a conformal-style calibration method for responses obtained by the probability integral transform (PIT) of the conditional cumulative distribution function (CDF) estimated via neural networks to construct a finite-sample-adjusted percentile interval with the shortest length determined by the estimated conditional CDF. Calibrating in PIT space is effective because PIT values are asymptotically feature-independent when the CDF estimator is accurate, which mitigates feature-dependent miscoverage and improves conditional calibration. On the other hand, our percentile calibration adapts to the empirical PIT distribution, which is robust against a possibly imperfect estimation of the conditional CDF. We prove the finite-sample marginal coverage property of the proposed method and show its asymptotic conditional coverage under mild consistency conditions. Experiments on diverse synthetic and real-world benchmarks demonstrate better conditional calibration and substantially shorter intervals than existing methods.
