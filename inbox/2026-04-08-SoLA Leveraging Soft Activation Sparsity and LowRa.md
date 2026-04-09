---
interest: medium
link: https://arxiv.org/abs/2604.03258
next_step: skim
priority: high
slack_ts: '1775703386.515639'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large
  Language Model Compression'
---
# SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression
> 原文: [https://arxiv.org/abs/2604.03258](https://arxiv.org/abs/2604.03258)

arXiv:2604.03258v1 Announce Type: new
Abstract: Large language models (LLMs) have demonstrated impressive capabilities across various tasks, but the billion-scale parameters pose deployment challenges. Although existing methods attempt to reduce the scale of LLMs, they require either special hardware support or expensive post-training to maintain model quality. To facilitate efficient and affordable model slimming, we propose a novel training-free compression method for LLMs, named "SoLA", which leverages \textbf{So}ft activation sparsity and \textbf{L}ow-r\textbf{A}nk decomposition. SoLA can identify and retain a minority of components significantly contributing to inference, while compressing the majority through low-rank decomposition, based on our analysis of the activation pattern in the feed-forward network (FFN) of modern LLMs. To alleviate the decomposition loss, SoLA is equipped with an adaptive component-wise low-rank allocation strategy to assign appropriate truncation positions for different weight matrices. We conduct extensive experiments on LLaMA-2-7B/13B/70B and Mistral-7B models across a variety of benchmarks. SoLA exhibits remarkable improvement in both language modeling and downstream task accuracy without post-training. For example, with a 30\% compression rate on the LLaMA-2-70B model, SoLA surpasses the state-of-the-art method by reducing perplexity from 6.95 to 4.44 and enhancing downstream task accuracy by 10\%.
