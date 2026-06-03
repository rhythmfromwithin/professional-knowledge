---
interest: medium
link: https://arxiv.org/abs/2606.03001
next_step: skim
priority: medium
slack_ts: '1780462702.417809'
source: cs.DC - Distributed Computing
status: unread
title: 'FOLD: Fuzzy Online Deduplication for Very Large Evolving Datasets via Approximate
  Nearest Neighbor Search'
---
# FOLD: Fuzzy Online Deduplication for Very Large Evolving Datasets via Approximate Nearest Neighbor Search
> 原文: [https://arxiv.org/abs/2606.03001](https://arxiv.org/abs/2606.03001)

arXiv:2606.03001v1 Announce Type: new
Abstract: Fuzzy deduplication is key to constructing large language model training corpora. However, classic Locality-Sensitive Hashing pipelines scale poorly as corpora grow and are ill-suited to continuous ingestion. We present FOLD (Fuzzy Online Deduplication), an online fuzzy deduplication system that delivers high recall and throughput for evolving datasets. FOLD maintains an incrementally updated HNSW index over admitted documents, retrieving a small, high-quality candidate neighborhood for each incoming document instead of repeatedly rebuilding global buckets or rescanning the accumulated corpus. To our knowledge, FOLD is the first online fuzzy deduplication system to use HNSW. However, applying Jaccard similarity out of the box causes score crowding, making graph traversal unreliable within a small number of steps. FOLD addresses this with a bitmap representation that provides a more discriminative, Jaccard-aligned signal during HNSW search. Across four LLM-scale datasets (LM1B, C4, RealNews, and Common Crawl), FOLD stays fast and accurate as the corpus grows: at the largest evaluated scales, it maintains 93-97% recall and achieves up to 2.09x higher throughput than competing alternatives, whose best recall reaches only 76%.
