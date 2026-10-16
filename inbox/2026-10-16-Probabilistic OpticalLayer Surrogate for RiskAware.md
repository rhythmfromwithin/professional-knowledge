---
title: "Probabilistic Optical-Layer Surrogate for Risk-Aware Control-Plane Decision Making"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.21069
priority: medium
status: unread
interest: medium
next_step: skim
---
# Probabilistic Optical-Layer Surrogate for Risk-Aware Control-Plane Decision Making
> 原文: [https://arxiv.org/abs/2610.21069](https://arxiv.org/abs/2610.21069)

arXiv:2610.21069v1 Announce Type: new
Abstract: In this paper, we propose a generative surrogate for the optical layer. Current control-plane decisions in optical transport networks are made using analytical impairment models, deterministic learned predictors, or quantile-regression-based uncertainty estimates. These approaches expose only a limited, static summary of the optical layer at any given time. This forces the control plane to rely on conservative fixed margins that leave capacity underutilized. Our proposed surrogate is a conditional generative model trained on traces from optical simulators with validated physical models. The surrogate produces a full conditional distribution over physical-layer metrics such as OSNR, Q-margin, nonlinear penalty, and feasibility. This output allows the controller to estimate violation probability and tail risk at arbitrary thresholds at runtime. This is different from existing approaches because no retraining is required for each decision. We present the first case study in fast path feasibility estimation using a generative surrogate for the optical layer. We compare the surrogate against simulators, deterministic learned predictors, and quantile-regression estimators. We evaluate the surrogate along nine research questions (RQ1--RQ9) covering prediction accuracy, inference latency, uncertainty quality, controller integration, cross-emulator generalization, dynamic reconfiguration under span degradation, topology scalability, GNPy-validated generalization, and finally, inference latency on real-world live hardware traces. The core contribution is an optical-layer control abstraction where physical-layer behavior is exposed as a fast probabilistic query mechanism instead of an offline simulation output or a deterministic feasibility rule.
