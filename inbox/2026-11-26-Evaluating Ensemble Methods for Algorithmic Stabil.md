---
interest: medium
link: https://arxiv.org/abs/2611.33375
next_step: skim
priority: medium
slack_ts: '1795850662.202989'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Evaluating Ensemble Methods for Algorithmic Stability Under Data Perturbations
---
# Evaluating Ensemble Methods for Algorithmic Stability Under Data Perturbations
> 原文: [https://arxiv.org/abs/2611.33375](https://arxiv.org/abs/2611.33375)

arXiv:2611.33375v1 Announce Type: new
Abstract: Standard classification algorithms often exhibit sensitivity near decision boundaries, which can compound instability that already exists from overfitting to a subset of high-influence samples. Ensembling is commonly used to stabilize classifiers, but we show that it can destabilize those that are already stable. The well-established practice of subbagging can yield substantial improvements in stability, as we validate in the cause-of-death classification setting. However, its effect depends on the perturbation level, and for stable classifiers the finite number of bags introduces destabilizing Monte Carlo noise that shrinks only slowly as the number of bags grows. This instability can be mitigated, though, by the recently proposed inflated argmax, which allows for multi-class predictions in ambiguous cases. We further examine the extent to which the Rashomon set, the collection of distinct models that achieve near-optimal predictive performance, can reduce instability by leveraging predictive multiplicity rather than resampling. We find that the Rashomon ensemble can stabilize unstable classifiers, but requires sufficient predictive multiplicity, which is not guaranteed. It is a promising direction, but not currently a general substitute for subbagging. Our results are consistent with an influence equalization interpretation of why these ensemble approaches stabilize unstable classifiers, although their failures on stable classifiers appear to have distinct sources.
