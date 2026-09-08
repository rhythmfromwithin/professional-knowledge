---
interest: medium
link: https://arxiv.org/abs/2609.05014
next_step: skim
priority: low
slack_ts: '1788840731.241429'
source: cs.DB - Databases
status: unread
title: 'Reducing the Cross-Model Tax: Query Optimization over Multi-Model Data'
---
# Reducing the Cross-Model Tax: Query Optimization over Multi-Model Data
> 原文: [https://arxiv.org/abs/2609.05014](https://arxiv.org/abs/2609.05014)

arXiv:2609.05014v1 Announce Type: new
Abstract: Querying across heterogeneous data models incurs substantial overhead from query decomposition, data transfer, and processing outside the underlying database systems. We show that, in the evaluated decomposition-based architecture, a substantial part of this cross-model tax is not inherent to heterogeneity itself, but results from avoidable decisions made by the unifying query processor.
We present a mapping- and capability-aware optimization approach that systematically moves processing closer to the data. It combines model-aware predicate pushdown, cross-model dependent joins, and non-redundant query-part construction within a unified optimization pipeline applicable across relational, document, and graph databases.
The approach is implemented in MM-quecat and evaluated over PostgreSQL, MongoDB, Neo4j, and their heterogeneous combination. It reduces query latency by up to two orders of magnitude, eliminates all out-of-memory failures observed in the original single-DBMS experiments, provides further order-of-magnitude improvements through dependent execution, and reduces planning time for complex graph plans from hundreds of milliseconds to several milliseconds. The results demonstrate that established optimization principles can be generalized across data-model and system boundaries and can substantially improve the efficiency and robustness of decomposition-based multi-model query processing.
