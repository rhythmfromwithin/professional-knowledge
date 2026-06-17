---
interest: medium
link: https://arxiv.org/abs/2606.17058
next_step: skim
priority: medium
slack_ts: '1781672190.230119'
source: cs.DC - Distributed Computing
status: unread
title: Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures
---
# Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures
> 原文: [https://arxiv.org/abs/2606.17058](https://arxiv.org/abs/2606.17058)

arXiv:2606.17058v1 Announce Type: new
Abstract: Large language model (LLM) coding agents are increasingly applied to code translation and optimization, yet their effectiveness in performance-critical high-performance computing (HPC) settings remains poorly characterized. This paper evaluates LLM-based coding workflows on SZ-family error-bounded lossy compression kernels, which combine numerical constraints with memory-intensive and control-flow-heavy implementations. We study two representative CUDA workloads (SZp and SZx) and target two heterogeneous execution platforms: NVIDIA GPUs and Cerebras wafer-scale accelerators. Focusing on single-agent iterative generation, we analyze not only final throughput but also agent runtime behavior, including iteration patterns, sensitivity to prompt specification, and characteristic failure modes. Our results reveal a pronounced cross-architecture divergence. On GPUs, stronger models can achieve substantially higher throughput but exhibit increased sensitivity to prompt precision and optimization guidance, whereas on Cerebras the dominant challenge lies in producing runnable programs under a PE-centric spatial execution model. We further observe that LLM agents are more effective on modular kernels (SZx) than on tightly coupled bit-level pipelines (SZp), where structural dependencies hinder optimization progress. These findings suggest that evaluating LLM coding agents for HPC requires accounting for both performance outcomes and architecture-specific robustness, and that success on thread-based platforms does not directly transfer to spatial accelerators.
