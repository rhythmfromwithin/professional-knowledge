---
title: "Locality, Not Spectral Mixing, Governs Direct Propagation in Distributed Offline Dynamic Programming"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.18615
priority: medium
status: unread
interest: medium
next_step: skim
---
# Locality, Not Spectral Mixing, Governs Direct Propagation in Distributed Offline Dynamic Programming
> 原文: [https://arxiv.org/abs/2604.18615](https://arxiv.org/abs/2604.18615)

arXiv:2604.18615v1 Announce Type: new
Abstract: We study the communication complexity of distributed offline dynamic programming, where a fixed batch dataset is partitioned across (M) machines connected by the data-induced dependency graph. We compare two paradigms: direct boundary-value propagation, which follows Bellman dependencies, and gossip averaging, which mixes local estimates. Our results show that \*\*locality\*\* is the fundamental driver of round complexity. In particular, we prove that no method can achieve (\varepsilon)-accuracy in fewer than (L\_\varepsilon = \left\lfloor \log(1/2\varepsilon) / \log(1/\gamma) \right\rfloor) rounds on graphs of diameter at least (L\_\varepsilon), and we show that direct propagation matches this scaling up to constants, attaining error (O(\gamma^T/(1-\gamma) + \delta/(1-\gamma))) after (T) rounds. In contrast, gossip-style fitted value iteration incurs an additional (1/\mathrm{gap}(W)) dependence in both convergence rate and asymptotic error. We also prove bandwidth-sensitive lower bounds on path topologies and extend the analysis to asynchronous systems with bounded delays. Together, these results show that spectral dependence is an artifact of gossip-based algorithms, whereas locality is the intrinsic barrier in distributed offline dynamic programming.
