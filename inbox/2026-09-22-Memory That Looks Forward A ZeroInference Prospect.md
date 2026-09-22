---
title: "Memory That Looks Forward: A Zero-Inference Prospective Term for Personal Memory Retrieval"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2609.22091
priority: high
status: unread
interest: medium
next_step: skim
---
# Memory That Looks Forward: A Zero-Inference Prospective Term for Personal Memory Retrieval
> 原文: [https://arxiv.org/abs/2609.22091](https://arxiv.org/abs/2609.22091)

arXiv:2609.22091v1 Announce Type: new
Abstract: Retrieval over a personal memory store is retrospective: it surfaces what resembles the query, and it is blind to what the user has committed to do. We describe a prospective term for memory retrieval that costs no inference at query time. Commitments are held in an explicit ledger as dated or trigger-conditioned entries; memory items linked to a firing entry receive a salience boost, blended multiplicatively into embedding-based retrieval so that relevance remains sovereign. On a synthetic prospective-memory task set modeled on TriggerBench's published structure (48 blind-authored dialogues, 175 tasks), the term raised recall@5 on the hard stratum from 0.000 to 0.955 at the default blend weight and to 1.000 under a floor variant, with zero false boosts across 53 resolved-commitment tasks. Blind authorship also produced a scope finding: only 17-29% of naturally phrased commitment-trigger pairs defeat embedding similarity, so the term matters on a real minority of cases and must do no harm on the rest, which it does not. We position precomputed commitment linkage as the always-on floor of a layered design whose expansion layer is query-time prospection. Results are preliminary: the evaluation set is author-constructed, and evaluation on TriggerBench proper is committed follow-up work once its data is released.
