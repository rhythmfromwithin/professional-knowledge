---
interest: medium
link: https://arxiv.org/abs/2607.22031
next_step: skim
priority: low
slack_ts: '1785380028.301059'
source: cs.DB - Databases
status: unread
title: 'IDSTune: A Multi-Agent Collaborative Framework for Integrated Database System
  Tuning'
---
# IDSTune: A Multi-Agent Collaborative Framework for Integrated Database System Tuning
> 原文: [https://arxiv.org/abs/2607.22031](https://arxiv.org/abs/2607.22031)

arXiv:2607.22031v1 Announce Type: new
Abstract: Database tuning is critical for achieving high performance in modern database management systems (DBMSs). Existing methods typically optimize a single component---knobs, indexes, or materialized views---without accounting for their interdependencies. This limitation arises because these components require different tuning strategies and are difficult to integrate within a unified framework. As a result, directly extending a method to multiple components or simply combining separate methods often fails to capture cross-component collaboration and shared tuning signals. Moreover, existing methods are insufficient for handling diverse workloads, evolving data, and dynamic query patterns.
To address these limitations, we propose IDSTune, an integrated tuning framework that jointly optimizes multiple configuration components through LLM-driven multi-agent collaboration. IDSTune operates in two phases: (i) workload compression, which extracts and selects task-relevant features, and (ii) configuration recommendation, where specialized agents collaboratively generate and refine configurations for knobs, indexes, and materialized views under the supervision of a centralized coordinator. By incorporating feedback and external knowledge retrieval, IDSTune achieves efficient and globally consistent tuning. Extensive experiments show that IDSTune achieves up to 38% performance improvement and 57% faster tuning, with strong adaptability across diverse scenarios.
