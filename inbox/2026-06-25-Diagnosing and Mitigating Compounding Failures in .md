---
interest: medium
link: https://arxiv.org/abs/2606.24976
next_step: skim
priority: high
slack_ts: '1782360758.730709'
source: cs.AI - Artificial Intelligence
status: unread
title: Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic
  Strategy Retrieval
---
# Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval
> 原文: [https://arxiv.org/abs/2606.24976](https://arxiv.org/abs/2606.24976)

arXiv:2606.24976v1 Announce Type: new
Abstract: Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in deterministic domains, agents in subjective tasks like persuasion experience severe problem drift and sycophantic conformity. We identify semantic leakage in standard Retrieval-Augmented Generation (RAG) as a reproducible trigger for these failures, as standard RAG prioritizes vocabulary overlap over logical necessity.
To eliminate this leakage, we introduce Taxonomic Strategy RAG (TS-RAG), a systems intervention that routes strategies through a discrete categorical bottleneck to decouple argumentative structure from topical content. Zero-shot, cross-domain evaluations demonstrate that TS-RAG significantly improves the transfer of abstract logic where standard semantic retrieval collapses. Crucially, TS-RAG acts as a "capability bridge" in asymmetric deployments, empowering lightweight persuaders to consistently defeat parametrically superior opponents (improving win rates from 70.5 to 78.5) and accelerating argumentative efficiency. Finally, we introduce trace-level diagnostics via a turn-by-turn Debate State Representation (DSR), demonstrating the necessity of strict constraints to prevent evaluation collapse via default agentic sycophancy.
