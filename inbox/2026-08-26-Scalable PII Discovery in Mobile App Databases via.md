---
interest: medium
link: https://arxiv.org/abs/2608.21469
next_step: skim
priority: low
slack_ts: '1787820610.543479'
source: cs.CR - Cryptography and Security
status: unread
title: Scalable PII Discovery in Mobile App Databases via Hypothesis-Driven Search
---
# Scalable PII Discovery in Mobile App Databases via Hypothesis-Driven Search
> 原文: [https://arxiv.org/abs/2608.21469](https://arxiv.org/abs/2608.21469)

arXiv:2608.21469v1 Announce Type: new
Abstract: Discovering personally identifiable information (PII) in mobile forensic databases is difficult because the relevant table-column regions are unknown, distributed across heterogeneous SQLite schemas, and may contain values embedded in free-text or semi-structured fields. We present a hypothesis-driven framework that treats PII localization as bounded, adaptive search under uncertainty. An agent ranks candidate table-column regions, probes sampled values, and maintains a memory of prior evidence, confidence scores, and decisions to refine subsequent hypotheses. The framework separates lightweight PII exploration from targeted extraction, normalization, and deduplication over validated regions, thereby limiting exhaustive inspection to regions supported by sampled evidence. We evaluate the framework on 25 SQLite databases from 10 Android and iOS applications in the Cellebrite CTF corpus, targeting email addresses, phone numbers, domain names, person names, and postal addresses. Against a corpus-level distinct ground-truth set of 3,751 entities, Gemini 2.5 Pro achieves 94.5% F1 while reducing the effective extraction search space by 79.9% on average. Results across 12 model backends show strong performance among several frontier models, but substantial sensitivity to model capability.
