---
interest: medium
link: https://arxiv.org/abs/2610.06854
next_step: skim
priority: low
slack_ts: '1791351195.034359'
source: cs.DB - Databases
status: unread
title: 'Beyond Marginals: A Multi-Dimensional Evaluation Framework for Multi-Table
  Synthetic Data Generation'
---
# Beyond Marginals: A Multi-Dimensional Evaluation Framework for Multi-Table Synthetic Data Generation
> 原文: [https://arxiv.org/abs/2610.06854](https://arxiv.org/abs/2610.06854)

arXiv:2610.06854v1 Announce Type: new
Abstract: Synthetic data generation is critical for privacy compliance, machine learning augmentation, and software testing. While single-table evaluation is well established, multi-table (relational) synthesis, the dominant enterprise use case, lacks a unified evaluation framework. Existing approaches assess marginal column distributions in isolation, overlooking joint distributions, cross-table structural integrity, downstream utility, and production-readiness edge cases. We present SynEval, a six-dimensional evaluation framework for multi-table synthetic databases. SynEval jointly assesses per-column fidelity, multivariate structure preservation including a novel conditional distribution check, cross-table integrity, ML utility, privacy protection, and edge-case robustness. The framework produces a unified weighted quality score with per-table and per-dimension drill-down, and is generator-agnostic, operating on any pair of real and synthetic CSV folders with automatic schema inference. SynEval is a framework to combine conditional distribution checks P(Y|X), cross-table cardinality validation, and production-readiness edge-case testing within a single evaluation pipeline for relational synthetic data.
