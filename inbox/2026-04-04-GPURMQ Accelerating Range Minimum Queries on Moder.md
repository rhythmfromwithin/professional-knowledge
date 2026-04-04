---
interest: medium
link: https://arxiv.org/abs/2604.01811
next_step: skim
priority: low
slack_ts: '1775270927.331869'
source: cs.DB - Databases
status: unread
title: 'GPU-RMQ: Accelerating Range Minimum Queries on Modern GPUs'
---
# GPU-RMQ: Accelerating Range Minimum Queries on Modern GPUs
> 原文: [https://arxiv.org/abs/2604.01811](https://arxiv.org/abs/2604.01811)

arXiv:2604.01811v1 Announce Type: new
Abstract: Range minimum queries are frequently used in string processing and database applications including biological sequence analysis, document retrieval, and web search. Hence, various data structures have been proposed for improving their efficiency on both CPUs and GPUs.Recent work has also shown that hardware-accelerated ray tracing on modern NVIDIA RTX graphic cards can be exploited to answer range minimum queries by expressing queries as rays, which are fired into a scene of triangles representing minima of ranges at different granularities. While these approaches are promising, they suffer from at least one of three issues: severe memory overhead, high index construction time, and low query throughput. This renders these methods practically unusable on larger arrays: For example, the state-of-art GPU-based approaches LCA and RTXRMQ exceed the memory capacity of an NVIDIA RTX 4090 GPU for input arrays of size >= 2^29. To tackle these problems, in this work, we present a new approach called GPU-RMQ which is based on a hierarchical approach. GPU-RMQ first constructs a hierarchy of range minimum summaries on top of the original array in a highly parallel fashion. For query answering, only the relevant portions of the hierarchy are then processed in an optimized massively-parallel scan operation. Additionally, GPU-RMQ is hybrid in design enabling the use of both ray tracing cores and CUDA cores across different levels of the hierarchy to handle queries. Our experimental evaluation shows that GPU-RMQ outperforms the state-of-the-art approaches in terms of query throughput especially for larger arrays while offering a significantly lower memory footprint and up to two orders-of-magnitude faster index construction. In particular, it achieves up to ~8x higher throughput than LCA, ~17x higher throughput than RTXRMQ, and up to ~4800x higher throughput compared to an optimized CPU-based approach.
