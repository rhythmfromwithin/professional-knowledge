---
title: "Diffusion-based Denoising Beats Vanilla Score Matching in Parameter Estimation: A Theoretical Explanation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.22950
priority: medium
status: unread
interest: medium
next_step: skim
---
# Diffusion-based Denoising Beats Vanilla Score Matching in Parameter Estimation: A Theoretical Explanation
> 原文: [https://arxiv.org/abs/2605.22950](https://arxiv.org/abs/2605.22950)

arXiv:2605.22950v1 Announce Type: new
Abstract: Score matching is an alternative to maximum likelihood estimation when the normalizing constant is unknown or too costly to evaluate. However, vanilla score matching has shown to be inefficient relative to maximum likelihood estimation for multimodal distributions with well-separated modes, which are commonly encountered in practical applications. We compare a novel diffusion-based denoising score matching estimator (DDSME) to the vanilla score matching estimator (SME) in this scenario. In particular, we prove statistical guarantees for both estimators, showing that the error bound for the vanilla SME worsens when the separation between the modes increases, which can be avoided in case of the DDSME with suitable hyperparameter tuning. This provides a novel theoretical explanation for the superior behavior of diffusion-based score matching over the vanilla version.
