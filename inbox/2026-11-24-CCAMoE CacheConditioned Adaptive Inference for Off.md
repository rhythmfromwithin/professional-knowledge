---
interest: medium
link: https://arxiv.org/abs/2611.28550
next_step: skim
priority: medium
slack_ts: '1795512716.736309'
source: cs.DC - Distributed Computing
status: unread
title: 'CCAMoE: Cache-Conditioned Adaptive Inference for Offloaded MoE'
---
# CCAMoE: Cache-Conditioned Adaptive Inference for Offloaded MoE
> 原文: [https://arxiv.org/abs/2611.28550](https://arxiv.org/abs/2611.28550)

arXiv:2611.28550v1 Announce Type: new
Abstract: Expert offloading enables Mixture-of-Experts (MoE) inference on memory-constrained GPUs, but expert transfers and CPU execution limit decoding performance. Speculative decoding can mitigate these costs, yet separate draft weights consume scarce GPU memory and longer drafts increase verification demand. In this paper, we present CCAMoE, a unified runtime that coordinates adaptive speculative decoding with concurrent expert-cache updates. Its design has three key features: 1) Cache-only drafting, which reuses resident target experts to generate proposals and routing hints without separate draft weights; 2) Draft-guided cache updates, which anticipate expert demand and overlap transfers with computation to support subsequent drafting and verification; and 3) Cost-aware draft-length control, which balances expected acceptance against execution cost. Together, these mechanisms coordinate proposal generation and cache preparation through a shared evolving cache, improving proposal quality while reducing verification cost. Across various MoE models, GPU platforms, and workloads, CCAMoE consistently achieves the lowest decoding latency, with up to 2.33$\times$ speedup over state-of-the-art baselines.
