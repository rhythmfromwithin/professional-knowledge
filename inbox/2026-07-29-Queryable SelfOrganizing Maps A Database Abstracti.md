---
interest: medium
link: https://arxiv.org/abs/2607.22843
next_step: skim
priority: low
slack_ts: '1785468996.736079'
source: cs.DB - Databases
status: unread
title: 'Queryable Self-Organizing Maps: A Database Abstraction for Topology-Driven
  Data Exploration'
---
# Queryable Self-Organizing Maps: A Database Abstraction for Topology-Driven Data Exploration
> 原文: [https://arxiv.org/abs/2607.22843](https://arxiv.org/abs/2607.22843)

arXiv:2607.22843v1 Announce Type: new
Abstract: Self-Organizing Maps (SOMs) have long been used as exploratory tools for high-dimensional data: they organize objects into a two-dimensional topology that reveals clusters, gradients, sparse regions, dense regions, and boundaries. Yet, in modern data systems, SOMs are typically trained and visualized outside the DBMS, disconnected from the relational data they summarize. We introduce the abstraction of a queryable data map: a learned topological artifact consisting of representatives, neighborhood relations, object assignments, and derived summaries. We instantiate this idea with MapDB, a lightweight prototype that makes SOM artifacts queryable so users can explore data topology without leaving the database. Experimental study shows that SOM training is feasible at moderate analytical scale, that map queries are interactive after materialization, and that SOM regions provide meaningful targets for exploratory SQL.
