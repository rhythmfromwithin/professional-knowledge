---
interest: medium
link: https://arxiv.org/abs/2606.28383
next_step: skim
priority: medium
slack_ts: '1782792826.276889'
source: cs.CV - Computer Vision
status: unread
title: Zero-Label Driving Scenario Complexity Detection via Joint Embedding Predictive
  Architecture
---
# Zero-Label Driving Scenario Complexity Detection via Joint Embedding Predictive Architecture
> 原文: [https://arxiv.org/abs/2606.28383](https://arxiv.org/abs/2606.28383)

arXiv:2606.28383v1 Announce Type: new
Abstract: Identifying complex and safety-critical driving scenarios in large unlabelled datasets is an important but expensive problem. Existing approaches rely on human annotators, supervised classifiers, or carefully engineered rule sets, all of which require substantial prior knowledge about what constitutes a difficult scenario. We ask whether a model can discover scenario complexity on its own, with no labels at any stage. We train a minimal Joint Embedding Predictive Architecture (JEPA) on structured agent state data from the nuPlan mini dataset and use the temporal prediction error as a zero-shot complexity score. Without access to any ground-truth labels during training or evaluation setup, the model assigns significantly higher scores to scenarios involving unprotected turns, crosswalk interactions, and pedestrian proximity, and significantly lower scores to lane-following and stationary-traffic scenarios. We validate this finding through four ablation experiments that isolate the source of the signal, and through a downstream anomaly detection evaluation that achieves Average Precision of 0.512 against a 0.436 chance baseline. The results show that temporal prediction error in a self-supervised latent world model is a practical proxy for driving scenario complexity.
