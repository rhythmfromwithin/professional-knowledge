---
interest: medium
link: https://arxiv.org/abs/2603.00866
next_step: skim
priority: low
slack_ts: '1773283505.655349'
source: cs.DB - Databases
status: unread
title: 'A Tree-Structured Two-Phase Commit Framework for OceanBase: Optimizing Scalability
  and Consistency'
---
# A Tree-Structured Two-Phase Commit Framework for OceanBase: Optimizing Scalability and Consistency
> 原文: [https://arxiv.org/abs/2603.00866](https://arxiv.org/abs/2603.00866)

arXiv:2603.00866v1 Announce Type: new
Abstract: Modern distributed databases face challenges in achieving transactional consistency across distributed partitions. Traditional two-phase commit (2PC) protocols incur high coordination overhead and latency, and require complex recovery for dynamic partition transfers. This paper introduces a novel tree-shaped 2PC framework for OceanBase that leverages single-machine log streams to address these challenges through three innovations. First, we propose log streams as atomic participants, replacing partition-level coordination. By treating each log stream as the commit unit, a transaction spanning $N$ co-located partitions interacts with one participant, reducing coordination overhead by orders of magnitude (e.g., 99 percent reduction for $N=100$). Second, we design a tree-shaped 2PC protocol with coordinator-rooted DAG topology that dynamically handles partition transfers by recursively constructing commit trees. When a partition migrates during a transaction, the protocol embeds migration contexts as leaf nodes, eliminating explicit participant list updates, resolving circular dependencies, and ensuring linearizable commits under topology changes. Third, we introduce prepare-unknown and trans-unknown states to prevent consistency violations when participants lose context. These states signal uncertainty during retries, avoiding erroneous aborts from so-called lying participants while isolating users from ambiguity. Experimental evaluation demonstrates performance approaching that of single-machine transactions, with reduced latency and bandwidth consumption, validating the framework's effectiveness for modern distributed databases.
