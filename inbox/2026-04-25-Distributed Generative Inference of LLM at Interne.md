---
interest: medium
link: https://arxiv.org/abs/2604.21072
next_step: skim
priority: medium
slack_ts: '1777087213.856149'
source: cs.DC - Distributed Computing
status: unread
title: Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional
  Communication Optimization
---
# Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization
> 原文: [https://arxiv.org/abs/2604.21072](https://arxiv.org/abs/2604.21072)

arXiv:2604.21072v1 Announce Type: new
Abstract: Decentralized LLM inference distributes computation among heterogeneous nodes across the internet, offering a performant and cost-efficient solution, alternative to traditional centralized inference. However, the low cross-node network bandwidth makes communication the primary bottleneck. In this paper, we introduce BloomBee, an internet-scale distributed LLM inference framework. BloomBee integrates LLM-layer assignment, micro-batching and tensor offloading to optimize communication from multiple dimensions. Additionally, BloomBee formulates the coordination of these techniques as an optimization problem and solves it using dynamic programming. BloomBee also customizes lossless compression and speculative decoding according to low-bandwidth network settings to reduce communication overhead. We evaluate BloomBee across a spectrum of network environments and show that it improves service throughput by up to 1.76x. It also reduces average latency by up to 43.20% compared to state-of-the-art decentralized LLM inference systems. BloomBee is open-sourced.
