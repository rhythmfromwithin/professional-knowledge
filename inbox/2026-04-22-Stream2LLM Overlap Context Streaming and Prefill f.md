---
interest: medium
link: https://arxiv.org/abs/2604.16395
next_step: skim
priority: low
slack_ts: '1776915192.936579'
source: cs.DB - Databases
status: unread
title: 'Stream2LLM: Overlap Context Streaming and Prefill for Reduced TTFT'
---
# Stream2LLM: Overlap Context Streaming and Prefill for Reduced TTFT
> 原文: [https://arxiv.org/abs/2604.16395](https://arxiv.org/abs/2604.16395)

arXiv:2604.16395v1 Announce Type: new
Abstract: Context retrieval systems for LLM inference face a critical challenge: high retrieval latency creates a fundamental tension between waiting for complete context (poor time-to-first-token) and proceeding without it (reduced quality). Recent work mitigates this via streaming--overlapping retrieval with inference--but prior systems focus on single-request settings and overlook challenges in multi-tenant deployments where concurrent requests contend for GPU memory and scheduling must adapt to dynamic context arrivals.
We present STREAM2LLM, a system that extends vLLM to support streaming prompts with adaptive scheduling and preemption for two distinct retrieval patterns: append-mode (progressive context accumulation) and update-mode (iterative refinement with cache invalidation). STREAM2LLM decouples scheduling decisions from resource acquisition, enabling flexible preemption strategies guided by hardware-specific cost models, and uses cache invalidation based on longest common prefix matching to minimize redundant computation when prompts change dynamically. To evaluate STREAM2LLM, we collect and characterize two large-scale, real-world streaming workloads based on web crawling and approximate nearest neighbor search. Our evaluation demonstrates that streaming architecture delivers up to 11x TTFT improvements, with cost-aware scheduling providing critical benefits under memory pressure, while maintaining throughput parity with non-streaming baselines.
