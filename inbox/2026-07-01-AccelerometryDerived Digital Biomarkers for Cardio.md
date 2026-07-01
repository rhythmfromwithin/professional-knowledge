---
interest: medium
link: https://arxiv.org/abs/2606.30702
next_step: skim
priority: high
slack_ts: '1782880926.040599'
source: cs.LG - Machine Learning
status: unread
title: 'Accelerometry-Derived Digital Biomarkers for Cardiometabolic Risk: A Population-Representative
  Tabular Benchmark with Uncertainty Quantification'
---
# Accelerometry-Derived Digital Biomarkers for Cardiometabolic Risk: A Population-Representative Tabular Benchmark with Uncertainty Quantification
> 原文: [https://arxiv.org/abs/2606.30702](https://arxiv.org/abs/2606.30702)

arXiv:2606.30702v1 Announce Type: new
Abstract: Structured tabular data dominates clinical medicine, yet existing benchmarks fail to reflect real-world properties like complex survey sampling, demographic oversampling, and subgroup fairness. We introduce the NHANES Accelerometry Cardiometabolic Benchmark, derived from NHANES 2003-2006, comprising 1,381 adults with hip-worn accelerometry, fasting laboratory biomarkers, dietary intake, and anthropometrics. We evaluate three tabular learning methods -- ridge regression, XGBoost, and the foundation model TabPFN v2 -- to predict glycated haemoglobin (HbA1c), fasting triglycerides, and C-reactive protein (CRP) from activity phenotypes and lifestyle covariates. TabPFN v2 achieves the best overall performance (HbA1c R^2=0.156, CRP R^2=0.383), while triglycerides remain largely unpredictable (R^2 < 0.05), consistent with known genetic dominance. We apply split conformal prediction to generate distribution-free 90% prediction intervals and evaluate demographic coverage equity across sex and race/ethnicity subgroups. Marginal coverage aligns with the 90% target for CRP and HbA1c but falls below for triglycerides. At the subgroup level, we observe localized undercoverage (e.g., HbA1c for Mexican American participants), illustrating the gap between marginal guarantees and the conditional coverage required for clinical fairness. Code and data are at https://github.com/felizzi/nhanes-accel-cardiometabolic-benchmark.
