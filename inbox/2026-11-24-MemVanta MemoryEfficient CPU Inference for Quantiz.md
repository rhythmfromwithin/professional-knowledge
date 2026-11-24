---
title: "MemVanta: Memory-Efficient CPU Inference for Quantized GGUF Language Models"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.27997
priority: medium
status: unread
interest: medium
next_step: skim
---
# MemVanta: Memory-Efficient CPU Inference for Quantized GGUF Language Models
> 原文: [https://arxiv.org/abs/2611.27997](https://arxiv.org/abs/2611.27997)

arXiv:2611.27997v1 Announce Type: new
Abstract: Deploying large language models on commodity CPUs is often constrained not only by computational throughput but also by the resident memory required to execute quantized models within fixed system budgets. We present MemVanta, an experimental C++20 inference runtime for quantized GGUF language models that treats memory residency as a first-class systems objective. MemVanta combines memory-mapped model access, bounded tensor caching, quantized execution paths, paged key-value state, and explicit memory-pressure validation. We evaluate MemVanta against a pinned llama.cpp baseline using the same OpenLLaMA 7B v2 Q4\_0 GGUF under CPU-only execution. Across five measured runs following warm-up, MemVanta records a peak resident set size of 3,983,412 KiB compared with 7,586,960 KiB for llama.cpp, corresponding to a 47.50 percent reduction in peak RSS. This memory reduction involves a substantial throughput trade-off: MemVanta achieves 3.15 +/- 0.04 tokens/s for prompt processing and 1.52 +/- 0.02 tokens/s for token generation, compared with 45.82 +/- 0.96 and 7.76 +/- 0.09 tokens/s, respectively, for llama.cpp. In a separate Linux cgroup-v2 experiment with swap disabled, MemVanta completes execution at a tested 3584 MiB memory ceiling, while llama.cpp is OOM-killed at that ceiling and first succeeds at the tested 3840 MiB level. These results position MemVanta as a memory-efficiency research prototype rather than a throughput competitor. We analyze the architectural mechanisms underlying this trade-off and discuss reproducibility, correctness, limitations, and opportunities for memory-constrained CPU and edge inference.
