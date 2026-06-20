---
interest: medium
link: https://arxiv.org/abs/2606.19746
next_step: skim
priority: medium
slack_ts: '1781930797.490539'
source: cs.DC - Distributed Computing
status: unread
title: 'SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL'
---
# SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL
> 原文: [https://arxiv.org/abs/2606.19746](https://arxiv.org/abs/2606.19746)

arXiv:2606.19746v1 Announce Type: new
Abstract: The scaling of LLMs toward long-context inference has shifted the primary serving system bottleneck from computation to memory capacity. Traditional solutions for dense attention models rely on RDMA-based disaggregated memory pools, which perform coarse-grained fetching of the entire prefix KV cache from remote storage to local memory before decoding. However, this approach is fundamentally inefficient for emerging sparse attention models. While only a small fraction of KV entries are active during decoding, these systems still fetch the full KV cache locally, leading to severe transmission bottlenecks and local memory wastage. To address this, we propose SAC, the first efficient disaggregated KV cache system optimized for sparse attention models. By leveraging the low-latency, cache-line granularity load/store semantics of Compute Express Link (CXL), SAC fetches only the required top-k KV entries on demand during inference. Evaluations on DeepSeek-V3.2 using SGLang show that SAC achieves 2.1x higher throughput, 9.7x lower TTFT, and 1.8x lower TBT compared to RDMA-based baselines, establishing CXL-based disaggregation as the superior infrastructure for emerging sparse attention models.
