---
title: "When Model Complexity Matters in Cross-Subject Naturalistic fMRI Prediction"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2611.04041
priority: low
status: unread
interest: medium
next_step: skim
---
# When Model Complexity Matters in Cross-Subject Naturalistic fMRI Prediction
> 原文: [https://arxiv.org/abs/2611.04041](https://arxiv.org/abs/2611.04041)

arXiv:2611.04041v1 Announce Type: new
Abstract: Increasingly complex neural models predict blood-oxygen-level-dependent (BOLD) responses to naturalistic stimuli, but the predictive value of this added complexity remains unclear. We ask when pretrained stimulus representations help and how much downstream complexity is needed, with and without recent measured BOLD history. We compare linear diagnostic references and nonlinear predictors across HCP movie fMRI (154 subjects), BOLD Moments (10 subjects), and Algonauts 2025 (4 subjects). Under a shared offline protocol, models are fitted on training subjects and evaluated on held-out subjects viewing largely familiar stimuli, without refitting. Pretrained visual features generally improve prediction over raw pixels; for linear autoregression, this advantage becomes more pronounced over longer rollouts (recursive predictions without additional measured BOLD). Measured BOLD history provides substantial gains that generally diminish {as rollouts lengthen}. Nonlinear stimulus-only predictors can improve on linear readouts, whereas linear autoregression provides a strong history-conditioned baseline. Controls examine context length, regularization, fitting procedures, and model capacity. Regional response consistency across subjects is associated with held-out prediction accuracy, while less consistent regions tend to gain more from measured history. In paired simulations with fixed linear neural dynamics, slower hemodynamic responses generally sustain high temporal prediction correlations over longer rollouts, illustrating how the observation process can contribute to predictive persistence. Together, these findings support evaluating stimulus representations and downstream complexity separately, using history-conditioned linear prediction as a diagnostic reference under matched inputs and measurement availability.
