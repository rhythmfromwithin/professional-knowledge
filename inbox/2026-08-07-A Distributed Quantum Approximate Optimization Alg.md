---
title: "A Distributed Quantum Approximate Optimization Algorithm For Unit Commitment"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.04159
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Distributed Quantum Approximate Optimization Algorithm For Unit Commitment
> 原文: [https://arxiv.org/abs/2608.04159](https://arxiv.org/abs/2608.04159)

arXiv:2608.04159v1 Announce Type: new
Abstract: This paper presents a distributed quantum approximate optimization algorithm (DQAOA)-enabled three-block alternating direction method of multipliers (ADMM) framework for unit commitment (UC). The relaxed commitment and dispatch variables are solved in a continuous quadratic programming block, while the binary commitment block is formulated as a quadratic unconstrained binary optimization (QUBO) problem. The DQAOA interface allows this QUBO to be solved using brute-force enumeration, monolithic QAOA, or distributed QAOA, while the remaining ADMM updates are kept unchanged. In the distributed mode, the logical commitment qubits are allocated across multiple capacity-constrained quantum processing units (QPU), avoiding the requirement that the complete binary problem fits on a single device. The framework is evaluated on a five-unit UC instance containing 15 binary variables. All three solver modes reduce the ADMM primal residual below a certain tolerance and recover the same commitment schedule, dispatch, and operating cost. The results demonstrate solution consistency across the three solver modes and the multi-QPU capacity accommodation provided by the distributed QAOA method.
