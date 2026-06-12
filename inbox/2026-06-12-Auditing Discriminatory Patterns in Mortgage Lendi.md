---
interest: medium
link: https://arxiv.org/abs/2606.12435
next_step: skim
priority: low
slack_ts: '1781239679.530099'
source: cs.DB - Databases
status: unread
title: Auditing Discriminatory Patterns in Mortgage Lending Through Association Rules
  and Fair Binning
---
# Auditing Discriminatory Patterns in Mortgage Lending Through Association Rules and Fair Binning
> 原文: [https://arxiv.org/abs/2606.12435](https://arxiv.org/abs/2606.12435)

arXiv:2606.12435v1 Announce Type: cross
Abstract: Mortgage lending in the United States exhibits persistent racial and gender disparities. We investigate whether standard data preprocessing steps, specifically attribute binning, amplify these disparities in downstream pattern mining. Using 103,481 cleaned mortgage applications from the HMDA 2023 dataset (Chicago metropolitan area), we build a three-stage pipeline: (1) a PySpark data cleaning and binning pipeline that implements both standard equal-frequency binning and the epsilon-biased fair binning algorithm from Asudeh et al. [1], (2) FP-Growth association rule mining that compares denial patterns under both binning regimes, and (3) K-Means clustering with a per-cluster disparate impact audit. Our standard binning shows 9.63% racial bias in income discretization, consistent with the 8-10% reported in prior work. Fair binning with seven race groups is infeasible at epsilon=0.03 and only succeeds at epsilon=0.08 with a Price of Fairness of 29.4%. FP-Growth reveals that high debt-to-income ratio is the dominant denial predictor (67.2% confidence, 2.81 lift), while racial bias does not appear as explicit high-support rules. However, K-Means clustering followed by a disparate impact audit flags 10 out of 45 cluster-group pairs, showing that Black applicants face significantly higher denial rates than White applicants even among financially similar groups.
