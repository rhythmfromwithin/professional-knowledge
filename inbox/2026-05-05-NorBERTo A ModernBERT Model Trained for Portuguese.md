---
title: "NorBERTo: A ModernBERT Model Trained for Portuguese with 331 Billion Tokens Corpus"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.00086
priority: high
status: unread
interest: medium
next_step: skim
---
# NorBERTo: A ModernBERT Model Trained for Portuguese with 331 Billion Tokens Corpus
> 原文: [https://arxiv.org/abs/2605.00086](https://arxiv.org/abs/2605.00086)

arXiv:2605.00086v1 Announce Type: new
Abstract: High-quality corpora are essential for advancing Natural Language Processing (NLP) in Portuguese. Building on previous encoder-only models such as BERTimbau and Albertina PT-BR, we introduce NorBERTo, a modern encoder based on the ModernBERT architecture, featuring long-context support and efficient attention mechanisms. NorBERTo is trained on Aurora-PT, a newly curated Brazilian Portuguese corpus comprising 331 billion GPT-2 tokens collected from diverse web sources and existing multilingual datasets. We systematically benchmark NorBERTo against Strong baselines on semantic similarity, textual entailment and classification tasks using standardized datasets such as ASSIN 2 and PLUE. On PLUE, NorBERTo-large achieves the best results among the encoder models we evaluated, notably reaching 0.9191 F1 on MRPC and 0.7689 accuracy on RTE. On ASSIN 2, NorBERTo-large attains the highest entailment F1 (~0.904) among all encoders considered, although Albertina-900M and BERTimbau-large still hold an advantage. To the best of our knowledge, Aurora-PT is currently the largest openly available monolingual Portuguese corpus, surpassing previous resources. NorBERTo provides a modern, mid-sized encoder designed for realistic deployment scenarios: it is straight-forward to fine-tune, efficient to serve, and well suited as a backbone for retrieval-augmented generation and other downstream Portuguese NLP systems.
