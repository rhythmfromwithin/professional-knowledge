---
interest: medium
link: https://arxiv.org/abs/2608.29581
next_step: skim
priority: medium
slack_ts: '1788237863.972429'
source: cs.DC - Distributed Computing
status: unread
title: 'Bridging Agent Semantics with Spot Capacity: An Elastic and Recoverable Service
  Model'
---
# Bridging Agent Semantics with Spot Capacity: An Elastic and Recoverable Service Model
> 原文: [https://arxiv.org/abs/2608.29581](https://arxiv.org/abs/2608.29581)

arXiv:2608.29581v1 Announce Type: new
Abstract: LLM agents increasingly drive long-running cloud inference workloads in which model calls differ in urgency, redundancy, completion semantics, and replay cost. Model-as-a-Service (MaaS) platforms expose several service models for trading cost against latency, availability, and capacity commitment. These models operate primarily at request, job, or endpoint scopes and provide limited support for combining transient platform supply with the evolving semantics of an agent task.
We present SemSpot, a semantics-aware service model that allows agent applications to leverage the spot capacity of LLM inference platforms. At the request level, SemSpot lets a provider publish short-lived offers over successful price, completion probability, and failure-notification deadline; the agent runtime selects among these offers using the current task state and completion rule. An audit of 1,535 cases from six agent benchmarks identifies four recurring workflow structures and shows how this service model may produce different cost, service-time, and fallback behavior. With specialized MaaS support, token-level SemSpot further preserves provider inference state and runtime-verified semantic segments inside a long request. We develop the service model, economic boundary, and the cross-layer research agenda required to realize SemSpot.
