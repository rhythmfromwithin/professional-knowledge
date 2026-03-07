---
title: "CTRL-RAG: Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.04406
priority: high
status: unread
---
# CTRL-RAG: Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models
> 原文: [https://arxiv.org/abs/2603.04406](https://arxiv.org/abs/2603.04406)

arXiv:2603.04406v1 Announce Type: new
Abstract: With the growing use of Retrieval-Augmented Generation (RAG), training large language models (LLMs) for context-sensitive reasoning and faithfulness is increasingly important. Existing RAG-oriented reinforcement learning (RL) methods rely on external rewards that often fail to evaluate document faithfulness, and may misjudge similar answers in open-domain settings. In addition, there is no RAG-based selfreward mechanism. Moreover, although such a mechanism could in principle estimate answer confidence given documents, the absence of objective feedback in a self-judgment can cause hallucination accumulation and eventual model collapse. To tackle these issues, we propose a novel "internal-external" hybrid reward framework centered on a Contrastive Likelihood Reward (CLR). CLR directly optimizes the log-likelihood gap between responses conditioned on prompts with and without supporting evidence. This encourages the model to extract relevant evidence and increases its confidence when grounded in a specific context. Experiments show that our method (used alone or combined with external correctness rewards) achieves strong performance on singlehop, multi-hop, vertical-domain, and faithfulness benchmarks. Our training code and models are coming soon.
