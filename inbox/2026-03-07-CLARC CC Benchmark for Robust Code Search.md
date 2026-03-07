---
title: "CLARC: C/C++ Benchmark for Robust Code Search"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.04484
priority: low
status: unread
---
# CLARC: C/C++ Benchmark for Robust Code Search
> 原文: [https://arxiv.org/abs/2603.04484](https://arxiv.org/abs/2603.04484)

arXiv:2603.04484v1 Announce Type: new
Abstract: Efficient code retrieval is critical for developer productivity, yet existing benchmarks largely focus on Python and rarely stress-test robustness beyond superficial lexical cues. To address the gap, we introduce an automated pipeline for code search datasets and present CLARC, a C/C++ benchmark built from real-world GitHub repositories. CLARC contains 1,245 query-code pairs for evaluation and 5,472 pairs for training. The benchmark incorporates LLM-generated natural language queries validated through rigorous human scoring and hypothesis testing. To analyze contextual requirements effectively, our pipeline starts by ensuring code compilability. It then categorizes code snippets by dependency complexity, distinguishing whether the code relies on custom-defined types or helper functions. The pipeline also enables CLARC to stress-test retrieval robustness by introducing challenging settings, including identifier anonymization and compilation to low-level languages like Assembly and WebAssembly. Under these conditions, our evaluation of six state-of-the-art models reveals sharp drops in retrieval effectiveness. The experimental results highlight the models' persistent reliance on lexical features rather than code semantic understanding. Our dataset is publicly available at https://huggingface.co/datasets/ClarcTeam/CLARC.
