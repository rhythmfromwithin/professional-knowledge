---
title: "Manifold Constrained Conformal Prediction for Spatial Events"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.10008
priority: medium
status: unread
interest: medium
next_step: skim
---
# Manifold Constrained Conformal Prediction for Spatial Events
> 原文: [https://arxiv.org/abs/2607.10008](https://arxiv.org/abs/2607.10008)

arXiv:2607.10008v1 Announce Type: new
Abstract: We introduce a new conformal prediction method that constructs calibrated prediction sets over collections of spatial events, such as tropical cyclone genesis and earthquake locations. Forecasting natural hazards has become increasingly important, due to their significant economic impact, and quantifying the uncertainty of predictions is critical for accurate risk assessment. Our approach works by representing spatial point clouds as empirical measures so that we can score them using (sliced) Wasserstein distance, then constraining the resulting distribution-valued prediction set to be supported only near the training data manifold. We derive a coverage lower bound for the intersected sets and show that, in practice, this gap can be made small through a simple data-adaptive selection criterion. Because the resulting set is not analytically tractable, we introduce a modified flow-based sampling procedure, which allows us to represent and apply these prediction sets in practice as ensembles. Numerical experiments on synthetic data, tropical cyclone genesis, and earthquake occurrences show that our method achieves near-nominal coverage, with significantly lower energy distance and manifold distance than highest predictive density region (HDR) baselines along with generative model baselines.
