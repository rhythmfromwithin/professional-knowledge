---
interest: medium
link: https://arxiv.org/abs/2607.15593
next_step: skim
priority: medium
slack_ts: '1784690755.357269'
source: cs.DC - Distributed Computing
status: unread
title: Scalable LLM Agent Tool Access in the Cloud
---
# Scalable LLM Agent Tool Access in the Cloud
> 原文: [https://arxiv.org/abs/2607.15593](https://arxiv.org/abs/2607.15593)

arXiv:2607.15593v1 Announce Type: new
Abstract: LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface. Operating MCP at cloud scale, however, becomes difficult. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development also creates ongoing compatibility cost. On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. Moreover, for stateful MCP backends with multiple replicas, preserving session affinity increases client-side complexity.
We present a cloud-scale gateway system for MCP service. It breaks the direct-connect model on the data plane and offloads legacy service integration, consolidating incompatible MCP variants, access control, tool recommendation, and session-aware routing to the gateway. Hybrid retrieval sustains 98% Top-15 recall; it scales agent tool access to 3,000+ with high tool selection accuracy, and reduces tool selection time by $8.9\times$ and token usage by $23.8\times$, with low per-call overhead, stable under scale-out. Finally, we share the lessons learned from deploying the gateway system in production.
