---
interest: medium
link: https://arxiv.org/abs/2609.09243
next_step: skim
priority: low
slack_ts: '1789013738.193049'
source: cs.CR - Cryptography and Security
status: unread
title: In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under
  Document Poisoning
---
# In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under Document Poisoning
> 原文: [https://arxiv.org/abs/2609.09243](https://arxiv.org/abs/2609.09243)

arXiv:2609.09243v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) grounds a language model in retrieved documents, which reduces hallucination but creates a new attack surface: if retrieved text is tampered with, the model may repeat the falsehood. We study how much a small quantized model, Llama 3.1 8B, degrades when a fraction of its retrieved context is poisoned. Three corruption strategies are tested, entity swap, number swap, and negation, each applied to zero, one, two, or three of the three retrieved passages, over a factorial sweep of 588 runs on a fact-checking task built from FEVER. Accuracy falls from 77.9% on clean context to 43.5% when all three passages are corrupted. Entity swap flips the largest share of answers that were correct on clean context. Number-based corruption stays flat while poisoned passages are a minority and jumps once they form a majority, a pattern we re-check with query-level bootstrap intervals. The model rarely invents new falsehoods; its dominant reaction is to abstain, and a lexical overlap proxy of unsupported generation falls under attack rather than rising. The study is a small-scale measurement with coarse automated labels; we treat the strategy contrasts as suggestive until decoding is controlled and stronger adjudication is in place.
