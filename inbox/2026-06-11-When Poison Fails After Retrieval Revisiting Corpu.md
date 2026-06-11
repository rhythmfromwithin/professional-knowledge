---
title: "When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.11265
priority: low
status: unread
interest: medium
next_step: skim
---
# When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines
> 原文: [https://arxiv.org/abs/2606.11265](https://arxiv.org/abs/2606.11265)

arXiv:2606.11265v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are often fragmented during chunking, while rerankers favor locally coherent and answer-bearing passages rather than globally optimized semantic similarity. Based on this observation, we propose Chunk-aware and Rerank-Consistent Poisoning (CRCP), a poisoning framework that jointly optimizes retrieval relevance, reranker consistency, and chunk-boundary robustness. CRCP explicitly models chunking transformations during optimization to generate locally self-contained adversarial passages that remain effective under varying chunking configurations. Experiments on standard RAG benchmarks with multiple retrievers and rerankers show that existing poisoning methods are highly sensitive to chunk size and reranking strategies, whereas CRCP achieves substantially higher attack success rates and stronger robustness across realistic retrieval pipelines. Our findings highlight an important realism gap in current RAG security evaluation and suggest that poisoning in modern RAG systems should be studied as a multi-stage retrieval consistency problem rather than a retrieval-only problem.
