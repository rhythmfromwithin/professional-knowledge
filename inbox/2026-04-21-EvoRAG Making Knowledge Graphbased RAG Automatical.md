---
interest: medium
link: https://arxiv.org/abs/2604.15676
next_step: skim
priority: low
slack_ts: '1776742304.405469'
source: cs.DB - Databases
status: unread
title: 'EvoRAG: Making Knowledge Graph-based RAG Automatically Evolve through Feedback-driven
  Backpropagation'
---
# EvoRAG: Making Knowledge Graph-based RAG Automatically Evolve through Feedback-driven Backpropagation
> 原文: [https://arxiv.org/abs/2604.15676](https://arxiv.org/abs/2604.15676)

arXiv:2604.15676v1 Announce Type: new
Abstract: Knowledge Graph-based Retrieval-Augmented Generation (KG-RAG) has emerged as a promising paradigm for enhancing LLM reasoning by retrieving multi-hop paths from KGs. However, existing KG-RAG frameworks often underperform in real-world scenarios because the pre-captured knowledge dependencies are not tailored to the downstream task or its evolving requirements. These frameworks struggle to adapt to task-specific requirements and lack mechanisms to filter low-contribution knowledge during generation. We observe that feedback on generated responses offers effective supervision for improving KG quality, as it directly reflects user expectations and provides insights into the correctness and usefulness of the output. However, a key challenge lies in effectively linking response-level feedback to triplet-level contribution evaluation and knowledge updates in the KG.
In this work, we propose EvoRAG, a self-evolving KG-RAG framework that leverages the feedback over generated responses to continuously refine the KG and enhance reasoning accuracy. EvoRAG introduces a feedback-driven backpropagation mechanism that attributes feedback to retrieved paths by measuring their utility for response and propagates this utility back to individual triplets, supporting fine-grained KG refinements towards more adaptive and accurate reasoning. Through EvoRAG, we establish a closed loop that couples feedback, LLM, and graph data, continuously enhancing the performance and robustness in real-world scenarios. Experimental results show that EvoRAG improves reasoning accuracy by $7.34\%$ over state-of-the-art KG-RAG frameworks. The source code has been made available at https://github.com/iDC-NEU/EvoRAG.
