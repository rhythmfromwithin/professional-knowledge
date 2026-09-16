---
interest: medium
link: https://arxiv.org/abs/2609.14255
next_step: skim
priority: low
slack_ts: '1789532923.698749'
source: cs.DB - Databases
status: unread
title: Towards Anticipatory Databases Through Shared Data and Workload Semantics
---
# Towards Anticipatory Databases Through Shared Data and Workload Semantics
> 原文: [https://arxiv.org/abs/2609.14255](https://arxiv.org/abs/2609.14255)

arXiv:2609.14255v1 Announce Type: new
Abstract: Database management systems increasingly serve dynamic and exploratory workloads, yet many of their decisions still rely on low-level signals such as recency, frequency, and address locality. These signals capture how data was accessed, but not what is being examined or how an analytical focus evolves. We argue for treating workload semantics as a first-class control signal for anticipatory decision making. Central to this view, we introduce semantic locality and semantic trajectories, which capture relationships among nearby queries and how those relationships evolve across a session.
We propose a framework that represents semantic context at the data, query, and session levels, models its evolution over time, and translates it into task-specific utility estimates. We instantiate this framework in semantic prefetching and semantic cache eviction, which share a semantic layer to make two separate decisions. Prefetching uses semantic trajectories to anticipate future accesses beyond what address-based locality can capture, while eviction uses semantic relevance to inform block replacement. These systems provide initial evidence that shared semantic context can support multiple DBMS components. We further outline how this principle can extend to other decisions and data systems, and discuss key challenges in representation, cost, adaptation, and evaluation.
