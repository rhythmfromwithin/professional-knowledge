---
title: "S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.10353
priority: medium
status: unread
interest: medium
next_step: skim
---
# S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance
> 原文: [https://arxiv.org/abs/2603.10353](https://arxiv.org/abs/2603.10353)

arXiv:2603.10353v1 Announce Type: new
Abstract: With the increasing volumes of Large Language Models (LLMs) and the expanding context lengths, attention computation has become a key performance bottleneck in LLM serving. For fast attention computation, recent practices often parallelize the attention heads on multiple GPUs, and also widely adopt attention sparsification to reduce the computation amount -- which selectively computes a subset of attention pairs under a preset sparsity budget. In this paper, we notice that attention heads of an LLM model often exhibit heterogeneous-yet-stable sparsity elasticities, which motivates us to enforce head-adaptive sparsity budgets to attain better efficiency while preserving high inference quality. Yet, from the system aspect, with heterogeneous sparsity levels, attention computation time on different heads would be inconsistent, yielding cross-GPU resource bubbles under head-parallel deployment. To further minimize such bubbles, we propose a novel attention deployment strategy called Sparsity-aware Head-Parallel Load Balance (S-HPLB). Experiments on long-context benchmark show that, S-HPLB can achieve a $2.88\times$ improvement in average attention computation latency without quality degradation.
