---
title: "HALO: Hybrid Adaptive Latent Reasoning for Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.08775
priority: high
status: unread
interest: medium
next_step: skim
---
# HALO: Hybrid Adaptive Latent Reasoning for Language Models
> 原文: [https://arxiv.org/abs/2607.08775](https://arxiv.org/abs/2607.08775)

arXiv:2607.08775v1 Announce Type: new
Abstract: We study how to improve a frozen pretrained language model with a small amount of adaptive extra computation. A simple approach is to add additional refinement steps on top of the backbone hidden states, but fixed extra refinement can be wasteful: a one-step refinement head may be too weak, while forcing a second full-sequence refinement step everywhere can increase compute without improving transfer. We introduce HALO, a hybrid adaptive latent-refinement method that combines a coarse refinement stage with selective second-stage latent refinement on a subset of tokens chosen by token scoring and monotonic token halting. On the main public benchmark comparison built from MMLU-Pro and GPQA-Diamond, HALO achieves the best overall average among the paper-facing methods, outperforming the frozen backbone, fixed-1, and fixed-2. Internal analysis further shows that HALO reaches nearly the same token-accuracy level as fixed-2 while using fewer average applied refine steps than fixed-1 and far fewer than fixed-2. These results suggest that the key advantage is not simply more refinement, but a better allocation of refinement: HALO achieves the strongest paper-facing result while also using less measured controller compute than either fixed baseline.
