---
interest: medium
link: https://arxiv.org/abs/2610.11230
next_step: skim
priority: low
slack_ts: '1791524745.915079'
source: cs.DB - Databases
status: unread
title: 'CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at
  Scale'
---
# CORAL: Cross-modal Vector Retrieval via Incremental Graph Construction at Scale
> 原文: [https://arxiv.org/abs/2610.11230](https://arxiv.org/abs/2610.11230)

arXiv:2610.11230v1 Announce Type: new
Abstract: Cross-modal vector retrieval is widely used in multimodal systems, such as search engines and vector databases. It typically operates in out-of-distribution (OOD) settings, where query vectors follow a distribution that differs from that of the vectors stored in the database. In such cases, conventional indexes suffer significant performance degradation, and even methods specially designed for OOD remain limited by inefficient use of query modal characteristics, restricted GPU parallelism, and inadequate support for dynamic updates. We present CORAL, a novel GPU-accelerated graph-based vector index for scalable cross-modal retrieval, featuring hierarchical memory management that spans GPU, CPU, and disk. Specifically, CORAL incrementally incorporates the characteristics of query modality and terminates index construction timely. Crucially, it introduces coverage-aware adaptive pruning to address the imbalanced coverage of the query vector's neighbors. Moreover, CORAL presents a fully neighborhood-aware projection approach to efficiently utilize GPUs for highly parallel index construction, and a targeted connectivity enhancement method to refine the index structure. Besides, CORAL also supports modal-semantics-based vector insertion and topology-repairing deletion that restore node connectivity. Experimental results demonstrate that CORAL outperforms existing methods with up to 1.6 times the throughput at matched recall while reducing construction time by up to 56%. Furthermore, it exhibits remarkable resilience under dynamic updates and remains effective at the billion scale.
