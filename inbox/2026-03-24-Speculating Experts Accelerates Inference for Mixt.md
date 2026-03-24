---
title: "Speculating Experts Accelerates Inference for Mixture-of-Experts"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.19289
priority: high
status: unread
interest: medium
next_step: skim
---
# Speculating Experts Accelerates Inference for Mixture-of-Experts
> 原文: [https://arxiv.org/abs/2603.19289](https://arxiv.org/abs/2603.19289)

arXiv:2603.19289v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) models have gained popularity as a means of scaling the capacity of large language models (LLMs) while maintaining sparse activations and reduced per-token compute. However, in memory-constrained inference settings, expert weights must be offloaded to CPU, creating a performance bottleneck from CPU-GPU transfers during decoding. We propose an expert prefetching scheme that leverages currently computed internal model representations to speculate future experts, enabling memory transfers to overlap with computation. Across multiple MoE architectures, we demonstrate that future experts can be reliably predicted by these internal representations. We also demonstrate that executing speculated experts generally maintains downstream task accuracy, thus preserving more effective compute-memory overlap by eliminating the need to re-fetch true router-selected experts. Integrated into an optimized inference engine, our approach achieves up to 14\% reduction in time per output token (TPOT) over on-demand loading of experts from CPU memory. For MoEs where speculative execution alone yields suboptimal accuracy, we further examine lightweight estimators that improve expert prediction hit rates, thereby reducing performance degradation. Our code is released in open-source at https://github.com/axonn-ai/yalis/tree/offload\_prefetch.
