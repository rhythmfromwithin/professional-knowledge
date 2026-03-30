---
interest: medium
link: https://arxiv.org/abs/2603.24761
next_step: skim
priority: medium
slack_ts: '1774841191.450169'
source: cs.DC - Distributed Computing
status: unread
title: 'Rafture: Erasure-coded Raft with Post-Dissemination Pruning'
---
# Rafture: Erasure-coded Raft with Post-Dissemination Pruning
> 原文: [https://arxiv.org/abs/2603.24761](https://arxiv.org/abs/2603.24761)

arXiv:2603.24761v1 Announce Type: new
Abstract: Spreading and storing erasure-coded data in distributed systems effectively is challenging in real settings. Practical deployments must contend with unpredictable network latencies, particularly when information dispersal is integrated into consensus protocols, a prominent and latency-sensitive use case. Existing approaches address this challenge through timeout-based dissemination and adaptive communication or storage decisions driven by acknowledgments during dissemination. However, these designs focus almost exclusively on dissemination-time efficiency, complicate recovery with reconstruction procedures that require metadata that can differ per consensus value, and rely on a centralized leader to make storage decisions for all nodes.
This paper introduces \textbf{Rafture}, a novel information dispersal algorithm, and its integration in a consensus protocol, that overcomes these limitations. Rafture is the first information dispersal solution to incorporate post-dissemination pruning, allowing systems to adapt storage costs after dissemination completes. It employs a simple, fixed-threshold erasure code while varying distinct fragment assignment along a second dimension. This ensures that reconstruction is always possible from $F+1$ fragments using the same interpolation method and no additional metadata. Rafture further enables nodes to adapt autonomously based on locally observed information, eliminating the need for global coordination.
We evaluate Rafture in highly dynamic network settings and show that it simplifies recovery while significantly improving long-term storage consumption under variable network conditions.
