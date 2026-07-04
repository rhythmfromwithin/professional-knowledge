---
interest: medium
link: https://arxiv.org/abs/2607.01276
next_step: skim
priority: low
slack_ts: '1783136962.109519'
source: cs.CR - Cryptography and Security
status: unread
title: Embedding Inference Attack
---
# Embedding Inference Attack
> 原文: [https://arxiv.org/abs/2607.01276](https://arxiv.org/abs/2607.01276)

arXiv:2607.01276v1 Announce Type: new
Abstract: Embedding models are essential components of modern Information Retrieval (IR) systems, yet they are typically hidden behind APIs. Recent works have shown that dense IR system can lead to security vulnerabilities such as embedding inversion attacks. However, such attacks usually require that the attacker knows the embedding model for the attack to be applicable. In this paper, we study IR systems under a black-box setting in which the adversary observes only the unordered set of retrieved documents, without ranking or similarity scores. We demonstrate that in such contexts, tailored queries allow an adversary to identify which embedding model is in use from a set of known model candidate, which we coin as an embedding inference attack (EIA). We also show that certain queries remain discriminative even when the system includes a reranker as a potential defense mechanism. We further validate our method on a real Retrieval-Augmented Generation (RAG) system, in which the tailored queries bypass the LLM's tendency to reject inputs it does not recognize as well-formed questions. Finally, we propose and evaluate other mitigation strategies such as similarity thresholds.
