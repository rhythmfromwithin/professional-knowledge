---
title: "NeuroFlex: Lossless Element-Level ANN-SNN Co-Execution for Efficient Sparse Inference"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2511.05215
priority: low
status: unread
interest: medium
next_step: skim
---
# NeuroFlex: Lossless Element-Level ANN-SNN Co-Execution for Efficient Sparse Inference
> 原文: [https://arxiv.org/abs/2511.05215](https://arxiv.org/abs/2511.05215)

arXiv:2511.05215v2 Announce Type: replace
Abstract: Sparse DNN accelerators specialize in ANN or SNN execution, leaving energy or latency on the table when workload characteristics vary within a layer. Hybrid accelerator designs that switch modes at layer or tile granularity suffer from low PE utilization since one core type idles whenever the other is active. NeuroFlex is the first accelerator to assign every output element independently to ANN or SNN execution mode with zero accuracy loss. We extend integer-exact ANN-SNN equivalence from layers to individual output elements, thereby enabling mode switching with no conversion error. An offline cost-guided scheduler scores each element by its marginal energy-delay trade-off and packs work across PEs, achieving 97-99% PE utilization compared to 40-45% for layer-wise hybrids. NeuroFlex reduces EDP by 57-67% over a strong ANN-only baseline and delivers up to 2.5x speedup over a dual-sparse SNN-only baseline. Our cost-guided scheduler improves throughput by 16-19% over random element assignment across vision, language, and transformer workloads.
