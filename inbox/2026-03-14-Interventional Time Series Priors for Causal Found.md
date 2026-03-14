---
title: "Interventional Time Series Priors for Causal Foundation Models"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.11090
priority: high
status: unread
interest: medium
next_step: skim
---
# Interventional Time Series Priors for Causal Foundation Models
> 原文: [https://arxiv.org/abs/2603.11090](https://arxiv.org/abs/2603.11090)

arXiv:2603.11090v1 Announce Type: new
Abstract: Prior-data fitted networks (PFNs) have emerged as powerful foundation models for tabular causal inference, yet their extension to time series remains limited by the absence of synthetic data generators that provide interventional targets. Existing time series benchmarks generate observational data with ground-truth causal graphs but lack the interventional data required for training causal foundation models. To address this, we propose \textbf{CausalTimePrior}, a principled framework for generating synthetic temporal structural causal models (TSCMs) with paired observational and interventional time series. Our prior supports configurable causal graph structures, nonlinear autoregressive mechanisms, regime-switching dynamics, and multiple intervention types (hard, soft, time-varying). We demonstrate that PFNs trained on CausalTimePrior can perform in-context causal effect estimation on held-out TSCMs, establishing a pathway toward foundation models for time series causal inference.
