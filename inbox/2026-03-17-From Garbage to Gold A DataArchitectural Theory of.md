---
title: "From Garbage to Gold: A Data-Architectural Theory of Predictive Robustness"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.12288
priority: high
status: unread
interest: medium
next_step: skim
---
# From Garbage to Gold: A Data-Architectural Theory of Predictive Robustness
> 原文: [https://arxiv.org/abs/2603.12288](https://arxiv.org/abs/2603.12288)

arXiv:2603.12288v1 Announce Type: new
Abstract: Tabular machine learning presents a paradox: modern models achieve state-of-the-art performance using high-dimensional (high-D), collinear, error-prone data, defying the "Garbage In, Garbage Out" mantra. To help resolve this, we synthesize principles from Information Theory, Latent Factor Models, and Psychometrics, clarifying that predictive robustness arises not solely from data cleanliness, but from the synergy between data architecture and model capacity. Partitioning predictor-space "noise" into "Predictor Error" and "Structural Uncertainty" (informational deficits from stochastic generative mappings), we prove that leveraging high-D sets of error-prone predictors asymptotically overcomes both types of noise, whereas cleaning a low-D set is fundamentally bounded by Structural Uncertainty. We demonstrate why "Informative Collinearity" (dependencies from shared latent causes) enhances reliability and convergence efficiency, and explain why increased dimensionality reduces the latent inference burden, enabling feasibility with finite samples. To address practical constraints, we propose "Proactive Data-Centric AI" to identify predictors that enable robustness efficiently. We also derive boundaries for Systematic Error Regimes and show why models that absorb "rogue" dependencies can mitigate assumption violations. Linking latent architecture to Benign Overfitting, we offer a first step towards a unified view of robustness to Outcome Error and predictor-space noise, while also delineating when traditional DCAI's focus on label cleaning remains powerful. By redefining data quality from item-level perfection to portfolio-level architecture, we provide a theoretical rationale for "Local Factories" -- learning from live, uncurated enterprise "data swamps" -- supporting a deployment paradigm shift from "Model Transfer" to "Methodology Transfer'' to overcome static generalizability limitations.
