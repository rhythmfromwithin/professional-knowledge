---
title: "Domain Adaptation of Large Language Models for Polymer-Composite Additive Manufacturing Using Retrieval-Augmented Generation and Fine-Tuning"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.12516
priority: high
status: unread
interest: medium
next_step: skim
---
# Domain Adaptation of Large Language Models for Polymer-Composite Additive Manufacturing Using Retrieval-Augmented Generation and Fine-Tuning
> 原文: [https://arxiv.org/abs/2605.12516](https://arxiv.org/abs/2605.12516)

arXiv:2605.12516v1 Announce Type: new
Abstract: General-purpose large language models (LLMs) often struggle to generate reliable responses in specialized engineering domains due to limited domain grounding and insufficient exposure to structured technical knowledge. This study investigates practical strategies for adapting a foundation LLM to the additive manufacturing (AM) domain in order to improve answer accuracy, relevance, and usability for expert-level question answering. AM knowledge is distributed across heterogeneous sources such as academic literature, manufacturer documentation, technical standards, and procedural guides. Although general LLMs demonstrate strong linguistic capabilities, they frequently fail to retrieve and contextualize such domain-specific information. Two common approaches to address this limitation are domain-specific fine-tuning and retrieval-augmented generation (RAG). We construct a curated AM corpus and evaluate three configurations based on LLaMA-3-8B: (1) the pretrained baseline model, (2) a RAG system that retrieves relevant document chunks from a vector database, and (3) a model fine-tuned on raw domain text. Performance is evaluated using 200 expert-designed AM questions assessed by mechanical engineering experts for accuracy, relevance, and overall preference. Results show that the RAG model consistently outperforms the baseline. Among the 200 questions, 75.5% of RAG responses are judged more accurate, 85.2% are preferred overall, and 90.8% are rated more relevant than baseline responses. In contrast, fine-tuning on raw AM text reduces performance, producing more accurate answers in only 5.6% of cases and more relevant answers in 32.5% of cases. These results indicate that retrieval-augmented approaches provide a more effective pathway for adapting LLMs to specialized engineering domains than naive fine-tuning on unstructured technical data.
