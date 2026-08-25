---
title: "The Exceedance Design Effect: Effective Sample Size for Thresholds under Clustering"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.21262
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Exceedance Design Effect: Effective Sample Size for Thresholds under Clustering
> 原文: [https://arxiv.org/abs/2608.21262](https://arxiv.org/abs/2608.21262)

arXiv:2608.21262v1 Announce Type: new
Abstract: Many machine-learning systems set a threshold at a quantile of a calibration set: conformal predictors that promise 90% coverage by drawing their cutoff at the calibration set's 90th percentile, abstention gates that decline to answer when a model's score falls below the calibration set's tenth percentile, safety filters that block any output scoring above the 99th percentile of a reference set. All of them promise that the threshold will hold at the stated rate on new data. The promise assumes the calibration examples are independent, and in modern pipelines they usually are not: they share a prompt, a document, a reasoning trace. Survey statistics has known how to discount correlated data since 1965, by counting how many independent observations a sample is worth, but only for averages. We show that a threshold needs a different count. The count depends on how often clustered scores land on the same side of the threshold, and that changes with where the threshold is set. How similar the scores are as numbers does not enter. We prove a closed-form law for the resulting effective sample size and for the spread of the coverage a deployed system actually sees.
Three consequences follow. The correction now used in the conformal literature is the wrong quantity, and can miss in either direction. A dataset has no single effective sample size. It has one for each level the threshold is set at. And the damage is invisible in coverage averaged over many runs, and fully felt by whoever deploys once. On a released calibration set of 25,028 examples, we measure the reliability of about 1,300.
