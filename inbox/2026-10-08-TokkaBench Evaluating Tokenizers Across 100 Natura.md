---
title: "Tokka-Bench: Evaluating Tokenizers Across 100 Natural and 20 Programming Languages"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.08794
priority: high
status: unread
interest: medium
next_step: skim
---
# Tokka-Bench: Evaluating Tokenizers Across 100 Natural and 20 Programming Languages
> 原文: [https://arxiv.org/abs/2610.08794](https://arxiv.org/abs/2610.08794)

arXiv:2610.08794v1 Announce Type: new
Abstract: Large language models rely on subword tokenizers whose quality varies across languages, yet no standardized multi-metric framework exists for broad comparative evaluation. We introduce Tokka-Bench, an open-source framework that evaluates tokenizers on five complementary metrics -- bytes per token, unique token coverage, subword fertility, word-split rate, and vocabulary composition -- across 100 natural languages (30+ scripts) and 20 programming languages, using language-aware segmentation adapted to each writing system. Comparing seven BPE tokenizers (GPT-2, GPT-4, gpt-oss, Llama 3.1, Gemma 3, Qwen3, and Kimi K2) within individual languages, we find that vocabulary allocation strategy matters more than raw vocabulary size, and that programming-language efficiency has converged among recent tokenizers despite divergent natural-language profiles. The framework, data, and interactive dashboard are publicly available.
