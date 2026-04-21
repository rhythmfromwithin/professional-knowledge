---
interest: medium
link: https://arxiv.org/abs/2604.15351
next_step: skim
priority: high
slack_ts: '1776742299.413279'
source: cs.LG - Machine Learning
status: unread
title: 'Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning Across
  Architectures'
---
# Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning Across Architectures
> 原文: [https://arxiv.org/abs/2604.15351](https://arxiv.org/abs/2604.15351)

arXiv:2604.15351v1 Announce Type: new
Abstract: Low-Rank Adaptation (LoRA) has become the dominant parameter-efficient fine-tuning method for large language models, yet standard practice applies LoRA adapters uniformly to all transformer layers regardless of their relevance to the downstream task. We introduce Aletheia, a gradient-guided layer selection method that identifies the most task-relevant layers via a lightweight gradient probe and applies LoRA adapters only to those layers with asymmetric rank allocation. Across 81 experiment rows covering 14 successful models from 8 architecture families (0.5B-72B parameters, including dense and Mixture-of-Experts architectures), with one additional documented failed Pythia/GPT-NeoX attempt in Campaign 2, Aletheia achieves a 15-28% training speedup (mean 23.1%, p < 0.001) with bounded extra forgetting and broadly matched downstream behavior on the evaluated MMLU, GSM8K, and HumanEval benchmark pack. Across the tested families and scales, Campaign 1 shows a 100% per-model speed win rate and Campaign 2 shows broadly preserved downstream behavior within a bounded-degradation framing. Together these results support a practical model-economics claim: intelligent layer selection can make LoRA fine-tuning materially more efficient without introducing major downstream damage on the evaluated set.
