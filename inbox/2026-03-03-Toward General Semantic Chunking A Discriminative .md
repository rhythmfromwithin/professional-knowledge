---
title: "Toward General Semantic Chunking: A Discriminative Framework for Ultra-Long Documents"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2602.23370
priority: high
status: unread
interest: medium
next_step: skim
---
# Toward General Semantic Chunking: A Discriminative Framework for Ultra-Long Documents
> 原文: [https://arxiv.org/abs/2602.23370](https://arxiv.org/abs/2602.23370)

arXiv:2602.23370v1 Announce Type: new
Abstract: Long-document topic segmentation plays an important role in information retrieval and document understanding, yet existing methods still show clear shortcomings in ultra-long text settings. Traditional discriminative models are constrained by fixed windows and cannot model document-level semantics; generative large language models can output paragraph boundaries, but inference is expensive and long inputs are difficult to support. To address these issues, we propose a discriminative segmentation model based on Qwen3-0.6B. On top of the backbone network, we add a cross-window context fusion layer and a boundary classification head, and combine them with an overlapping sliding-window strategy. Our model supports single-pass inputs of up to 13k tokens and can be extended to ultra-long documents for paragraph boundary detection. To further enhance downstream retrieval efficiency, we derive a vector fusion method with scalar correction, which compresses the representation of ultra-long segments into a single vector without semantic loss. Experiments on the Wikipedia long-document topic segmentation dataset WIKI-727K show that, compared with three generative models based on Qwen2-0.5B released by Jina, our method achieves a better macro-averaged F1 and delivers two orders of magnitude faster inference, substantially improving the practicality and scalability of long-document processing.
