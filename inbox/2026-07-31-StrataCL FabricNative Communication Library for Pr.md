---
title: "StrataCL: Fabric-Native Communication Library for Production Supernodes"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.26444
priority: medium
status: unread
interest: medium
next_step: skim
---
# StrataCL: Fabric-Native Communication Library for Production Supernodes
> 原文: [https://arxiv.org/abs/2607.26444](https://arxiv.org/abs/2607.26444)

arXiv:2607.26444v1 Announce Type: new
Abstract: Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck. Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration. This paper presents StrataCL, a zero-redundancy and fabric-native communication library for production supernodes. StrataCL introduces registration-on-allocation to realize user-buffer direct communication, and designs communication operators with workload-balanced NPU-core partitioning and NPU-driven SDMA offloading to exploit supernode architecture features. On the Huawei CloudMatrix384, StrataCL improves collective bus bandwidth by up to 1.6x and improves MoE dispatch/combine bus bandwidth by up to 1.4x. Across three production workloads, StrataCL improves LLM inference throughput by 1.9x, reduces P99 TTFT by 2.2x, and reduces LLM and Recsys training iteration time by 1.4x and 1.3x, respectively.
