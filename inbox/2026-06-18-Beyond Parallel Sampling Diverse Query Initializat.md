---
interest: medium
link: https://arxiv.org/abs/2606.17209
next_step: skim
priority: high
slack_ts: '1781759639.684219'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search'
---
# Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search
> 原文: [https://arxiv.org/abs/2606.17209](https://arxiv.org/abs/2606.17209)

arXiv:2606.17209v1 Announce Type: new
Abstract: Test-time scaling for agentic search typically increases depth (i.e., more turns and tokens per trajectory) or breadth (i.e., more parallel rollouts). Here we focus on breadth scaling, showing that standard parallel sampling yields diminishing returns, tracing this to query redundancy at the first turn. When models issue similar first queries across rollouts, the threads retrieve overlapping evidence, and subsequent turns are conditioned on this shared retrieval. We address this limitation with DivInit, a training-free intervention at the first turn. Rather than sampling k independent first queries, DivInit draws n candidates from a single call, picks k < n diverse seeds, and runs them as parallel trajectories. Across five open-weight models and eight benchmarks, DivInit consistently improves over standard parallel sampling, with average gains of five to seven points on multi-hop QA at matched compute. Code available at https://github.com/cxcscmu/diverse-query-initialization
