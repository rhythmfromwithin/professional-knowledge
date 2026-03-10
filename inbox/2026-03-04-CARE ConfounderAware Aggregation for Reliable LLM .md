---
title: "CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.00039
priority: high
status: unread
interest: medium
next_step: skim
---
# CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation
> 原文: [https://arxiv.org/abs/2603.00039](https://arxiv.org/abs/2603.00039)

arXiv:2603.00039v1 Announce Type: new
Abstract: LLM-as-a-judge ensembles are the standard paradigm for scalable evaluation, but their aggregation mechanisms suffer from a fundamental flaw: they implicitly assume that judges provide independent estimates of true quality. However, in practice, LLM judges exhibit correlated errors caused by shared latent confounders -- such as verbosity, stylistic preferences, or training artifacts -- causing standard aggregation rules like majority vote or averaging to provide little gain or even amplify systematic mistakes. To address this, we introduce CARE, a confounder-aware aggregation framework that explicitly models LLM judge scores as arising from both a latent true-quality signal and shared confounding factors. Rather than heuristically re-weighting judges, CARE separates quality from confounders without access to ground-truth labels. We provide theoretical guarantees for identifiability and finite-sample recovery under shared confounders, and we quantify the systematic bias incurred when aggregation models omit confounding latent factors. Across 12 public benchmarks spanning continuous scoring, binary classification, and pairwise preference settings, CARE improves aggregation accuracy, reducing error by up to 26.8\%. Code is released in \href{https://github.com/SprocketLab/CARE}{https://github.com/SprocketLab/CARE}.
