---
interest: medium
link: https://arxiv.org/abs/2604.07403
next_step: skim
priority: low
slack_ts: '1775964765.548329'
source: cs.CR - Cryptography and Security
status: unread
title: 'RefineRAG: Word-Level Poisoning Attacks via Retriever-Guided Text Refinement'
---
# RefineRAG: Word-Level Poisoning Attacks via Retriever-Guided Text Refinement
> 原文: [https://arxiv.org/abs/2604.07403](https://arxiv.org/abs/2604.07403)

arXiv:2604.07403v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs), but simultaneously exposes a critical vulnerability to knowledge poisoning attacks. Existing attack methods like PoisonedRAG remain detectable due to coarse-grained separate-and-concatenate strategies. To bridge this gap, we propose RefineRAG, a novel framework that treats poisoning as a holistic word-level refinement problem. It operates in two stages: Macro Generation produces toxic seeds guaranteed to induce target answers, while Micro Refinement employs a retriever-in-the-loop optimization to maximize retrieval priority without compromising naturalness. Evaluations on NQ and MSMARCO demonstrate that RefineRAG achieves state-of-the-art effectiveness, securing a 90% Attack Success Rate on NQ, while registering the lowest grammar errors and repetition rates among all baselines. Crucially, our proxy-optimized attacks successfully transfer to black-box victim systems, highlighting a severe practical threat.
