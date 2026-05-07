---
interest: medium
link: https://arxiv.org/abs/2605.00905
next_step: skim
priority: high
slack_ts: '1778125801.060589'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'DIAGRAMS: A Review Framework for Reasoning-Level Attribution in Diagram QA'
---
# DIAGRAMS: A Review Framework for Reasoning-Level Attribution in Diagram QA
> 原文: [https://arxiv.org/abs/2605.00905](https://arxiv.org/abs/2605.00905)

arXiv:2605.00905v1 Announce Type: new
Abstract: Diagram question answering (Diagram QA) requires reasoning-level attribution that links each question-answer pair to all visual regions needed to derive the answer, rather than only the region containing the final response. Creating such structured evidence across diagrams, charts, maps, circuits, and infographics is time-consuming, and existing annotation tools tightly couple their interfaces to dataset-specific formats. We present DIAGRAMS, a lightweight, schema-driven review framework that decouples interface logic from dataset-specific JSON structures through an internal meta-schema and dataset adapters. Given an image and QA pair with optional candidate regions, the system performs QA-conditioned evidence selection and proposes the regions required for reasoning. When QA pairs or candidate regions are missing, it generates them and supports human verification and refinement. Across six Diagram QA datasets, model-suggested evidence achieves 85.39% precision and 75.30% recall against reviewer-final selections (micro-averaged). These results indicate that the review-first framework reduces manual region creation while maintaining high agreement with final reasoning-level attributions. We release a public demo and installable package to support dataset auditing, grounded supervision creation, and grounded evaluation.
