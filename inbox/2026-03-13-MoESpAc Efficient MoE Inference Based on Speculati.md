---
interest: medium
link: https://arxiv.org/abs/2603.09983
next_step: skim
priority: high
slack_ts: '1773974636.070129'
source: cs.LG - Machine Learning
status: unread
title: 'MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility
  in Heterogeneous Edge Scenarios'
---
# MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios
> 原文: [https://arxiv.org/abs/2603.09983](https://arxiv.org/abs/2603.09983)

arXiv:2603.09983v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) models enable scalable performance but face severe memory constraints on edge devices. Existing offloading strategies struggle with I/O bottlenecks due to the dynamic, low-information nature of autoregressive expert activation. In this paper, we propose to repurpose Speculative Decoding (SD) not merely as a compute accelerator, but as an informative lookahead sensor for memory management, supported by our theoretical and empirical analyses. Hence, we introduce MoE-SpAc, an MoE inference framework that integrates a Speculative Utility Estimator to track expert demand, a Heterogeneous Workload Balancer to dynamically partition computation via online integer optimization, and an Asynchronous Execution Engine to unify the prefetching and eviction in the same utility space. Extensive experiments on seven benchmarks demonstrate that MoE-SpAc achieves a 42% improvement in TPS over the SOTA SD-based baseline, and an average 4.04x speedup over all standard baselines. Code is available at https://github.com/lshAlgorithm/MoE-SpAc .
