---
interest: medium
link: https://arxiv.org/abs/2607.13037
next_step: skim
priority: high
slack_ts: '1784344418.409249'
source: cs.AI - Artificial Intelligence
status: unread
title: 'OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets'
---
# OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets
> 原文: [https://arxiv.org/abs/2607.13037](https://arxiv.org/abs/2607.13037)

arXiv:2607.13037v1 Announce Type: new
Abstract: When a data contributor requests removal, model trainers face a practical gap: unlearning algorithms require a forget set, yet no tool can locate which training records belong to a given author. Existing provenance systems operate at file or dataset level, forcing catastrophic over-deletion. We present ob, a record- and token-level data provenance system that propagates author identity through data processing pipelines and resolves revocation requests into precise forget sets via deterministic queries. Evaluation on 219,555 Wikipedia pages demonstrates that record-level provenance eliminates dataset-level over-deletion (from 101x to 1.3x), while integration adds 1.3-4.0% throughput overhead (HuggingFace) and 2.1-19.0% (Datatrove) on wiki data. On a 1.7B model, provenance-based forget sets improve unlearning by 42% over random baselines.
