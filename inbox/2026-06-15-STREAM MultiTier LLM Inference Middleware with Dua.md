---
interest: medium
link: https://arxiv.org/abs/2606.13968
next_step: skim
priority: medium
slack_ts: '1781500247.501079'
source: cs.DC - Distributed Computing
status: unread
title: 'STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming'
---
# STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming
> 原文: [https://arxiv.org/abs/2606.13968](https://arxiv.org/abs/2606.13968)

arXiv:2606.13968v1 Announce Type: new
Abstract: Researchers and practitioners working with large language models face a fragmented landscape: local models are free and private but hardware limits the model size and context windows a researcher can use; institutional HPC centers offer powerful GPU resources at no marginal cost and keep data within institutional boundaries, but operate behind firewalls and are designed for batch jobs rather than interactive use; commercial cloud APIs provide frontier-model quality on demand but impose significant cost and data retention policies unsuitable for sensitive research data. No existing system unifies all three. STREAM (Smart Tiered Routing Engine for AI Models) addresses this gap with four contributions: (1) a three-tier routing architecture combining local, HPC, and cloud inference with a local LLM-based complexity judge; (2) a dual-channel HPC streaming architecture that separates the Globus Compute control plane (authentication and job dispatch) from a WebSocket relay data plane (token delivery), enabling sub-second TTFT (0.54 s median, 21.1x over batch mode's 11.40 s) through institutional firewalls without VPN or firewall rule changes, with end-to-end AES-256-GCM encryption ensuring the relay operator cannot read token payloads; (3) tier-aware context summarization that prevents long conversations from forcing simple queries onto expensive tiers; and (4) an HPC-as-API proxy mode that exposes HPC inference as an OpenAI-compatible endpoint callable from any standard client with no HPC expertise, a deployment pattern made practical only by the sub-second TTFT of contribution (2). Llama 3.2 3B achieves 85.1% free-tier retention on a 1,200-query benchmark spanning ten domains. Measured TTFT: 0.26 s local, 0.54 s HPC (relay), 1.68 s cloud.
