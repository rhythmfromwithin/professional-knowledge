---
title: "Beyond Differences: Doubly Robust Meta-Learners for Ratio-Based Treatment Effects"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.26288
priority: medium
status: unread
interest: medium
next_step: skim
---
# Beyond Differences: Doubly Robust Meta-Learners for Ratio-Based Treatment Effects
> 原文: [https://arxiv.org/abs/2605.26288](https://arxiv.org/abs/2605.26288)

arXiv:2605.26288v1 Announce Type: new
Abstract: When treatment effects are naturally expressed as ratios -- as in medicine, pricing, and marketing -- the ratio-based CATE $\tau(x) = E[Y|W=1,X=x] / E[Y|W=0,X=x]$ is the appropriate estimand. Yet existing estimators either impose a log-linear parametric structure or apply generic regression without robustness guarantees for this functional. We introduce the Q-Learner, which decomposes $\tau(x)$ into a product of two odds ratios, reducing ratio-CATE estimation for binary outcomes to two propensity classification tasks. We further derive doubly robust augmentations for both S/T- and Q-style ratio learners and characterize their distinct robustness properties. In benchmarks on seven RCT datasets, the Q-Learner is the most consistently competitive method in low-conversion regimes, where its propensity-only construction sidesteps the imbalanced regression that hurts outcome-based estimators. On four observational datasets, where propensity must be estimated and confounding cannot be ruled out, the DR learners introduced here decisively come out on top, making them practitioners' natural default for confounded observational data.
