---
interest: medium
link: https://arxiv.org/abs/2609.21079
next_step: skim
priority: medium
slack_ts: '1790051339.207599'
source: cs.DC - Distributed Computing
status: unread
title: 'DLB: Distributed Load Balancing at Scale for Generative AI Inference'
---
# DLB: Distributed Load Balancing at Scale for Generative AI Inference
> 原文: [https://arxiv.org/abs/2609.21079](https://arxiv.org/abs/2609.21079)

arXiv:2609.21079v1 Announce Type: new
Abstract: The reliance on scarce and expensive accelerators such as GPUs and TPUs in modern datacenters places unprecedented demands on backend infrastructure. For workloads characterized by heterogeneous service times and complex multi-stage processing, such as Generative AI, conventional load balancing techniques are often inadequate, relying heavily on costly overprovisioning to maintain service level objectives. This paper introduces DLB, the Distributed Load Balancer, a novel system designed to minimize end-to-end user latency for large-scale, heterogeneous workloads.
DLB employs a scalable, distributed design with peer-to-peer probing to maintain real-time visibility into server capacity across large-scale, geographically distributed infrastructure. The system continuously learns latency models to estimate the latency impact of routing decisions, allowing it to effectively manage heterogeneous hardware and diverse model architectures. We provide a novel theoretical analysis of our routing algorithms that establishes their stability and global performance guarantees over time. We also evaluate DLB through extensive simulations, which show substantial gains compared to state-of-the-art load balancing algorithms. Finally, following a 22-month deployment of DLB at Google, where it facilitates large-scale Generative AI inference for thousands of different machine learning models and millions of requests per second, we detail the design choices and practical experiences gained from the system in production. Analysis of production migrations demonstrates that DLB yields statistically significant latency reductions compared to the legacy baseline, including a 17\% decrease in median latency and a 13\% decrease at the p95 tail.
