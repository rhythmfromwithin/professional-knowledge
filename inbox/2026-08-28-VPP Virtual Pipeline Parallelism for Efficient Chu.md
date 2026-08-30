---
interest: medium
link: https://arxiv.org/abs/2608.26523
next_step: skim
priority: medium
slack_ts: '1788066033.888479'
source: cs.DC - Distributed Computing
status: unread
title: 'VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context
  LLM Inference'
---
# VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference
> 原文: [https://arxiv.org/abs/2608.26523](https://arxiv.org/abs/2608.26523)

arXiv:2608.26523v1 Announce Type: new
Abstract: Chunked prefill pipeline parallelism (CPP) is a key technique for LLM inference. However, equal-size chunks exhibit imbalanced latency, as later chunks attend longer prefix KV caches and incur higher attention costs, leading to pipeline bubbles. Existing approaches mitigate this imbalance through dynamic chunk resizing (Dynamic CPP, DCPP), but our measurements show that this trades scheduling overhead for load balancing, which becomes unfavorable on long sequences. In this study, we propose Virtual Pipeline Parallelism (VPP), which keeps chunk sizes fixed and optimizes the pipeline layout through virtual stages. A V-shaped virtual-stage traversal overlaps each chunk's expensive middle stages with the lighter head and tail stages of its neighbors, while asynchronous communication and pipelined packing further reduce communication stalls and cross-request drain bubbles. We implement VPP in vLLM-Ascend and evaluate it on three MoE-based LLMs with sequences up to 1M tokens on 16 Ascend 910C NPUs. VPP improves throughput by up to 13.1% over DCPP on long sequences and 6.7% on mixed workloads, while preserving performance on short sequences. On a 512K-token DeepSeek-V3.1 prefill workload, VPP reduces the pipeline bubble ratio from 6.4% to 0.1%, achieving a 98.0% reduction compared with DCPP.
