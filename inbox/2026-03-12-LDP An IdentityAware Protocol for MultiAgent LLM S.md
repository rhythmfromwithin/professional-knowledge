---
interest: medium
link: https://arxiv.org/abs/2603.08852
next_step: skim
priority: high
slack_ts: '1773888798.454349'
source: cs.AI - Artificial Intelligence
status: unread
title: 'LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems'
---
# LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems
> 原文: [https://arxiv.org/abs/2603.08852](https://arxiv.org/abs/2603.08852)

arXiv:2603.08852v1 Announce Type: new
Abstract: As multi-agent AI systems grow in complexity, the protocols connecting them constrain their capabilities. Current protocols such as A2A and MCP do not expose model-level properties as first-class primitives, ignoring properties fundamental to effective delegation: model identity, reasoning profile, quality calibration, and cost characteristics. We present the LLM Delegate Protocol (LDP), an AI-native communication protocol introducing five mechanisms: (1) rich delegate identity cards with quality hints and reasoning profiles; (2) progressive payload modes with negotiation and fallback; (3) governed sessions with persistent context; (4) structured provenance tracking confidence and verification status; (5) trust domains enforcing security boundaries at the protocol level. We implement LDP as a plugin for the JamJet agent runtime and evaluate against A2A and random baselines using local Ollama models and LLM-as-judge evaluation. Identity-aware routing achieves ~12x lower latency on easy tasks through delegate specialization, though it does not improve aggregate quality in our small delegate pool; semantic frame payloads reduce token count by 37% (p=0.031) with no observed quality loss; governed sessions eliminate 39% token overhead at 10 rounds; and noisy provenance degrades synthesis quality below the no-provenance baseline, arguing that confidence metadata is harmful without verification. Simulated analyses show architectural advantages in attack detection (96% vs. 6%) and failure recovery (100% vs. 35% completion). This paper contributes a protocol design, reference implementation, and initial evidence that AI-native protocol primitives enable more efficient and governable delegation.
