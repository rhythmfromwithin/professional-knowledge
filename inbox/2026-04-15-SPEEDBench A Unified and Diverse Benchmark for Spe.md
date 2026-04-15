---
title: "SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.09557
priority: medium
status: unread
interest: medium
next_step: skim
---
# SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding
> 原文: [https://arxiv.org/abs/2604.09557](https://arxiv.org/abs/2604.09557)

arXiv:2604.09557v1 Announce Type: new
Abstract: Speculative Decoding (SD) has emerged as a critical technique for accelerating Large Language Model (LLM) inference. Unlike deterministic system optimizations, SD performance is inherently data-dependent, meaning that diverse and representative workloads are essential for accurately measuring its effectiveness. Existing benchmarks suffer from limited task diversity, inadequate support for throughput-oriented evaluation, and a reliance on high-level implementations that fail to reflect production environments. To address this, we introduce SPEED-Bench, a comprehensive suite designed to standardize SD evaluation across diverse semantic domains and realistic serving regimes. SPEED-Bench offers a carefully curated Qualitative data split, selected by prioritizing semantic diversity across the data samples. Additionally, it includes a Throughput data split, allowing speedup evaluation across a range of concurrencies, from latency-sensitive low-batch settings to throughput-oriented high-load scenarios. By integrating with production engines like vLLM and TensorRT-LLM, SPEED-Bench allows practitioners to analyze system behaviors often masked by other benchmarks. We highlight this by quantifying how synthetic inputs overestimate real-world throughput, identifying batch-size dependent optimal draft lengths and biases in low-diversity data, and analyzing the caveats of vocabulary pruning in state-of-the-art drafters. We release SPEED-Bench to establish a unified evaluation standard for practical comparisons of SD algorithms.
