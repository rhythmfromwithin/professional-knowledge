---
interest: medium
link: https://arxiv.org/abs/2609.13154
next_step: skim
priority: high
slack_ts: '1789532917.034289'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic
  Pipeline with Empirical Pareto Analysis Across Eleven Task Categories'
---
# Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic Pipeline with Empirical Pareto Analysis Across Eleven Task Categories
> 原文: [https://arxiv.org/abs/2609.13154](https://arxiv.org/abs/2609.13154)

arXiv:2609.13154v1 Announce Type: new
Abstract: Recent advances in large language models (LLMs) have made prompts increasingly large and complex. Techniques such as chain-of-thought reasoning (Wei et al., 2022) and in-context learning (Brown et al., 2020) frequently push real-world prompts past several thousand tokens, increasing inference cost and latency. Learned compression methods such as LLMLingua (Jiang et al., 2023) and Selective Context (Li et al., 2023) achieve high compression ratios but require auxiliary language models and are non-deterministic. We ask a complementary question: how far can a training-free, fully deterministic, CPU-only pipeline based on classical lexical NLP be pushed before output quality degrades significantly? Eleven toggleable lexical transformations - stopword removal, filler-phrase deletion, contraction and abbreviation substitution, part-of-speech-based pruning, lemmatization, WordNet-driven synonym shortening, and named-entity preservation - are assembled into a configurable pipeline. Fifteen configurations are evaluated on 1,242 English-only prompts from six sources (Dolly-15k, LMSYS-Chat-1M, WildChat-1M, MMLU, GSM8K, HellaSwag), spanning eleven automatically derived task categories, yielding 18,630 paired GPT-4o-mini completions. Output preservation is measured using BLEU, ROUGE-1/2/L, BERTScore-F1, and SentenceBERT cosine similarity. The most aggressive configuration achieves a mean token reduction of 40.3% (sigma = 9.2) at a BERTScore-F1 of 0.876 against the original-prompt output; a stopword-only configuration achieves 29.6% reduction at 0.913. The compression-versus-fidelity Pareto frontier is characterized per task category, with commonsense reasoning a systematic failure mode under aggressive compression. All code, prompts, and per-cell results are released for reproducibility.
