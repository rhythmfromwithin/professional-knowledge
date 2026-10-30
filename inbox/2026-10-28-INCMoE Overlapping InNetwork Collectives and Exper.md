---
interest: medium
link: https://arxiv.org/abs/2610.36339
next_step: skim
priority: medium
slack_ts: '1793337888.660199'
source: cs.DC - Distributed Computing
status: unread
title: 'INC-MoE: Overlapping In-Network Collectives and Expert Computation for Expert-Parallel
  Mixture-of-Experts Inference'
---
# INC-MoE: Overlapping In-Network Collectives and Expert Computation for Expert-Parallel Mixture-of-Experts Inference
> 原文: [https://arxiv.org/abs/2610.36339](https://arxiv.org/abs/2610.36339)

arXiv:2610.36339v1 Announce Type: new
Abstract: In expert-parallel mixture-of-experts (MoE) serving, dispatch moves tokens to the accelerators hosting their selected experts, and combine returns expert outputs to each token's owner. Both operations lie on the critical path and can dominate MoE layer latency in multi-node deployments. We present INC-MoE, an expert-parallel MoE layer that offloads dispatch and combine to the network switch and overlaps both collectives with each other and with expert computation. Dispatch uses in-network AllGather through switch-side multicast, while combine uses in-network ReduceScatter through switch-side reduction. Both collectives use message semantics between the end hosts and the switch. Because the in-network collectives load opposite directions of each link, executing them concurrently reduces bandwidth-bound communication time by $(N-2)/(2(N-1))$ relative to concurrent ring-based collectives: 33% for four ranks and 43% for eight.
INC-MoE partitions tokens into bands and processes them through a three-stage AllGather-feed-forward network (FFN)-ReduceScatter pipeline inside a single persistent kernel. At steady state, role-specialized thread blocks gather the next band, compute the current band, and reduce the previous band concurrently, overlapping both collectives with each other and with computation using device-side synchronization. INC-MoE integrates as a drop-in replacement for the MoE layer of vLLM. We evaluate it in an emulated four-node scale-out deployment with a dedicated accelerator emulating an in-network computing (INC) switch. On OLMoE prefill with four-way expert parallelism, INC-MoE reduces time to first token (TTFT) by up to 33% and increases throughput by up to 50% relative to vLLM's default collective path, while matching its outputs.
