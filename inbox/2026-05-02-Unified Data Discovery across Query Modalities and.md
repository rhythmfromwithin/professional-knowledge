---
title: "Unified Data Discovery across Query Modalities and User Intents"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.27252
priority: low
status: unread
interest: medium
next_step: skim
---
# Unified Data Discovery across Query Modalities and User Intents
> 原文: [https://arxiv.org/abs/2604.27252](https://arxiv.org/abs/2604.27252)

arXiv:2604.27252v1 Announce Type: new
Abstract: Data discovery - retrieving relevant tables from a data lake in response to user queries - is a fundamental building block for downstream analytics. In practice, data discovery must support different query modalities, including natural language (NL) statements and tables, and accommodate diverse user intents, ranging from open-ended enrichment to task-driven inference for applications such as table question answering and fact verification. However, most existing methods are designed for a single query modality or a specific user intent, limiting their generalizability. We propose UniDisc, a unified data discovery framework that supports both NL statements and tables as queries and generalizes across diverse user intents without intent-specific representations or relevance modeling. UniDisc learns a common cross-modal representation model that produces unified representations for queries of different modalities and candidate tables, enabling uniform relevance assessment across discovery scenarios. Since learning such a model typically requires large labeled collections of query-table pairs, which are expensive to obtain, UniDisc instead exploits contextual signals naturally available in data lakes. Specifically, it models NL statements and tables as nodes in a heterogeneous graph with multiple edge types, and applies dual-view neighbor aggregation and joint optimization to learn robust, context-aware representations under limited supervision. These representations support flexible relevance estimation during retrieval. Experiments on seven datasets show that UniDisc consistently outperforms strong baselines on both NL- and table-based discovery.
