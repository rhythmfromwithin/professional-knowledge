---
interest: medium
link: https://arxiv.org/abs/2607.05399
next_step: skim
priority: high
slack_ts: '1783569525.138949'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Benchmarking KV-Cache Optimizations across Task Quality and System Performance
  for Long-Context Serving
---
# Benchmarking KV-Cache Optimizations across Task Quality and System Performance for Long-Context Serving
> 原文: [https://arxiv.org/abs/2607.05399](https://arxiv.org/abs/2607.05399)

arXiv:2607.05399v1 Announce Type: new
Abstract: Large language model serving is increasingly limited by KV-cache growth under long-context workloads, yet existing KV-cache compression techniques are difficult to compare because they were evaluated on different models, tasks, budgets, and serving stacks. This paper presents a workload-aware benchmark of representative KV-cache optimization mechanisms spanning quantization, pruning, and merging, including KIVI, TurboQuant, SnapKV, and CaM, evaluated on LongBench-style multi-document QA, single-document QA, few-shot learning, and summarization workloads using Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3. The benchmark measures task quality, mean output throughput, mean time-to-first-token, and realized compression ratio across context-length buckets. The results show that the compression ratio alone is a poor predictor of end-to-end performance. KIVI4 provides the most stable quality across models, SnapKV delivers the strongest long-context throughput, and CaM yields large gains on selected QA workloads but exhibits substantial workload sensitivity in both quality and realized compression ratio. These findings motivate workload-aware selection of KV-cache mechanisms rather than one-size-fits-all compression and provide deployment guidance for long-context serving systems.
