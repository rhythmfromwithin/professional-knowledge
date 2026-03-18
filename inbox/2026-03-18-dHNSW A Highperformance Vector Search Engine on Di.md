---
title: "d-HNSW: A High-performance Vector Search Engine on Disaggregated Memory"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.13591
priority: low
status: unread
interest: medium
next_step: skim
---
# d-HNSW: A High-performance Vector Search Engine on Disaggregated Memory
> 原文: [https://arxiv.org/abs/2603.13591](https://arxiv.org/abs/2603.13591)

arXiv:2603.13591v1 Announce Type: new
Abstract: Efficient vector search is essential for powering large-scale AI applications, such as LLMs. Existing solutions are designed for monolithic architectures where compute and memory are tightly coupled. Recently, disaggregated architecture breaks this coupling by separating compution and memory resources into independently scalable pools to improve utilization. However, applying vector database on disaggregated memory system brings unique challenges to system design due to its graph-based index. We present d-HNSW, the first RDMA-based vector search engine optimized for disaggregated memory systems. d-HNSW preserves HNSW's high accuracy while addressing the new system-level challenges introduced by disaggregation: 1) network inefficiency from pointer-chasing traversals, 2) non-contiguous remote memory layout induced by dynamic insertions, 3) redundant data transfers in batch workloads, and 4) resource underutilization due to sequential execution. d-HNSW tackles these challenges through a set of hardware-algorithm co-designed techniques, including 1) balanced clustering with a lightweight representative index to reduce network round-trips and ensure predictable latency, 2) an RDMA-friendly graph layout that preserves data contiguity under dynamic insertions, 3) query-aware data loading to eliminate redundant fetches across batch queries, and 4) a pipelined execution model that overlaps RDMA transfers with computation to hide network latency and improve throughput. Our evaluation results in a public cloud show that d-HNSW achieves up to < 10-2x query latency and > 100x query throughput compared to other baselines, while maintaining a high recall of 94%.
