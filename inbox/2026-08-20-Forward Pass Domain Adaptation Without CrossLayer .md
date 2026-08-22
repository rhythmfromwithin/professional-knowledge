---
interest: medium
link: https://arxiv.org/abs/2608.14563
next_step: skim
priority: high
slack_ts: '1787362727.865439'
source: cs.LG - Machine Learning
status: unread
title: Forward Pass Domain Adaptation (Without Cross-Layer Backpropagation)
---
# Forward Pass Domain Adaptation (Without Cross-Layer Backpropagation)
> 原文: [https://arxiv.org/abs/2608.14563](https://arxiv.org/abs/2608.14563)

arXiv:2608.14563v1 Announce Type: new
Abstract: Forward-Pass-Only MLP training (FPO) adapts large language models without a backward pass through the model body, achieving 2.7--3.2x the throughput of standard fine-tuning at ~40% less peak training memory, while leaving off-domain benchmarks within seed-noise of baseline, a property that full-network fine-tuning does not reliably reproduce. FPO rests on a single empirical observation: at late layers of a transformer, the output-layer prediction error approximates the true gradient with cosine similarity 0.47--0.59 across six public models we survey. We introduce a two-minute diagnostic that quantifies this approximation per layer for any model, identifying where late-layer adaptation is viable. Informed by the diagnostic, FPO computes a single error signal at the output and applies it to each target layer. No signal is propagated between layers, and no autograd graph is constructed at any point. We evaluate FPO on three model families (OLMo-2-7B, Qwen3-8B, Falcon3-7B). Across all three, FPO produces in-domain perplexity improvement and leaves MMLU, ARC-Challenge, HellaSwag, and Winogrande within seed-noise of baseline. Localizing SFT to FPO's target layers to enter this regime is also feasible, but at 2.2x the wall-clock cost of FPO.
