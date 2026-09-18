---
interest: medium
link: https://arxiv.org/abs/2609.17564
next_step: skim
priority: high
slack_ts: '1789705158.470339'
source: cs.LG - Machine Learning
status: unread
title: 'Beyond Static RAG: An Adaptive, Tri-Metric Routing Framework for Efficient
  Long-Context Inference on Commodity GPUs'
---
# Beyond Static RAG: An Adaptive, Tri-Metric Routing Framework for Efficient Long-Context Inference on Commodity GPUs
> 原文: [https://arxiv.org/abs/2609.17564](https://arxiv.org/abs/2609.17564)

arXiv:2609.17564v1 Announce Type: new
Abstract: Deploying retrieval-augmented generation (RAG) on commodity GPUs such as the NVIDIA T4 (16 GB VRAM) exposes a practical failure mode we call the Compression Paradox: neural prompt compression can add key-value (KV) cache contention and preprocessing latency that outweigh generation-time savings, while skipping compression can cause out-of-memory (OOM) failures on long contexts. We identify two distinct failure mechanisms when a vLLM-served LLM and a PyTorch-based compressor are co-deployed under tight memory budgets, and introduce the Tri-Metric Router, a deterministic, training-free policy that selects among Raw, Neural (LLMLingua-2), and Lexical (BM25) pipelines. The router uses three CPU-side signals: spatial complexity ($L$), syntactic density ($\rho\_{key}$), and type-token ratio (TTR). Unlike prior semantic-only adaptation, our dispatch signal is hardware-physical, based on VRAM headroom and a latency crossover point. Thresholds are calibrated from profiling on LongBench qasper, yielding an operating crossover near 4,332 words on T4; our contribution is this calibration methodology rather than a hardware-specific constant. On out-of-distribution holdouts, the method achieves 0% OOM failures, 88.5 $\pm$ 4.4% oracle alignment, and 49.3% Combined F1, improving over always-on lexical compression by 5.2 points without additional VRAM or training cost.
