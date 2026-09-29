---
interest: medium
link: https://arxiv.org/abs/2609.30313
next_step: skim
priority: low
slack_ts: '1790659450.669039'
source: cs.SE - Software Engineering
status: unread
title: 'HyQDB: LLM-Assisted Debugging for Hybrid Quantum Workflows'
---
# HyQDB: LLM-Assisted Debugging for Hybrid Quantum Workflows
> 原文: [https://arxiv.org/abs/2609.30313](https://arxiv.org/abs/2609.30313)

arXiv:2609.30313v1 Announce Type: new
Abstract: Hybrid quantum program failures frequently occur silently, yet existing debugging tools provide limited support for detecting and repairing them. These faults dominate the failures reported by domain experts, yet existing tools evaluate on public data that under-represents this failure mode. Our key insight is that faults divide into two classes that require different strategies: mechanical faults, which allow deterministic analysis, and conceptual faults, which require reconstructing the program's intent. To address this challenge, we present HyQDB, a tiered agent that injects deterministic hardware, physics and optimization evidence into the LLM repair process. When no evidence is detected, the agent treats this silence as a signal to escalate to a second intent-reconstruction tier, that infers the program's behaviour and reconciles it with the implementation. To evaluate HyQDB, we introduce QFaultBench, a benchmark built from an expert-derived fault taxonomy that represents the true failure modes of hybrid programs. On a held-out set of human-authored programs, HyQDB raises repair success over a standard LLM from 45% to 75%. We show that the escalation gate is crucial, giving a 20% improvement in mechanical fault repair accuracy.
