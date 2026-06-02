---
interest: medium
link: https://arxiv.org/abs/2606.00734
next_step: skim
priority: low
slack_ts: '1780375678.563839'
source: cs.DB - Databases
status: unread
title: 'EMA: Approximate Nearest Neighbor Search with General Attribute Filtering
  and Dynamic Updates'
---
# EMA: Approximate Nearest Neighbor Search with General Attribute Filtering and Dynamic Updates
> 原文: [https://arxiv.org/abs/2606.00734](https://arxiv.org/abs/2606.00734)

arXiv:2606.00734v1 Announce Type: new
Abstract: Filtering Approximate Nearest Neighbor (FANN) search is a critical and emerging task for strengthening the query capability of vector databases, supporting applications such as recommendation systems, retrieval-augmented generation (RAG), and agent memory. However, most existing methods are limited to range or label filtering, often incurring unacceptable index construction time and memory overhead. Predicate-agnostic approaches further struggle to handle a wide range of predicate selectivities effectively. In this paper, we propose EMA, a filtering ANN algorithm that supports multi-predicate queries over mixed numerical and categorical attributes, and efficient dynamic updates. EMA introduces Markers as compact summaries attached to graph edges, providing conservative predicate- and geometric-aware guidance with zero false negatives at the Marker level. During query processing, EMA performs Marker-augmented joint search with a bounded edge recovery mechanism, enabling efficient filtering while preserving graph navigability. Extensive experiments demonstrate that EMA achieves 1.68x--12.25x speedup over state-of-the-art general filtering ANN methods across diverse workloads.
