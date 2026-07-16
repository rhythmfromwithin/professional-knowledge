---
interest: medium
link: https://arxiv.org/abs/2607.10410
next_step: skim
priority: medium
slack_ts: '1784172054.564759'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'TSCoNet: A Two-Stage Copula CNN-LSTM for Uncertainty-Aware Spatio-Temporal
  Forecasting'
---
# TSCoNet: A Two-Stage Copula CNN-LSTM for Uncertainty-Aware Spatio-Temporal Forecasting
> 原文: [https://arxiv.org/abs/2607.10410](https://arxiv.org/abs/2607.10410)

arXiv:2607.10410v1 Announce Type: new
Abstract: Reliable forecasting of several interrelated environmental variables - such as regional precipitation and temperature, or other correlated geophysical fields - across many locations calls for accurate predictions accompanied by trustworthy statements of their uncertainty. Modern deep-learning models forecast such variables accurately but usually report no uncertainty, and forcing them to output uncertainty through maximum likelihood tends to degrade their accuracy, especially when the variables are strongly correlated. Motivated by this tension, we develop TSCoNet, a two-stage convolutional-recurrent model coupled with a Gaussian copula that jointly forecasts multiple variables over space and time while quantifying predictive uncertainty. The method first learns accurate mean forecasts and then, holding the mean fixed, refines a shared representation to estimate the predictive variance, yielding calibrated prediction intervals after a standard recalibration, so that uncertainty is added without sacrificing point accuracy. We study the approach on simulated non-stationary spatial fields on the sphere and on a real dataset of monthly precipitation and temperature for fifty cities over 2000-2020. The model matches the accuracy of a strong deterministic forecaster while supplying calibrated prediction intervals that the deterministic model cannot, giving a single tool that provides both accurate point forecasts and reliable uncertainty for multivariate spatio-temporal data.
