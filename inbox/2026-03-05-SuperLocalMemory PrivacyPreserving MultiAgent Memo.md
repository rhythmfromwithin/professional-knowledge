---
interest: medium
link: https://arxiv.org/abs/2603.02240
next_step: skim
priority: high
slack_ts: '1773132458.427559'
source: cs.AI - Artificial Intelligence
status: unread
title: 'SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust
  Defense Against Memory Poisoning'
---
# SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning
> 原文: [https://arxiv.org/abs/2603.02240](https://arxiv.org/abs/2603.02240)

arXiv:2603.02240v1 Announce Type: new
Abstract: We present SuperLocalMemory, a local-first memory system for multi-agent AI that defends against OWASP ASI06 memory poisoning through architectural isolation and Bayesian trust scoring, while personalizing retrieval through adaptive learning-to-rank -- all without cloud dependencies or LLM inference calls. As AI agents increasingly rely on persistent memory, cloud-based memory systems create centralized attack surfaces where poisoned memories propagate across sessions and users -- a threat demonstrated in documented attacks against production systems. Our architecture combines SQLite-backed storage with FTS5 full-text search, Leiden-based knowledge graph clustering, an event-driven coordination layer with per-agent provenance, and an adaptive re-ranking framework that learns user preferences through three-layer behavioral analysis (cross-project technology preferences, project context detection, and workflow pattern mining). Evaluation across seven benchmark dimensions demonstrates 10.6ms median search latency, zero concurrency errors under 10 simultaneous agents, trust separation (gap =0.90) with 72% trust degradation for sleeper attacks, and 104% improvement in NDCG@5 when adaptive re-ranking is enabled. Behavioral data is isolated in a separate database with GDPR Article 17 erasure support. SuperLocalMemory is open-source (MIT) and integrates with 17+ development tools via Model Context Protocol.
