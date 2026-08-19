---
title: "ARISE: An adaptive residual-informed stability ensemble for feature selection in small-sample biomedical omics"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.14866
priority: medium
status: unread
interest: medium
next_step: skim
---
# ARISE: An adaptive residual-informed stability ensemble for feature selection in small-sample biomedical omics
> 原文: [https://arxiv.org/abs/2608.14866](https://arxiv.org/abs/2608.14866)

arXiv:2608.14866v1 Announce Type: new
Abstract: Objective: Small-sample molecular classification requires feature selectors that identify predictive, stable, and nonredundant subsets for binary and multiclass outcomes. We propose ARISE (Adaptive Residual-Informed Stability Ensemble), which integrates complementary relevance signals, class-balanced stability assessment, residual-informed redundancy control, and multiclass pairwise coverage.
Methods: ARISE combines seven percentile-normalized relevance components through 15 predefined profiles, adaptively weighted by nested inner cross-validation. It was evaluated on five molecular datasets, eight feature-set sizes, three fixed classifiers (k-nearest neighbours, support vector machine, and random forest), and six filter comparators. Generalization was estimated by five-fold outer cross-validation repeated 50 times using balanced accuracy, macro-F1, and Cohen's kappa.
Results: Across 210,000 held-out assessments, ARISE ranked first in all 15 dataset-metric combinations. Equal-dataset means were 0.793 for balanced accuracy, 0.776 for macro-F1, and 0.725 for kappa, exceeding the strongest aggregate comparator by 0.022, 0.023, and 0.028, respectively. Performance remained strong across compact feature sets, although the optimal budget differed by dataset.
Conclusion: ARISE provides a transparent, adaptive framework that jointly addresses relevance, stability, redundancy, and multiclass discrimination. Its consistent results across datasets, classifiers, metrics, and feature-set sizes support further evaluation for small-sample molecular classification.
