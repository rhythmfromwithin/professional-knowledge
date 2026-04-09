---
interest: medium
link: https://arxiv.org/abs/2604.03240
next_step: skim
priority: high
slack_ts: '1775703385.761439'
source: cs.LG - Machine Learning
status: unread
title: 'Scaling DPPs for RAG: Density Meets Diversity'
---
# Scaling DPPs for RAG: Density Meets Diversity
> 原文: [https://arxiv.org/abs/2604.03240](https://arxiv.org/abs/2604.03240)

arXiv:2604.03240v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by grounding generation in external knowledge, yielding relevance responses that are aligned with factual evidence and evolving corpora. Standard RAG pipelines construct context through relevance ranking, performing point-wise scoring between the user query and each corpora chunk. This formulation, however, ignores interactions among retrieved candidates, leading to redundant contexts that dilute density and fail to surface complementary evidence. We argue that effective retrieval should optimize jointly for both density and diversity, ensuring the grounding evidence that is dense in information yet diverse in coverage. In this study, we propose ScalDPP, a diversity-aware retrieval mechanism for RAG that incorporates Determinantal Point Processes (DPPs) through a lightweight P-Adapter, enabling scalable modeling of inter-chunk dependencies and complementary context selection. In addition, we develop a novel set-level objective, Diverse Margin Loss (DML), that enforces ground-truth complementary evidence chains to dominate any equally sized redundant alternatives under DPP geometry. Experimental results demonstrate the superiority of ScalDPP, substantiating our core statement in practice.
