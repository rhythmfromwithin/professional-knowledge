---
interest: medium
link: https://arxiv.org/abs/2604.02371
next_step: skim
priority: medium
slack_ts: '1775531929.441359'
source: cs.CV - Computer Vision
status: unread
title: Internalized Reasoning for Long-Context Visual Document Understanding
---
# Internalized Reasoning for Long-Context Visual Document Understanding
> 原文: [https://arxiv.org/abs/2604.02371](https://arxiv.org/abs/2604.02371)

arXiv:2604.02371v1 Announce Type: new
Abstract: Visual long-document understanding is critical for enterprise, legal, and scientific applications, yet the best performing open recipes have not explored reasoning, a capability which has driven leaps in math and code performance. We introduce a synthetic data pipeline for reasoning in long-document understanding that generates thinking traces by scoring each page for question relevance, extracting textual evidence and ordering it from most to least relevant. We apply SFT to the resulting traces within \texttt{} tags, gated by a \texttt{} control token, and the resulting reasoning capability is internalized via low-strength model merging. We study Qwen3 VL 32B and Mistral Small 3.1 24B. With Qwen3 VL, we achieve 58.3 on MMLongBenchDoc, surpassing the 7$\times$ larger Qwen3 VL 235B A22B (57.0). With Mistral, we show that synthetic reasoning outperforms distillation from the Thinking version's traces by 3.8 points on MMLBD-C, and internalized reasoning exhibits 12.4$\times$ fewer mean output tokens compared to explicit reasoning. We release our pipeline for reproducibility and further exploration.
