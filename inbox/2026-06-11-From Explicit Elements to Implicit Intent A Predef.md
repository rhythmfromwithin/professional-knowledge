---
interest: medium
link: https://arxiv.org/abs/2606.11207
next_step: skim
priority: high
slack_ts: '1781153115.400599'
source: cs.AI - Artificial Intelligence
status: unread
title: 'From Explicit Elements to Implicit Intent: A Predefined Library for Auditable
  Behavioral Inference'
---
# From Explicit Elements to Implicit Intent: A Predefined Library for Auditable Behavioral Inference
> 原文: [https://arxiv.org/abs/2606.11207](https://arxiv.org/abs/2606.11207)

arXiv:2606.11207v1 Announce Type: new
Abstract: We present SemantiClean, a modular framework for extracting structured semantic signals from e-commerce session data and driving pluggable inference targets including purchase intent, customer segmentation, and product affinity through a shared element library. Unlike conventional end-to-end predictors that optimise solely for accuracy, SemantiClean prioritises auditability, structural governance, and sigma=0 reproducibility, explicitly trading marginal predictive gains for element-level transparency and defensible decision trails. Built upon the Online Shoppers Purchasing Intention (OSPI) dataset, the framework organises twenty-four behavioural elements into a four-layer architecture (Functional, Interaction, Systemic, Contextual) and enforces signal quality through three anti-inflation mechanisms: RedundancyGroup contribution caps, TieredPenaltyCalculator bias penalties, and AdaptiveConstraintMode cold-start protection.This report introduces the LLM-Integrated Semantic Inference Engine, a fully implemented two-phase LLM-driven inference architecture that leverages complete element metadata at inference time. All quantitative results reported herein are produced by this engine. Deterministic engine outputs remain fully reproducible (sigma=0); LLM-dependent results (E8, E10) are subject to controlled output variability under fixed provider/model/temperature settings. The gender inference target remains non-functional in the current implementation and is excluded from all quantitative results.
