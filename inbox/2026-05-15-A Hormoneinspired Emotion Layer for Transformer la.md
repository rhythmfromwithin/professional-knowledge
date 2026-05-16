---
interest: medium
link: https://arxiv.org/abs/2605.13858
next_step: skim
priority: low
slack_ts: '1778903334.640139'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: A Hormone-inspired Emotion Layer for Transformer language models (HELT)
---
# A Hormone-inspired Emotion Layer for Transformer language models (HELT)
> 原文: [https://arxiv.org/abs/2605.13858](https://arxiv.org/abs/2605.13858)

arXiv:2605.13858v1 Announce Type: new
Abstract: Large Language Models have demonstrated remarkable capabilities in generating contextually relevant and grammatically correct text. However, they fundamentally lack the ability to process and respond to emotional context in a manner analogous to human emotional cognition. Current approaches to emotion modeling in NLP systems rely primarily on discrete emotion classification or simplistic sentiment analysis, which fail to capture the continuous, multi-dimensional nature of human emotional states. In this paper, we introduce HormoneT5, a novel architecture that augments transformer language models with a biologically-inspired Hormone Emotion Block that simulates the human endocrine system's role in emotional processing. Our approach computes six continuous hormone-like values through specialized per-hormone attention heads, each with orthogonally initialized learnable queries, temperature-scaled attention mechanisms, and deep output projections. These hormone values are then transformed into an emotional embedding that modulates the encoder hidden states, enabling emotionally-appropriate response generation. We propose a multi-objective training framework combining sequence-to-sequence loss, hormone prediction loss with margin penalties, and diversity regularization to prevent attention collapse. Experimental results on our curated emotion-labeled dataset demonstrate that HormoneT5 achieves 85%+ per-hormone accuracy within a 0.15 tolerance threshold, with hormone differentiation ranges exceeding 0.85 across all six hormones between contrasting emotional tones. Human evaluation studies show significant preference (p < 0.01) for HormoneT5-generated responses in terms of emotional appropriateness and empathetic quality compared to baseline T5 outputs. Our work opens new directions for biologically-grounded affective computing and emotionally intelligent conversational agents.
