---
interest: medium
link: https://arxiv.org/abs/2604.09625
next_step: skim
priority: high
slack_ts: '1776310487.650379'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale
  Data and Ensemble LLM Annotations
---
# Toward Generalized Cross-Lingual Hateful Language Detection with Web-Scale Data and Ensemble LLM Annotations
> 原文: [https://arxiv.org/abs/2604.09625](https://arxiv.org/abs/2604.09625)

arXiv:2604.09625v1 Announce Type: new
Abstract: We study whether large-scale unlabelled web data and LLM-based synthetic annotations can improve multilingual hate speech detection. Starting from texts crawled via OpenWebSearch.eu~(OWS) in four languages (English, German, Spanish, Vietnamese), we pursue two complementary strategies. First, we apply continued pre-training to BERT models by continuing masked language modelling on unlabelled OWS texts before supervised fine-tuning, and show that this yields an average macro-F1 gain of approximately 3% over standard baselines across sixteen benchmarks, with stronger gains in low-resource settings. Second, we use four open-source LLMs (Mistral-7B, Llama3.1-8B, Gemma2-9B, Qwen2.5-14B) to produce synthetic annotations through three ensemble strategies: mean averaging, majority voting, and a LightGBM meta-learner. The LightGBM ensemble consistently outperforms the other strategies. Fine-tuning on these synthetic labels substantially benefits a small model (Llama3.2-1B: +11% pooled F1), but provides only a modest gain for the larger Qwen2.5-14B (+0.6%). Our results indicate that the combination of web-scale unlabelled data and LLM-ensemble annotations is the most valuable for smaller models and low-resource languages.
