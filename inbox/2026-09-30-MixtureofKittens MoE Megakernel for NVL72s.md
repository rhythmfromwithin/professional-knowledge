---
interest: medium
link: https://arxiv.org/abs/2609.36070
next_step: skim
priority: medium
slack_ts: '1790918084.432409'
source: cs.DC - Distributed Computing
status: unread
title: 'Mixture-of-Kittens: MoE Megakernel for NVL72s'
---
# Mixture-of-Kittens: MoE Megakernel for NVL72s
> 原文: [https://arxiv.org/abs/2609.36070](https://arxiv.org/abs/2609.36070)

arXiv:2609.36070v1 Announce Type: new
Abstract: AI accelerator systems are rapidly consolidating into scale-up architectures, where tens to thousands of GPUs communicate over high-bandwidth, single-hop fabrics. We find that existing Mixture-of-Experts (MoE) training systems, optimized for conventional scale-out networks, transfer poorly to this setting, often running slower than a naive baseline built with PyTorch and NCCL. With industry roadmaps pointing toward even larger scale-up domains, understanding the performance tradeoffs of this hardware regime is increasingly important. We present Mixture-of-Kittens (MoK), an MoE training system designed for Nvidia NVL72. MoK builds on three insights that unlock performance on scale-up domains: (1) choosing push- or pull-based communication per operator, (2) restructuring the computation-communication overlap, and (3) fully eliminating CPU-GPU synchronization. MoK distills these insights into a single deterministic training megakernel that fuses token dispatch, shared and routed expert FFNs, and token combine. Across MoE layer shapes from four widely used open-weight models, MoK delivers up to $2.37\times$ the throughput of the strongest publicly available baseline. In a production run on 512 GPUs spanning multiple GB300 NVL72 racks, MoK improves end-to-end training throughput by $1.41\times$.
