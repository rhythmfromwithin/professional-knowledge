---
interest: medium
link: https://arxiv.org/abs/2609.19150
next_step: skim
priority: high
slack_ts: '1789878892.863089'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Sampling Reveals Style: Unsupervised, Training-Free Discovery of Prompt-Conditional
  Stylistic Axes in LLM Activations'
---
# Sampling Reveals Style: Unsupervised, Training-Free Discovery of Prompt-Conditional Stylistic Axes in LLM Activations
> 原文: [https://arxiv.org/abs/2609.19150](https://arxiv.org/abs/2609.19150)

arXiv:2609.19150v1 Announce Type: new
Abstract: Large language models (LLMs) encode rich stylistic structure in their hidden activations, but discovering which stylistic dimensions are salient for a given prompt typically requires supervised contrastive data. We present a training-free, prompt-conditional alternative: we repeatedly sample completions of a single prompt at elevated temperature, apply Principal Component Analysis (PCA) to the pooled hidden activations, and label the resulting axes automatically from the pole generations. We validate the discovered axes against 245 human-elicited stylistic annotations in a two-phase study. On our strongest model (Qwen-3.5-4B-Instruct), the top two axes match spontaneously requested human dimensions with 72.8% precision and 43.6% macro-recall, and 75.6% of validity ratings judge the axes' polar generations accurate to their labels, with 90.9% adjacent inter-annotator agreement. Discoverability is strongly model-dependent: both Qwen models and Llama-3.2-3B expose human-salient axes, while DeepSeek-7B-Chat drops to 35.3% precision, its leading components dominated by structural rather than stylistic variance. Simple PCA over a model's own decoding variance is thus an effective, low-cost probe of stylistic structure in LLM representations, one that also exposes sharp cross-model differences in how that structure is organized.
