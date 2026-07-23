---
title: "Remora: Scale-out Deterministic Execution for Smart Contracts"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.02817
priority: low
status: unread
interest: medium
next_step: skim
---
# Remora: Scale-out Deterministic Execution for Smart Contracts
> 原文: [https://arxiv.org/abs/2607.02817](https://arxiv.org/abs/2607.02817)

arXiv:2607.02817v2 Announce Type: replace-cross
Abstract: Modern blockchains rely on a modular architecture that decouples consensus from execution. Recent advances in consensus algorithms have shifted the bottleneck to the execution layer, which must deterministically follow the consensus order and handle increasingly complex, compute-intensive smart contracts. We identify that single-node validators cannot keep up, motivating the need for a scale-out design. We design Remora, a scale-out smart contract execution engine. Remora adopts an efficient asymmetric architecture with centralized transaction dispatching and distributed execution, and depends on an object versioning scheme with a strict ownership model to guarantee deterministic scale-out execution. Remora achieves up to 3x throughput improvement compared to state-of-the-art deterministic execution schemes, scales up to 250k TPS, matching modern consensus performance, and reduces latency by up to 5ms. We also show that Remora elastically adapts to bursty workloads and dynamic access patterns using real-world traces. Remora's main performance benefits come from a novel stateless-stateful separation during smart contract execution, which overlaps the execution of state-independent tasks with consensus, and a new locality-aware and load-balanced scheduling scheme.
