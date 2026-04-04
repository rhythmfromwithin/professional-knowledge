---
title: "A Reliability Evaluation of Hybrid Deterministic-LLM Based Approaches for Academic Course Registration PDF Information Extraction"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.00003
priority: high
status: unread
interest: medium
next_step: skim
---
# A Reliability Evaluation of Hybrid Deterministic-LLM Based Approaches for Academic Course Registration PDF Information Extraction
> 原文: [https://arxiv.org/abs/2604.00003](https://arxiv.org/abs/2604.00003)

arXiv:2604.00003v1 Announce Type: new
Abstract: This study evaluates the reliability of information extraction approaches from KRS documents using three strategies: LLM only, Hybrid Deterministic - LLM (regex + LLM), and a Camelot based pipeline with LLM fallback. Experiments were conducted on 140 documents for the LLM based test and 860 documents for the Camelot based pipeline evaluation, covering four study programs with varying data in tables and metadata. Three 12 - 14B LLM models (Gemma 3, Phi 4, and Qwen 2.5) were run locally using Ollama and a consumer grade CPU without a GPU. Evaluations used exact match (EM) and Levenshtein similarity (LS) metrics with a threshold of 0.7. Although not applicable to all models, the results show that the hybrid approach can improve efficiency compared to LLM only, especially for deterministic metadata. The Camelot based pipeline with LLM fallback produced the best combination of accuracy (EM and LS up to 0.99 - 1.00) and computational efficiency (less than 1 second per PDF in most cases). The Qwen 2.5:14b model demonstrated the most consistent performance across all scenarios. These findings confirm that integrating deterministic and LLM methods is increasingly reliable and efficient for information extraction from text based academic documents in computationally constrained environments.
