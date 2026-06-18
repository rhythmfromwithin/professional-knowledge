---
title: "SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2606.18381
priority: high
status: unread
interest: medium
next_step: skim
---
# SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG
> 原文: [https://arxiv.org/abs/2606.18381](https://arxiv.org/abs/2606.18381)

arXiv:2606.18381v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) systems must balance retrieval granularity with contextual coherence, a challenge that existing methods address through LLM-guided chunking, single-level context expansion, or hierarchical summarization. These approaches variously depend on costly LLM calls during indexing or retrieval, limit context aggregation to a single granularity level, or introduce information loss through summarization. We present SproutRAG, an attention-guided hierarchical RAG framework that addresses this trade-off by organizing sentence-level chunks into progressively larger but semantically coherent units, using learned inter-sentence attention to construct a binary chunking tree. Unlike prior approaches that rely on external LLMs, fixed context expansion, or lossy summarization, SproutRAG learns which attention heads and layers best capture semantic document structure, enabling multi-granularity retrieval without additional LLM calls or compressed summaries. At retrieval time, SproutRAG uses hierarchical beam search to retrieve candidates at multiple granularities, capturing multi-sentence relevance beyond flat retrieval. The framework is trained end-to-end with a joint objective that improves both embeddings and tree structure. Experiments across four benchmarks spanning scientific, legal, and open-domain settings demonstrate that SproutRAG improves information efficiency (IE) by 6.1% on average over the strongest baseline. Code is available on https://github.com/AmirAbaskohi/SproutRAG.
