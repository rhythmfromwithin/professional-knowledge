---
interest: medium
link: https://arxiv.org/abs/2605.20706
next_step: skim
priority: medium
slack_ts: '1779508586.126799'
source: cs.DC - Distributed Computing
status: unread
title: 'Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision
  LLM Inference with WebGPU'
---
# Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU
> 原文: [https://arxiv.org/abs/2605.20706](https://arxiv.org/abs/2605.20706)

arXiv:2605.20706v1 Announce Type: new
Abstract: Running language models in the browser presents a unique opportunity to build efficient, private, and portable AI applications, but requires contending with constrained memory availability and heterogeneous hardware targets. To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama.cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser. Our design significantly reduces memory overhead through static memory planning and efficient model loading, addresses cross-device variability through a tunable kernel library, and introduces templated GPU kernels that support performant implementations of numerous quantization formats, enabling broad model support and extensibility to new formats.
We evaluate LlamaWeb on 16 devices from 8 vendors, collecting data from 10 language models and four model weight formats. We compare LlamaWeb against existing browser-based LLM frameworks and find that LlamaWeb requires 29-33% less memory across several combinations of device, browser, and operating system. We also evaluate LlamaWeb's performance against these frameworks and find that it increases decode throughput by 45-69% across four GPUs from separate vendors. In addition, we compare LlamaWeb's performance against other llama.cpp backends, where it is competitive with and even beats vendor-specific backend performance on some devices.
