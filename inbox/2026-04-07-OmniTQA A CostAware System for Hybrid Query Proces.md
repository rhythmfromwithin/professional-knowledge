---
interest: medium
link: https://arxiv.org/abs/2604.02444
next_step: skim
priority: low
slack_ts: '1775531933.184169'
source: cs.DB - Databases
status: unread
title: 'OmniTQA: A Cost-Aware System for Hybrid Query Processing over Semi-Structured
  Data'
---
# OmniTQA: A Cost-Aware System for Hybrid Query Processing over Semi-Structured Data
> 原文: [https://arxiv.org/abs/2604.02444](https://arxiv.org/abs/2604.02444)

arXiv:2604.02444v1 Announce Type: new
Abstract: While recent advances in large language models have significantly improved Text-to-SQL and table question answering systems, most existing approaches assume that all query-relevant information is explicitly represented in structured schemas. In practice, many enterprise databases contain hybrid schemas where structured attributes coexist with free-form textual fields, requiring systems to reason over both types of information. To address this challenge, we introduce OmniTQA, a cost-aware hybrid query processing framework that operates over both structured and semi-structured data. OmniTQA treats semantic reasoning as a first-class query operator, seamlessly integrating LLM-based semantic operations with classical relational operators into an executable directed acyclic graph. To manage the high latency and cost of LLM inference, it extends classical query optimization with data-aware planning, combining atomic query decomposition and operator reordering to minimize semantic workload. The framework also features a dual-engine execution architecture that dynamically routes tasks between a relational database and an LLM module, using operator-aware batching to scale efficiently. Extensive experiments across a diverse suite of structured and semi-structured table question answering benchmarks demonstrate that OmniTQA consistently outperforms existing symbolic, semantic, and hybrid baselines in both accuracy and cost efficiency. These gains are particularly pronounced for complex queries, large tables and multi-relation schemas.
