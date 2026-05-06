---
interest: medium
link: https://arxiv.org/abs/2605.01260
next_step: skim
priority: low
slack_ts: '1778039504.766699'
source: cs.DB - Databases
status: unread
title: 'Write-Read Decoupling in Modern Large-Scale Search Engines: Architectures,
  Techniques, and Emerging Approaches'
---
# Write-Read Decoupling in Modern Large-Scale Search Engines: Architectures, Techniques, and Emerging Approaches
> 原文: [https://arxiv.org/abs/2605.01260](https://arxiv.org/abs/2605.01260)

arXiv:2605.01260v1 Announce Type: new
Abstract: Large-scale search engines face a fundamental tension: the index must be updated frequently to maintain freshness, yet updates create resource contention that inflates query latency. In the dominant Lucene-based architecture, segment merges triggered by writes compete with concurrent queries for CPU cycles, disk I/O bandwidth, and operating-system page cache -- a problem we term \emph{write-read contention}. This survey systematically examines the architectural solutions that industry and academia have developed to decouple write pressure from read latency. We identify five principal patterns: (i)~node-level read-write separation; (ii)~compute-storage separation; (iii)~full in-memory indexing; (iv)~log-structured write paths; and (v)~in-place partial updates. We survey representative systems including Elasticsearch, LinkedIn Galene, Uber Sia, Quickwit, Alibaba Havenask, Algolia, Milvus, and Vespa, and discuss an emerging synthesis -- the ScaleSearch architecture -- that combines compute-storage separation with full in-memory indexing and dedicated write nodes. A key contribution of ScaleSearch is \emph{per-field update routing}: each field is assigned its own Kafka topic and update path, allowing scalar fields (price, stock, tags) to be updated in-place in $O(1)$ RAM with immediate visibility while full-text fields follow the segment-based compute-storage path. We conclude with open challenges in hybrid vector-and-full-text retrieval, serverless deployments, and AI-integrated search.
