---
interest: medium
link: https://arxiv.org/abs/2607.00113
next_step: skim
priority: high
slack_ts: '1782965368.360629'
source: cs.LG - Machine Learning
status: unread
title: 'SemiScope: Disentangling Classifier Tuning and Joint Optimization in Semi-Supervised
  Security Classification'
---
# SemiScope: Disentangling Classifier Tuning and Joint Optimization in Semi-Supervised Security Classification
> 原文: [https://arxiv.org/abs/2607.00113](https://arxiv.org/abs/2607.00113)

arXiv:2607.00113v1 Announce Type: new
Abstract: Background. Labeled data for security classification is scarce. Semi-supervised learning (SSL) propagates labels from a small labeled pool to larger unlabeled pools. Yet security applications often use SSL as a black box: default parameters, a fixed classifier, and no handling of pseudo-label-induced class imbalance. Aims. Recent work reports sizeable gains from optimizing SSL pipelines via joint search, AutoML, or per-component tuning. These gains are hard to attribute: they may reflect useful SSL-classifier interactions, or mostly from simply tuning the downstream classifier. We disentangle these effects for binary tabular security data with classical SSL and tree-based classifiers. Method. We build SemiScope as an analysis instrument, not a deployment recommendation. It uses Bayesian Optimization to jointly tune SSL settings, confidence filtering, oversampling, and the classifier. The key control, Tuned-Clf, fixes SSL to defaults but gets the same 100-trial classifier budget and validation-set threshold tuning as SemiScope. At 10% labels, we compare them with paired TOST using a +/-1.0 g-measure smallest effect of interest. Results. SemiScope beats every default SSL baseline on all five datasets, improving over the strongest by 0.7-12.7 points. Under the equal-budget control, Tuned-Clf is statistically equivalent to the full pipeline on 4 of 5 datasets; Phishing is inconclusive. Classifier HPO alone recovers a median 86% of SemiScope's gain over Default Self-Training (ST) + Random Forest (RF). Conclusions. The reusable contribution is the decomposition protocol. A simpler recipe suffices: use Self-Training, tune the classifier with Bayesian Optimization, and tune the decision threshold on validation data. It reaches within 1 g-measure of Supervised RF at 20-30% labels on four datasets and 40% on Drebin, at the same or lower label rate than Default ST + RF on every dataset.
