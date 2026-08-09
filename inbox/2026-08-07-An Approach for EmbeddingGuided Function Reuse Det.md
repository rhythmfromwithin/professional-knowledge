---
interest: medium
link: https://arxiv.org/abs/2608.04137
next_step: skim
priority: low
slack_ts: '1786241595.725579'
source: cs.SE - Software Engineering
status: unread
title: An Approach for Embedding-Guided Function Reuse Detection in Embedded C Software
---
# An Approach for Embedding-Guided Function Reuse Detection in Embedded C Software
> 原文: [https://arxiv.org/abs/2608.04137](https://arxiv.org/abs/2608.04137)

arXiv:2608.04137v1 Announce Type: new
Abstract: Reusing embedded software functions across products is economically valuable but technically difficult: the same functionality implemented for two different microcontroller platforms can be entirely incompatible at the hardware level, even when the functions score above 0.90 cosine similarity and both pass SonarQube quality checks. Static analysis tools were designed to measure code quality, not hardware-domain compatibility, and have no model of peripheral interfaces, hardware abstraction layer (HAL) dependencies, or register-map constraints. This paper presents a domain-aware retrieval-augmented generation (RAG) pipeline for embedded C software reuse detection that addresses the hardware-compatibility gap directly. The pipeline enriches each function by extracting its existing inline comments, call-graph context, and a project README before embedding it with eight backbone models (MiniLM, MPNet, BGE, E5, GraphCodeBERT, OpenAI text-embedding-3-small, LLaMA 3 8B, StarCoder2 3B) acting as feature extractors. Four hardware-compatibility validators---covering peripheral token overlap, parameter count parity, call-graph dependency overlap, and structural branching pattern---filter candidates directly in the retrieval stack. Evaluated on six public embedded C software projects (184 functions, 4,815 above-plateau pairs), the pipeline reveals that SonarQube produces a 93.6% false-positive rate as a reuse filter, with 83.5% of failures caused by hardware-environment mismatches that static analysis cannot detect. Manual verification of 40 rejected pairs confirms 97.5% validator accuracy, and a diagnostic rule-injection variant identifies the dominant failure categories (McNemar chi-squared~=~294.0, p~$<$~0.001).
