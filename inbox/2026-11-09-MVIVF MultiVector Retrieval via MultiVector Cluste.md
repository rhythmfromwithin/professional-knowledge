---
interest: medium
link: https://arxiv.org/abs/2611.09040
next_step: skim
priority: low
slack_ts: '1794293799.280089'
source: cs.DB - Databases
status: unread
title: 'MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering'
---
# MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering
> 原文: [https://arxiv.org/abs/2611.09040](https://arxiv.org/abs/2611.09040)

arXiv:2611.09040v1 Announce Type: cross
Abstract: Multi-vector retrieval represents each query and document as a set of embeddings and scores relevance via fine-grained set-to-set interactions such as MaxSim (Chamfer similarity). This expressiveness improves retrieval quality over single-vector representations, but makes search substantially more expensive. Existing systems address this challenge primarily through proxy representations or filter-and-rerank pipelines that reduce candidate generation to single-vector search. We study the complementary direction of building a native IVF-style index directly over multi-vector data.
We introduce MV-IVF, an inverted-file index for multi-vector retrieval built on MV-Lloyd, a new Lloyd-style algorithm for clustering point clouds under a Chamfer objective. Our key observation is that once point clouds are assigned to clusters, the center-update step reduces to standard single-vector clustering over the flattened embeddings in each cluster. This enables efficient construction of a hierarchical IVF tree with center point clouds at internal nodes.
At query time, MV-IVF performs best-first beam search over the tree to identify promising leaf clusters, then scores the documents in those leaves. We further accelerate search using low-bit quantization, query compression, and cache-efficient batched search. We implement MV-IVF in MVSIC, an optimized C++ library and unified evaluation framework for multi-vector retrieval that includes several major approaches. Across BEIR and LoTTE text retrieval benchmarks, MV-IVF achieves strong latency--recall tradeoffs, the best batched throughput frontiers, and favorable build-time and index-size profiles. At $90\%$ Recall-$10$@$10$, MV-IVF achieves up to $8.03\times$ lower single-query latency and up to $173.5\times$ higher QPS than the baselines, demonstrating that native IVF-style indexing is practical and effective for scalable multi-vector retrieval.
