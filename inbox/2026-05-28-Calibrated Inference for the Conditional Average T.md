---
interest: medium
link: https://arxiv.org/abs/2605.27473
next_step: skim
priority: medium
slack_ts: '1780113871.743129'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Calibrated Inference for the Conditional Average Treatment Effect in the Few-Placebo
  Regime via Gaussian Processes
---
# Calibrated Inference for the Conditional Average Treatment Effect in the Few-Placebo Regime via Gaussian Processes
> 原文: [https://arxiv.org/abs/2605.27473](https://arxiv.org/abs/2605.27473)

arXiv:2605.27473v1 Announce Type: new
Abstract: Estimating how much an intervention helps a given individual the conditional average treatment effect (CATE) is increasingly central to decision-making in medicine, economics, and policy, where an estimate is most useful when accompanied by a calibrated uncertainty interval. We study the few-placebo regime, in which one treatment arm is much smaller than the other, as arises in unequal-allocation trials and small-holdout $A/B$ tests. The standard estimator in this setting is the X-Learner, and a natural way to obtain credible intervals is to make its second stage Bayesian. We show that these intervals under-cover: they contain the true effect less often than their nominal level. We trace this to a structural cause the X-Learner's regression target inherits the bias of a nuisance model fitted to the small arm, so the posterior is centered away from the true effect and we find that the standard remedy, regressing an orthogonal doubly-robust score, is also unreliable here, since the regime's limited overlap leaves the estimator either highly variable or, once stabilized, biased once more. Both consequences reflect a pattern that extends beyond causal inference: a separately estimated variance is attached to a point estimate of a hard-to-learn quantity, and the point estimate's bias is not captured by that variance. We propose GP-CATE, which models each arm's outcome surface with a Gaussian process, so the scarce arm's uncertainty enters the posterior directly rather than as an unmodelled bias. Across synthetic and semi-synthetic benchmarks, GP-CATE attains calibrated coverage where the estimators we compare against including Causal Forest and BART do not, at the cost of intervals that are appropriately wide when the data are uninformative.
