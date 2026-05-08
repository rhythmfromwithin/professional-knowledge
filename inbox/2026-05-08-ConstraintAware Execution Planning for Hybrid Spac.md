---
title: "Constraint-Aware Execution Planning for Hybrid Space-Ground Compute Workloads"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.04052
priority: medium
status: unread
interest: medium
next_step: skim
---
# Constraint-Aware Execution Planning for Hybrid Space-Ground Compute Workloads
> 原文: [https://arxiv.org/abs/2605.04052](https://arxiv.org/abs/2605.04052)

arXiv:2605.04052v1 Announce Type: new
Abstract: Low Earth orbit (LEO) satellites increasingly carry compute hardware capable of on-board processing, yet each satellite generates roughly two orders of magnitude more data than it can downlink per orbit. This mismatch forces operators to decide, for every workload, which computation runs on-board and which runs on the ground, how intermediate data crosses the space-ground boundary through narrow contact windows, and how to maintain delivery guarantees over noisy channels. We present Constraint-Aware Execution (CAE), a planning system that takes a satellite identifier, a workload expressed as a directed acyclic graph of processing steps, and a set of orbital and resource constraints, and produces a deterministic, physically grounded execution plan. CAE operates in four phases: (1) orbital environment construction via SGP4 propagation with eclipse detection and ground station pass prediction, (2) compute placement using a cost model that compares on-board resource consumption against transfer overhead, (3) transfer insertion with adaptive forward error correction and security overhead modeling, and (4) greedy first-fit scheduling into orbital windows under power, thermal, compute, and communication constraints. We evaluate CAE against five representative workload patterns across satellites in distinct orbital regimes and demonstrate that the system produces feasible plans in under two seconds, correctly exploits onboard data reduction to minimize transfer volume, and adapts FEC and multi-pass allocation to varying channel conditions. CAE is deployed as a production API computing plans for any cataloged satellite using live two-line element data.
