---
title: "Fair regression under localized demographic parity constraints"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.25224
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fair regression under localized demographic parity constraints
> 原文: [https://arxiv.org/abs/2603.25224](https://arxiv.org/abs/2603.25224)

arXiv:2603.25224v1 Announce Type: new
Abstract: Demographic parity (DP) is a widely used group fairness criterion requiring predictive distributions to be invariant across sensitive groups. While natural in classification, full distributional DP is often overly restrictive in regression and can lead to substantial accuracy loss. We propose a relaxation of DP tailored to regression, enforcing parity only at a finite set of quantile levels and/or score thresholds. Concretely, we introduce a novel (${\ell}$, Z)-fair predictor, which imposes groupwise CDF constraints of the form F f |S=s (z m ) = ${\ell}$ m for prescribed pairs (${\ell}$ m , z m ). For this setting, we derive closed-form characterizations of the optimal fair discretized predictor via a Lagrangian dual formulation and quantify the discretization cost, showing that the risk gap to the continuous optimum vanishes as the grid is refined. We further develop a model-agnostic post-processing algorithm based on two samples (labeled for learning a base regressor and unlabeled for calibration), and establish finite-sample guarantees on constraint violation and excess penalized risk. In addition, we introduce two alternative frameworks where we match group and marginal CDF values at selected score thresholds. In both settings, we provide closed-form solutions for the optimal fair discretized predictor. Experiments on synthetic and real datasets illustrate an interpretable fairness-accuracy trade-off, enabling targeted corrections at decision-relevant quantiles or thresholds while preserving predictive performance.
