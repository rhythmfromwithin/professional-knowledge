---
title: "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.18034
priority: low
status: unread
interest: medium
next_step: skim
---
# Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems
> 原文: [https://arxiv.org/abs/2603.18034](https://arxiv.org/abs/2603.18034)

arXiv:2603.18034v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge sources but introduce new attack surfaces through the retrieval pipeline. In particular, adversaries can poison retrieval corpora so that malicious documents are preferentially retrieved at inference time, enabling targeted manipulation of model outputs. We study gradient-guided corpus poisoning attacks against modern RAG pipelines and evaluate retrieval-layer defenses that require no modification to the underlying LLM.
We implement dual-document poisoning attacks consisting of a sleeper document and a trigger document optimized using Greedy Coordinate Gradient (GCG). In a large-scale evaluation on the Security Stack Exchange corpus (67,941 documents) with 50 attack attempts, gradient-guided poisoning achieves a 38.0 percent co-retrieval rate under pure vector retrieval.
We show that a simple architectural modification, hybrid retrieval combining BM25 and vector similarity, substantially mitigates this attack. Across all 50 attacks, hybrid retrieval reduces gradient-guided attack success from 38 percent to 0 percent without modifying the model or retraining the retriever. When attackers jointly optimize payloads for both sparse and dense retrieval signals, hybrid retrieval can be partially circumvented, achieving 20-44 percent success, but still significantly raises attack difficulty relative to vector-only retrieval.
Evaluation across five LLM families (GPT-5.3, GPT-4o, Claude Sonnet 4.6, Llama 4, and GPT-4o-mini) shows attack success ranging from 46.7 percent to 93.3 percent. Cross-corpus evaluation on the FEVER Wikipedia dataset (25 attacks) yields 0 percent attack success across all retrieval configurations.
