---
interest: medium
link: https://arxiv.org/abs/2604.08601
next_step: skim
priority: high
slack_ts: '1776223650.558759'
source: cs.AI - Artificial Intelligence
status: unread
title: 'OpenKedge: Governing Agentic Mutation with Execution-Bound Safety and Evidence
  Chains'
---
# OpenKedge: Governing Agentic Mutation with Execution-Bound Safety and Evidence Chains
> 原文: [https://arxiv.org/abs/2604.08601](https://arxiv.org/abs/2604.08601)

arXiv:2604.08601v1 Announce Type: new
Abstract: The rise of autonomous AI agents exposes a fundamental flaw in API-centric architectures: probabilistic systems directly execute state mutations without sufficient context, coordination, or safety guarantees. We introduce OpenKedge, a protocol that redefines mutation as a governed process rather than an immediate consequence of API invocation. OpenKedge requires actors to submit declarative intent proposals, which are evaluated against deterministically derived system state, temporal signals, and policy constraints prior to execution. Approved intents are compiled into execution contracts that strictly bound permitted actions, resource scope, and time, and are enforced via ephemeral, task-oriented identities. This shifts safety from reactive filtering to preventative, execution-bound enforcement. Crucially, OpenKedge introduces an Intent-to-Execution Evidence Chain (IEEC), which cryptographically links intent, context, policy decisions, execution bounds, and outcomes into a unified lineage. This transforms mutation into a verifiable and reconstructable process, enabling deterministic auditability and reasoning about system behavior. We evaluate OpenKedge across multi-agent conflict scenarios and cloud infrastructure mutations. Results show that the protocol deterministically arbitrates competing intents and cages unsafe execution while maintaining high throughput, establishing a principled foundation for safely operating agentic systems at scale.
