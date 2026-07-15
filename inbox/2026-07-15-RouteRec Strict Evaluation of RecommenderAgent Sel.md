---
title: "RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.09908
priority: high
status: unread
interest: medium
next_step: skim
---
# RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation
> 原文: [https://arxiv.org/abs/2607.09908](https://arxiv.org/abs/2607.09908)

arXiv:2607.09908v1 Announce Type: new
Abstract: Recommender systems increasingly face a choice among heterogeneous agents -- collaborative filters, sequential models, content-based retrievers, and LLM-based rerankers -- yet no single agent is uniformly best. We study this choice as task-aware agent ranking under cost constraints using RouteRec, a framework that compares request-level hard selection with item-level learned aggregation over four traditional recommender agents and one LLM reranker agent. On MovieLens-1M, the full quality oracle has substantial headroom (HR@10 = 0.584), confirming that useful cross-agent signal exists. Under a leakage-free 5-fold out-of-fold protocol, however, hard selection remains below BM25 (0.223 vs. 0.254), and selective LLM escalation does not improve it. The same protocol yields a different outcome for learned aggregation: its cheap-only variant matches BM25 in HR and has a higher NDCG point estimate (0.123 vs. 0.114), while gated all-agent aggregation reaches HR@10 = 0.295 with 70.2\% LLM calls. The resulting lesson is not that routing is solved, but that request-level selection of one complete agent list is too coarse for this sparse fixed-candidate setting; item-level aggregation is the more promising action space.
