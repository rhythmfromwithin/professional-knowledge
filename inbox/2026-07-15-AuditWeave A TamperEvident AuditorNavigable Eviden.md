---
interest: medium
link: https://arxiv.org/abs/2607.09682
next_step: skim
priority: high
slack_ts: '1784172042.880109'
source: cs.LG - Machine Learning
status: unread
title: 'AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted
  and Data-Transformation Workflows'
---
# AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted and Data-Transformation Workflows
> 原文: [https://arxiv.org/abs/2607.09682](https://arxiv.org/abs/2607.09682)

arXiv:2607.09682v1 Announce Type: new
Abstract: AI systems are increasingly used to assist consequential decisions in regulated domains such as auditing, finance, and healthcare. This creates a recurring obligation: an organization must be able to reconstruct, after the fact, which evidence informed a given conclusion, and to show that the record of that reasoning was not altered. Existing tools address related but distinct problems - model observability, drift monitoring, governance reporting - and are built for the machine-learning engineer operating a system, not the reviewer who must trace one specific conclusion back to its supporting evidence. We present AuditWeave, a lightweight Python library, with no runtime dependencies, that records the steps of AI-assisted and data-transformation workflows into a single append-only, hash-chained ledger. A small, system-agnostic event vocabulary spans both retrieval-augmented generation (RAG) pipelines and tabular/lakehouse transformations, so a conclusion that draws on both can be traced end-to-end through one record. Within a sealed ledger, any modification, reordering, insertion, or deletion of events is detectable through chain verification. We describe the design and evaluate recording overhead, scalability, and tamper-detection correctness on the reference implementation. The integrity guarantees cost tens of microseconds per event, and, as the hash-chain construction implies, verification flagged every injected mutation across four mutation classes over 2,000 randomized trials.
