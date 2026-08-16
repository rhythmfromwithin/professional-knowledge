---
interest: medium
link: https://arxiv.org/abs/2608.11644
next_step: skim
priority: low
slack_ts: '1786844801.742919'
source: cs.DB - Databases
status: unread
title: Guided Table Retrieval for Structured Data Search
---
# Guided Table Retrieval for Structured Data Search
> 原文: [https://arxiv.org/abs/2608.11644](https://arxiv.org/abs/2608.11644)

arXiv:2608.11644v2 Announce Type: new
Abstract: Answering natural language questions over structured databases requires identifying the relevant tables and determining how to join them---a task that demands both schema knowledge and semantic understanding of the user's intent. We present guided table retrieval, a four-phase pipeline that combines deterministic grounding via hash-based predictors, structural exploration of join-graph reachability, LLM-powered disambiguation of sources and targets, and algorithmic merging into minimal, topologically ordered join trees. By decomposing the problem into phases with distinct responsibilities--- determinism, coverage, semantic reasoning, and coherence--- the pipeline avoids the brittleness of end-to-end LLM approaches while leveraging LLMs where their contextual judgment is most needed. We evaluate on BIRD-DEV and the enterprise-scale BEAVER benchmark, achieving 94% and 70% precision respectively, with 92% and 53% F1---substantially outperforming existing baselines on precision and F1 while producing exact join trees that can be directly consumed by downstream query compilers.
