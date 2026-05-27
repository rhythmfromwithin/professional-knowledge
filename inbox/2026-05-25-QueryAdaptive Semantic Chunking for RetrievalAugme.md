---
interest: medium
link: https://arxiv.org/abs/2605.22834
next_step: skim
priority: high
slack_ts: '1779856024.857329'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Query-Adaptive Semantic Chunking for Retrieval-Augmented Generation: A Dynamic
  Strategy with Contextual Window Expansion'
---
# Query-Adaptive Semantic Chunking for Retrieval-Augmented Generation: A Dynamic Strategy with Contextual Window Expansion
> 原文: [https://arxiv.org/abs/2605.22834](https://arxiv.org/abs/2605.22834)

arXiv:2605.22834v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) systems depend critically on document chunking quality for retrieving relevant context. Fixed chunking segments documents into uniform units irrespective of semantics or user intent, producing a precision-recall trade-off unresolvable by tuning chunk size alone. Semantic and agentic methods partially address these limitations but do not integrate user queries at the chunking stage. We present Query-Adaptive Semantic Chunking (QASC), which dynamically constructs chunks by integrating queries into segmentation through three mechanisms: cosine similarity scoring between sentence and query embeddings to identify seed sentences, contextual window expansion around seeds to preserve coherence, and chunk-level score aggregation to ensure holistic relevance. We evaluate QASC on 100 technical documents across 200 queries spanning four types, comparing against fixed chunking at five granularities, recursive splitting, semantic chunking, and agentic chunking. QASC achieves an F1-score of 0.85, a relative improvement of 18-27% over fixed chunking and 8-12% over semantic and agentic alternatives. Ablation studies confirm each component contributes meaningfully. Human evaluation by three annotators (Cohen kappa = 0.82) corroborates that QASC produces more relevant and coherent chunks than existing methods.
