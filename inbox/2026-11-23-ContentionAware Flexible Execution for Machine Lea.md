---
title: "Contention-Aware Flexible Execution for Machine Learning Workloads"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.26840
priority: medium
status: unread
interest: medium
next_step: skim
---
# Contention-Aware Flexible Execution for Machine Learning Workloads
> 原文: [https://arxiv.org/abs/2611.26840](https://arxiv.org/abs/2611.26840)

arXiv:2611.26840v1 Announce Type: new
Abstract: Concurrent kernel execution is a ubiquitous paradigm in artificial intelligence (AI) and machine learning (ML) across both training and inference. That said, concurrency causes potential slowdown as concurrent kernels contend for limited GPU resources (cores, caches, memory bandwidth), which are shared between these kernels rather than exclusively available to one, as in isolated execution. This raises an important research question: to what extent does concurrency slow down kernel execution and how can it be mitigated. To answer this question, our work presents two studies. First, we characterize concurrent kernel execution extensively for the first time, to our knowledge. We conduct not just performance analysis of concurrent kernels but also memory behavior under concurrency on state-of-the-art AMD Instinct MI300X GPUs designed for datacenter AI, using the AMD-internal millisecond sampler. Based on the observations, we share insights on the slowdown along two dimensions (memory vs. compute bound, large vs. small kernels) to inform future optimizations. Second, we put the derived insights to use, aiming to deliver higher performance via targeted, flexible overlap of ML operators. Frameworks today make the simple decision of early-first for concurrent kernels, which is suboptimal. Noticing the opportunity that ML dataflow has inherent flexibility in which operators can be overlapped and how hardware resources can be allocated, we deduce simple heuristics to tune both overlap anchors and resource allocation for concurrent kernels to improve performance. We evaluate our proposed contention-aware flexible execution (termed CAFEML) across a variety of ML scenarios (inference decode, inference prefill, training) and demonstrate a speedup of up to 13% end-to-end with simple scheduling changes and no kernel rewrites.
