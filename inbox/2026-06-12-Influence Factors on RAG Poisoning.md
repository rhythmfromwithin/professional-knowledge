---
interest: medium
link: https://arxiv.org/abs/2606.12469
next_step: skim
priority: low
slack_ts: '1781239684.710809'
source: cs.CR - Cryptography and Security
status: unread
title: Influence Factors on RAG Poisoning
---
# Influence Factors on RAG Poisoning
> 原文: [https://arxiv.org/abs/2606.12469](https://arxiv.org/abs/2606.12469)

arXiv:2606.12469v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time. However, this reliance on retrieved content introduces vulnerabilities to poisoning attacks, in which adversarial documents can manipulate both the retrieval process and the generated outputs. This paper investigates poisoning robustness in RAG through a full factorial experimental study covering 432 configurations. We analyze the impacts of dataset, retriever type, retrieval depth, database composition, chunking strategy, and generator model on retrieval-level and generation-level metrics. The results show that retriever architecture, dataset, and retrieval depth are the strongest factors affecting poisoning exposure, while generator choice and database composition have a major impact on downstream attack success. Dense and graph-based retrievers generally improve robustness relative to BM25, whereas larger retrieval depth increases the likelihood of retrieving poisoned passages. We further show that replicating poisoned content across multiple databases amplifies adversarial influence, while additional clean sources can mitigate it. These findings highlight that poisoning vulnerability in RAG is not attributable to a single component, but instead arises from the interaction of retrieval, generation, and knowledge-base configuration.
