---
interest: medium
link: https://arxiv.org/abs/2603.26698
next_step: skim
priority: low
slack_ts: '1775098530.241669'
source: cs.DB - Databases
status: unread
title: Partial Partial Aggregates
---
# Partial Partial Aggregates
> 原文: [https://arxiv.org/abs/2603.26698](https://arxiv.org/abs/2603.26698)

arXiv:2603.26698v1 Announce Type: new
Abstract: We introduce partial partial aggregates (PPA), a query optimization technique for distributed engines that pushes only the local compute phase of an aggregate operation through joins. A query that aggregates after a join involves two logical operations, each requiring a network shuffle. Pushing a full aggregate (COMPUTE$\rightarrow$DISTRIBUTE$\rightarrow$MERGE) below the join introduces a third shuffle. In the specific case where the join key is included in the grouping key and the join is FK-PK, the full pushed aggregate can eliminate the top-level aggregate entirely, making it the preferred choice. In all other key configurations, the top aggregate must remain, and the extra shuffle is wasteful. A PPA pushes only COMPUTE, achieving data reduction before the join without the extra shuffle. The technique relies on the distributive property of aggregates and requires accurate NDV estimation for cost-based decisions.
