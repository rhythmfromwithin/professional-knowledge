---
title: "Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.04067
priority: low
status: unread
interest: medium
next_step: skim
---
# Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation
> 原文: [https://arxiv.org/abs/2606.04067](https://arxiv.org/abs/2606.04067)

arXiv:2606.04067v1 Announce Type: new
Abstract: As LLMs become increasingly woven into everyday workflows, user queries sent to cloud hosted LLMs routinely mix task-essential content with task non-essential sensitive disclosures, yet type based PII redaction is context agnostic and may raise two issues: over disclosing untyped sensitive context and over removing answer bearing spans. We recast privacy preserving query rewriting under Contextual Integrity: a span should be forwarded only if it is necessary for the task. We introduce DelegateCI-Bench, the first task based Contextual Integrity benchmark for privacy-conscious delegation, comprising 3,167 samples that combine high quality synthetic data spanning 11 tasks and 20 task types, WildChat based real user queries, and a medical challenge set with dense sensitive information. Building on this benchmark, we propose a CI-guided reinforcement learning framework that converts essential and non-essential sensitive spans into verifiable optimization signals, and train a query rewriter to preserve task critical information while suppressing unnecessary sensitive disclosure. Experiments show that our learned rewriter achieves the best privacy-utility tradeoff, achieving up to +10.1 average utility over on-device baselines.
