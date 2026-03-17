---
interest: medium
link: https://arxiv.org/abs/2603.07345
next_step: skim
priority: medium
slack_ts: '1773715518.303439'
source: cs.DC - Distributed Computing
status: unread
title: 'Uber''s Failover Architecture: Reconciling Reliability and Efficiency in Hyperscale
  Microservice Infrastructure'
---
# Uber's Failover Architecture: Reconciling Reliability and Efficiency in Hyperscale Microservice Infrastructure
> 原文: [https://arxiv.org/abs/2603.07345](https://arxiv.org/abs/2603.07345)

arXiv:2603.07345v1 Announce Type: new
Abstract: Operating a global, real-time platform at Uber's scale requires infrastructure that is both resilient and cost-efficient. Historically, reliability was ensured through a costly 2x capacity model--each service provisioned to handle global traffic independently across two regions--leaving half the fleet idle. We present Uber's Failover Architecture (UFA), which replaces the uniform 2x model with a differentiated architecture aligned to business criticality. Critical services retain failover guarantees, while non-critical services opportunistically use failover buffer capacity reserved for critical services during steady state. During rare "full-peak" failovers, non-critical services are selectively preempted and rapidly restored, with differentiated Service-Level Agreements (SLAs) using on-demand capacity. Automated safeguards, including dependency analysis and regression gates, ensure critical services continue to function even while non-critical services are unavailable. The quantitative impact is significant: UFA reduces steady-state provisioning from 2x to 1.3x, raising utilization from ~20% to ~30% while sustaining 99.97% availability. To date, UFA has hardened over 4,000 unsafe dependencies, eliminated over one million CPU cores from a baseline of about four million cores.
