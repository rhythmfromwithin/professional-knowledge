---
title: "The Cost of Context: Profiling the Energy Footprint of Input Tokens in Large Language Models"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.19819
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Cost of Context: Profiling the Energy Footprint of Input Tokens in Large Language Models
> 原文: [https://arxiv.org/abs/2610.19819](https://arxiv.org/abs/2610.19819)

arXiv:2610.19819v1 Announce Type: new
Abstract: The rapid adoption of Retrieval-Augmented Generation (RAG) and long-context LLMs has shifted the computational burden toward the prefill phase---the initial stage where the model processes all input tokens in parallel before generating a response---yet its energy impact remains poorly characterised. We investigate the contradiction between massive hardware-level power spikes and the sub-linear marginal cost of input tokens reported in system-level studies. Through high-resolution telemetry of Llama-3.1 and Qwen-2 models on NVIDIA A100 hardware, we identify the efficiency threshold where $O(n^2)$ attention complexity overcomes GPU parallelisation. Our results quantify how optimised memory orchestration (PagedAttention) delays this scaling bottleneck across three orders of context scaling, yielding up to an 8.9$\times$ energy efficiency advantage at 112,000 tokens compared to standard baselines. Furthermore, we characterise the energy disparity between input and output tokens, demonstrating that optimised serving (vLLM) causes this ratio to narrow (from $\approx$850$\times$ to 750$\times$) as context scales due to high decode efficiency, whereas unoptimised baselines show a much smaller, roughly constant gap ($\approx$150--230$\times$) because their prefill is itself expensive. This work establishes context-scaling laws that differentiate engine-level optimisations from inherent model constraints, providing an empirical framework for sustainable LLM deployment.
