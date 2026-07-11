---
interest: medium
link: https://arxiv.org/abs/2607.06601
next_step: skim
priority: high
slack_ts: '1783740355.339679'
source: cs.LG - Machine Learning
status: unread
title: 'TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and
  KV-Cache Allocation'
---
# TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation
> 原文: [https://arxiv.org/abs/2607.06601](https://arxiv.org/abs/2607.06601)

arXiv:2607.06601v1 Announce Type: new
Abstract: Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may also need high-precision caching regardless of which expert processes it. We introduce TriRoute, a single lightweight controller shared across all three axes that, for every token at every layer, emits a coordinated policy: (i) an attention mode (skip/local/full), (ii) a sparse set of FFN experts (with a null expert recovering MoD), and (iii) a KV-cache bit-width. The controller trains end-to-end via a heterogeneous relaxation (Gumbel-Softmax with straight-through estimation for categorical decisions and load-balanced top-k gating for experts) under a Lagrangian budget constraint that turns the average compute and memory cost into a controllable knob. We identify a cross-axis routing-collapse cascade in naive joint training, where collapse on one axis propagates to the others, and address it with per-axis normalization and a coupling-aware balancing loss. On decoder-only models from 160M to 1.3B parameters at compute-optimal token counts, TriRoute Pareto-dominates the best independent MoD+MoE+KV-quantization combination at matched inference FLOPs and memory, while better preserving tail-case robustness on rare entities, code, and arithmetic that pure perplexity optimization erodes. Post-hoc analysis reveals interpretable structure: the controller allocates full attention and high-precision cache to sentence-initial positions, rare subwords, and named entities, while cheaply routing function words.
