---
interest: medium
link: https://arxiv.org/abs/2606.03026
next_step: skim
priority: low
slack_ts: '1780633550.868489'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity
  CPUs
---
# Spike-Aware C++ INT8 Inference for Sparse Spiking Language Models on Commodity CPUs
> 原文: [https://arxiv.org/abs/2606.03026](https://arxiv.org/abs/2606.03026)

arXiv:2606.03026v1 Announce Type: new
Abstract: Spiking language models expose activation sparsity that dense Transformer runtimes do not directly exploit. This paper studies that property from a systems perspective. Building on the SymbolicLight V1 spike-gated language model family, we implement a C++ CPU inference runtime that treats sparse binary spike states as an execution primitive rather than only applying post-hoc weight compression. The runtime combines a manifest-driven weight loader, mixed row/column memory layout, AVX2/FMA kernels, per-channel symmetric INT8 quantization, and integer-domain accumulation for spike-conditioned sparse paths. On an AMD Ryzen 7 5800X, an early scalar FP32 baseline decodes at 9.5 tokens/s. Mixed-layout AVX2 FP32 raises this to 14.7 tokens/s, and AVX2 INT8 reaches 19.9 tokens/s on the same step-30k export while reducing the weight footprint from 3.49 GB to 1.06 GB. For the available 186k-step 874M-parameter INT8 export, the C++ runtime decodes at 22.63 tokens/s in a single-thread CPU benchmark, compared with 16.31 tokens/s for TinyLlama-1.1B Q8\_0, 11.26 tokens/s for Falcon3-1B Q8\_0, and 9.70 tokens/s for Qwen2.5-1.5B Q8\_0 under llama.cpp. Thread scaling reaches 47.90 tokens/s at four CPU threads, and 512-token prefill improves from 29.86 to 94.68 tokens/s from one to eight threads. The throughput result comes with a quality cost: the SNN reports WikiText-2 perplexity 24.80, worse than the dense baselines in the same benchmark. We frame the result as an inference-systems study for sparse language runtimes, with longer-term motivation in embodied and edge agents that may benefit from local, low-core inference near sensors and actuators. Spike-aware execution can improve CPU throughput and memory behavior for sparse spiking language models, while model quality, controlled dense training baselines, embodied-task evaluation, and measured CPU energy remain open problems.
