---
interest: medium
link: https://arxiv.org/abs/2607.00151
next_step: skim
priority: medium
slack_ts: '1783050943.094619'
source: cs.DC - Distributed Computing
status: unread
title: 'SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead
  Context Engineering'
---
# SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering
> 原文: [https://arxiv.org/abs/2607.00151](https://arxiv.org/abs/2607.00151)

arXiv:2607.00151v1 Announce Type: new
Abstract: LLM-based agents execute multi-turn workflows with continuously growing contexts, where LLM calls are interleaved with tool invocations and environment feedback. To maintain model quality, modern agent frameworks rely on context engineering strategies such as offloading, reduction, and isolation to control the context length. However, these strategies introduce significant context transformation overhead: each transformation invalidates existing KV caches and triggers re-prefill, leading to increased time-to-first-token (TTFT).
In this paper, we identify that context transformations are segment-decomposable, where the transformation of a prefix is independent of future tokens. This property enables transformations to be executed ahead of time. Based on this insight, we propose a lookahead programming model that allows agent frameworks to express context transformations as asynchronous operations without modifying their execution logic. The runtime proactively executes these transformations and prepares transformed KV caches in advance, enabling direct context replacement without blocking. We further design a lookahead-aware scheduler in LLM serving systems to support these asynchronous requests alongside latency-critical workloads with controlled interference. We implement our approach to support representative context engineering strategies and integrate it into existing agent frameworks and LLM serving systems. Experiments show that our approach effectively eliminates transformation overhead and reduces TTFT by up to 11.9x.
