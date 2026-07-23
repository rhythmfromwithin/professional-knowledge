---
title: "Convolution for Large Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.18413
priority: high
status: unread
interest: medium
next_step: skim
---
# Convolution for Large Language Models
> 原文: [https://arxiv.org/abs/2607.18413](https://arxiv.org/abs/2607.18413)

arXiv:2607.18413v1 Announce Type: new
Abstract: Large language models (LLMs) largely rely on Transformers, where self-attention provides global token interaction but does not explicitly encode the locality of natural language. We study whether lightweight depthwise convolutions can supply this local inductive bias without materially increasing model size. Our macro-level ablation compares convolution at 17 locations in a Qwen3 Transformer block and finds the best results when convolution is applied to the projected queries, keys, and values before attention. A subsequent micro-level study favors a residual depthwise convolution with kernel size $k=3$, without additional normalization or activation. Across Qwen3 models and several pre-training data budgets, this design improves the average accuracy on seven downstream benchmarks while adding less than $0.01\%$ parameters. A representation-level case study further suggests that the convolution makes repeated token IDs more sensitive to their immediate context. These results support depthwise convolution as a lightweight complement to self-attention for modeling short-range token interactions.
