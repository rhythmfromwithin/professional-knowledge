---
title: "SHIFT: Robust Double Machine Learning for Average Dose-Response Functions under Heavy-Tailed Contamination"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.00176
priority: medium
status: unread
interest: medium
next_step: skim
---
# SHIFT: Robust Double Machine Learning for Average Dose-Response Functions under Heavy-Tailed Contamination
> 原文: [https://arxiv.org/abs/2605.00176](https://arxiv.org/abs/2605.00176)

arXiv:2605.00176v1 Announce Type: new
Abstract: Double-machine-learning pipelines for the Average Dose-Response Function rely on kernel-weighted local-linear smoothers, which inherit unbounded functional influence: a single outlier within a kernel window biases the curve across the entire window. We introduce SHIFT (Self-calibrated Heavy-tail Inlier-Fit with Tempering), a robust DML estimator combining cross-fit nuisance orthogonalization with a kernel-local Welsch-loss second stage optimized by Graduated Non-Convexity, and -- the principal design choice -- a defensive OLS refit whose inlier cutoff is scaled by post-GNC residual MAD rather than the raw-outcome MAD. On a localized-contamination stress test at $p=0.25$ this design choice drops level-RMSE from 1.03 to 0.33 while leaving clean and uniformly-contaminated runs unchanged. Across 1,400 main-sweep fits, SHIFT has competitive worst-case shape recovery (RMSE $0.325$ at $p=0.25$, second to Huber-DML's $0.276$); among the three methods with worst-case RMSE below $0.35$, only SHIFT emits a non-uniform per-sample weight vector, recovering the ground-truth outlier mask at mean $F\_1 \approx 0.96$ (range $0.945$--$0.968$) on Gaussian-jump DGPs. We pair the estimator with a six-technique Extreme Value Theory diagnostic suite (Hill, GPD-MLE/PWM, GEV, Mean Excess, parameter stability, causal tail coefficient) that lets a practitioner distinguish Frechet from Weibull regimes and choose between SHIFT and L1 alternatives on empirical grounds. Extensions to binary-treatment CATE (Huber pseudo-outcome X-Learner) and time-series ADRF (block-CV + rolling MAD) are included. A counter-intuitive ablation: linear nuisance models (Ridge, Lasso) outperform gradient-boosted nuisances for robust DML under uniform contamination, inverting the usual more-flexible-is-better heuristic.
