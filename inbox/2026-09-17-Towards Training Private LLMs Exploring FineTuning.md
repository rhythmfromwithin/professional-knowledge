---
title: "Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.18066
priority: medium
status: unread
interest: medium
next_step: skim
---
# Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt
> 原文: [https://arxiv.org/abs/2609.18066](https://arxiv.org/abs/2609.18066)

arXiv:2609.18066v1 Announce Type: new
Abstract: Private large language model (LLM) fine-tuning is increasingly important for organizations that need to adapt models using sensitive data, but it often exceeds the memory capacity of commodity datacenter accelerators. Apple Silicon offers a different design point through large unified memory and lower complete-system cost, while recent Apple software support enables distributed execution over RDMA-over-Thunderbolt (TB). This paper studies whether Apple Silicon can serve as a practical platform for private LLM fine-tuning. We characterize RDMA-over-TB communication on Mac Studio nodes, showing that the measured bandwidth is far below nominal TB specifications. Next, we extend Apple's implementation with multi-trunk communication, persistent worker threads, and CPU-side gradient overlap to better exploit multiple direct TB links for LLM fine-tuning workloads. Finally, on a four-node Mac Studio cluster that fine-tunes a Qwen3-9B, our optimizations improve weak-scaling throughput by up to 1.6X over the single-trunk, non-overlapped baseline and reach 936 tokens/s for sequence length 17408. We further compare Apple Silicon with an NVIDIA H100 platform to quantify the trade-off between memory capacity, throughput, and acquisition cost, showing that Apple Silicon can provide a cost-effective solution for private LLM fine-tuning.
