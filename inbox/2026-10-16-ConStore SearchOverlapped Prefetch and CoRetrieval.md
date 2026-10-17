---
interest: medium
link: https://arxiv.org/abs/2610.21676
next_step: skim
priority: low
slack_ts: '1792209646.916029'
source: cs.DB - Databases
status: unread
title: 'ConStore: Search-Overlapped Prefetch and Co-Retrieval-Aware Content Storage
  for Disk-Based ANNS'
---
# ConStore: Search-Overlapped Prefetch and Co-Retrieval-Aware Content Storage for Disk-Based ANNS
> 原文: [https://arxiv.org/abs/2610.21676](https://arxiv.org/abs/2610.21676)

arXiv:2610.21676v1 Announce Type: new
Abstract: Disk-based approximate nearest-neighbor search (ANNS) supports retrieval-augmented generation (RAG), search, recommendation, and advertising over corpora that exceed memory capacity. Existing ANNS research often focuses on vector search at small top-K, whereas industrial-scale applications require larger retrieval sets. Fetching the corresponding content from storage remains comparatively underexplored. Our profiling across million- to billion-vector corpora shows that, at large K, content fetch latency can match or exceed vector-search latency and cannot be ignored in end-to-end retrieval.
We present ConStore, a content storage engine combining two complementary techniques to reduce end-to-end retrieval latency. Speculative Inline Content Prefetch (SICP) commonly abstracts graph-based and cluster-based ANNS as progressive SSD I/O that refines an in-flight candidate queue. It prefetches content for stable leading candidates under a bounded I/O budget, overlapping content reads with search without changing the final top-K results. Co-Retrieval-Pattern-Aware Grouping (RPAG) uses query logs to place frequently co-retrieved documents in contiguous segments. Workload-Adaptive Segment Reorganization (WASR) adapts this layout to workload shifts by selectively regrouping segments under a bounded rewrite budget. Group Content Fetch (GCF) exploits this layout to coalesce per-document random reads into batched, page-aware I/O requests. SICP works independently of the content layout, while RPAG and GCF reduce fetch cost even without prefetching.
Across three multi-hop QA workloads with K from 10 to 1600, ConStore reduces end-to-end retrieval latency over the best per-document-read baseline by up to 48% on DiskANN and 25% on SPANN. Separate experiments on 100M- and billion-vector indexes demonstrate SICP's applicability at larger scales.
