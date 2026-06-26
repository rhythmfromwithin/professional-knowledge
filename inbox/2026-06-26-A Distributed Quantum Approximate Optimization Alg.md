---
interest: medium
link: https://arxiv.org/abs/2606.26297
next_step: skim
priority: medium
slack_ts: '1782447543.947629'
source: cs.DC - Distributed Computing
status: unread
title: A Distributed Quantum Approximate Optimization Algorithm Simulator for Engineering
  Design Optimization
---
# A Distributed Quantum Approximate Optimization Algorithm Simulator for Engineering Design Optimization
> 原文: [https://arxiv.org/abs/2606.26297](https://arxiv.org/abs/2606.26297)

arXiv:2606.26297v1 Announce Type: new
Abstract: This paper presents a Qiskit-compatible distributed quantum approximate optimization algorithm (DQAOA) simulator for quadratic unconstrained binary optimization (QUBO) problems arising in engineering design and decision applications. The open-source simulator is available through the RAISE LAB website and GitHub repository, with README documentation for installation, input formatting, configurable parameters, and example workflows. The package addresses the need for a reusable simulator that can solve and compare QUBO instances across different QAOA execution modes. It supports monolithic QAOA on a single quantum processing unit (QPU) and distributed QAOA across a user-specified number of QPUs with configurable capacities. The workflow canonicalizes the QUBO model, maps it to a cost Hamiltonian, allocates variables across QPUs, identifies local and cross-QPU couplings, and constructs the corresponding circuits. Runtime optimizations, including parameterized circuit reuse, objective reuse at fixed depth, batched evaluations, and parallel multi-start execution, reduce repeated overhead. A Streamlit graphical user interface is also provided for entering or uploading QUBO instances, configuring solver settings, running selected modes, and visualizing solution-quality metrics without editing Python scripts. The package is demonstrated on standalone QUBO benchmarks and a power generation unit commitment application. In the unit commitment case, brute force, monolithic QAOA, and distributed QAOA recover the same commitment bitstring and operating cost. Across multiple case studies, the simulator produces results consistent with classical monolithic QAOA references in terms of optimal bitstrings and costs. Staged runtime analysis shows substantial runtime reduction across implementation stages, while distributed QAOA remains more demanding because cross-QPU couplings require remote operations.
