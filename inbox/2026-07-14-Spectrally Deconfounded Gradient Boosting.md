---
interest: medium
link: https://arxiv.org/abs/2607.09371
next_step: skim
priority: medium
slack_ts: '1783998921.052299'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Spectrally Deconfounded Gradient Boosting
---
# Spectrally Deconfounded Gradient Boosting
> 原文: [https://arxiv.org/abs/2607.09371](https://arxiv.org/abs/2607.09371)

arXiv:2607.09371v1 Announce Type: new
Abstract: Flexible machine-learning methods can be sensitive to hidden confounding: they may learn associations induced by unobserved confounders rather than stable signals. Spectral deconfounding mitigates this problem by shrinking high-variance directions of the covariate matrix that, under dense confounding, carry latent confounder information. Existing work has largely focused on linear models. We develop a nonlinear spectral deconfounding framework for gradient boosting. Our approach replaces the ordinary squared-error loss by a spectral loss, which alters the boosting dynamics by slowing down learning in confounding-aligned directions. We show that deconfounding is not achieved by the spectral loss alone, but by the interaction between spectral shrinkage and regularization, especially in terms of early stopping. Moreover, we provide a mixed-model interpretation that connects LAVA-type shrinkage to random-effects adjustment and yields an empirical-Bayes procedure for tuning the spectral loss. We also extend the method to general likelihoods and nonlinear confounding using Laplace approximations and kernel random effects. Across synthetic and real-world experiments, spectrally deconfounded boosting improves estimation of the target function under hidden confounding and is substantially more scalable than existing nonlinear spectral deconfounding baselines.
