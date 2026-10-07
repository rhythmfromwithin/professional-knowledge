---
interest: medium
link: https://arxiv.org/abs/2610.02248
next_step: skim
priority: high
slack_ts: '1791351180.538159'
source: cs.LG - Machine Learning
status: unread
title: State-Space Unlearning for Non-Stationary Bias in Land Surface Forecasting
---
# State-Space Unlearning for Non-Stationary Bias in Land Surface Forecasting
> 原文: [https://arxiv.org/abs/2610.02248](https://arxiv.org/abs/2610.02248)

arXiv:2610.02248v1 Announce Type: new
Abstract: Operational land surface forecasting systems built on Mamba-family Structured State Space Models absorb non-stationary confounding events (unrecorded irrigation booms, dam-operation shifts, sensor recalibrations) into their state-transition matrices, silently biasing NDVI, LST, and crop phenology predictions long after the physical cause ends. This paper introduces SSU-LSF (State-Space Unlearning for Land Surface Forecasting), the first machine-unlearning framework purpose-built for geoscientific Mamba-based SSMs. We develop EKFac influence functions specialized to the Mamba state matrices via a closed-form matrix-exponential gradient, use spectral-radius-weighted elbow thresholding to localize a temporal confounding footprint $\Phi$, and apply Hessian-free projected gradient ascent within a KL-divergence trust region augmented by spatial total-variation (TV) regularization. Proposition 1 establishes that residual confounding is bounded by $\mathcal{O}\big((1-\rho(\bar{A})^{T\_c})/((1-\rho(\bar{A}))\mu)\big)$, which grows with the window length $T\_c$. Across three heterogeneous benchmarks and eleven baselines, SSU-LSF achieves confounding reduction rates of $0.773$ (CropHarvest), $0.821$ (NDVI-LST), and $0.859$ (ERA5), with worst-case clean-domain RMSE degradation of $4.2\%$ on ERA5, converging in 3--5 epochs at $8.4\times$ lower GPU-cost per unlearning request than full retraining. Code: https://github.com/Anidipta/SSU-LSF
