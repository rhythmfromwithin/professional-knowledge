---
interest: medium
link: https://arxiv.org/abs/2607.13276
next_step: skim
priority: low
slack_ts: '1784344396.812869'
source: cs.DB - Databases
status: unread
title: 'Aurora DSQL: Scalable, Multi-Region OLTP'
---
# Aurora DSQL: Scalable, Multi-Region OLTP
> 原文: [https://arxiv.org/abs/2607.13276](https://arxiv.org/abs/2607.13276)

arXiv:2607.13276v2 Announce Type: new
Abstract: Aurora DSQL is a serverless SQL database designed for cloud-scale transaction processing with multi-region active-active capabilities. Built on a disaggregated architecture, DSQL separates compute, storage, and transaction coordination into independent, horizontally scalable services. Query processors run in Firecracker MicroVMs executing PostgreSQL-compatible SQL without local state. The system uses multiversion concurrency control with precision timestamps for coordination-free reads and optimistic concurrency control for writes, deferring coordination to commit time through distributed adjudicators and the Journal replication system. This minimizes cross-region latency by requiring coordination only during commits, not individual statements. DSQL enables elastic scaling from zero to millions of transactions per second while providing strong consistency, ACID transactions, and continuous availability during availability zone or region failures.
