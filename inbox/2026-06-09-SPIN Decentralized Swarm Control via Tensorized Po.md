---
interest: medium
link: https://arxiv.org/abs/2606.07557
next_step: skim
priority: high
slack_ts: '1780978312.980849'
source: cs.LG - Machine Learning
status: unread
title: 'SPIN: Decentralized Swarm Control via Tensorized Policy Coordination'
---
# SPIN: Decentralized Swarm Control via Tensorized Policy Coordination
> 原文: [https://arxiv.org/abs/2606.07557](https://arxiv.org/abs/2606.07557)

arXiv:2606.07557v1 Announce Type: new
Abstract: Decentralized multi-agent swarm coordination on resource-constrained edge platforms remains fundamentally bottlenecked by the exponential scaling of joint action spaces and high-latency communication overhead. This paper introduces the Swarm Policy Interference Network (SPIN) framework, an architectural paradigm that bypasses these limitations by modeling swarm topologies as a compressed tensor network. We factorize the joint policy tensors of local multi-agent cliques into Matrix Product State (MPS) chains, reducing the computational complexity of evaluation from an exponential $O(n^m)$ wall to a strictly linear $O(m \cdot n \cdot \chi^2)$ constraint. To bridge local continuous spatial geometry with this discrete algebraic backend without requiring power-intensive online training loops, we introduce a decoupled, hybrid neuro-symbolic control pipeline. Local multi-layered neural networks operate as structural coordination encoders, pre-trained offline to nonlinearly map hand-engineered geometric descriptors into abstract environmental target measures. At runtime, edge agents execute instantaneous behavioral adaptations by applying the Radon-Nikod\'ym derivative directly as a zero-shot importance-reweighting filter. We validate the framework within a discrete-time multi-agent simulation sandbox spanning tracking, decentralized dispersion/area coverage, and multi-goal coordination regimes. Qualitative telemetry demonstrates that the integrated pipeline achieves stable target-directed motion, anti-collapse spatial spreading under decentralized constraints, and structured subgroup formation across multiple targets, providing a mathematically grounded route to tractable, low-power edge swarm intelligence.
