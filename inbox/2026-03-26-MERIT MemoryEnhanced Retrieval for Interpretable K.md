---
title: "MERIT: Memory-Enhanced Retrieval for Interpretable Knowledge Tracing"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.22289
priority: high
status: unread
interest: medium
next_step: skim
---
# MERIT: Memory-Enhanced Retrieval for Interpretable Knowledge Tracing
> 原文: [https://arxiv.org/abs/2603.22289](https://arxiv.org/abs/2603.22289)

arXiv:2603.22289v1 Announce Type: new
Abstract: Knowledge Tracing (KT) models students' evolving knowledge states to predict future performance, serving as a foundation for personalized education. While traditional deep learning models achieve high accuracy, they often lack interpretability. Large Language Models (LLMs) offer strong reasoning capabilities but struggle with limited context windows and hallucinations. Furthermore, existing LLM-based methods typically require expensive fine-tuning, limiting scalability and adaptability to new data. We propose MERIT (Memory-Enhanced Retrieval for Interpretable Knowledge Tracing), a training-free framework combining frozen LLM reasoning with structured pedagogical memory. Rather than updating parameters, MERIT transforms raw interaction logs into an interpretable memory bank. The framework uses semantic denoising to categorize students into latent cognitive schemas and constructs a paradigm bank where representative error patterns are analyzed offline to generate explicit Chain-of-Thought (CoT) rationales. During inference, a hierarchical routing mechanism retrieves relevant contexts, while a logic-augmented module applies semantic constraints to calibrate predictions. By grounding the LLM in interpretable memory, MERIT achieves state-of-the-art performance on real-world datasets without gradient updates. This approach reduces computational costs and supports dynamic knowledge updates, improving the accessibility and transparency of educational diagnosis.
