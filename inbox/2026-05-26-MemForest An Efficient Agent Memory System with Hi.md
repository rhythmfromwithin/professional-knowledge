---
interest: medium
link: https://arxiv.org/abs/2605.23986
next_step: skim
priority: low
slack_ts: '1779941826.523769'
source: cs.DB - Databases
status: unread
title: 'MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing'
---
# MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing
> 原文: [https://arxiv.org/abs/2605.23986](https://arxiv.org/abs/2605.23986)

arXiv:2605.23986v1 Announce Type: new
Abstract: Memory is a fundamental component for enabling long-context LLM agents, supporting persistent state across interactions through a continuous serve-and-update lifecycle. Despite substantial prior work, existing systems suffer from significant maintenance overhead due to two key limitations: coarse-grained state management and inherently sequential update pipelines. In particular, updates are often tightly coupled with LLM inference and require full-state rewrites, leading to poor scalability and growing latency as memory accumulates. To address these challenges, we present MemForest, a memory framework that reformulates agent memory as a write-efficient temporal data management problem. MemForest breaks the sequential bottleneck via parallel chunk extraction, decoupling memory construction into concurrent, independent operations. To further eliminate coarse-grained maintenance, we introduce MemTree, a hierarchical temporal index that organizes memory as time-ordered trees rather than flat global summaries. This design replaces full-state rewrites with localized per-node updates, reducing maintenance cost to the affected tree paths while naturally preserving temporally evolving states. We evaluate MemForest on two long-context memory benchmarks, LongMemEval-S and LoCoMo. On LongMemEval-S, MemForest achieves the best overall performance among stateful baselines, reaching 79.8% pass@1 accuracy while sustaining a memory construction throughput approximately 6x higher than state-of-the-art approaches including EverMemOS.
