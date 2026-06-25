---
interest: medium
link: https://arxiv.org/abs/2606.09209
next_step: skim
priority: low
slack_ts: '1782360767.887069'
source: cs.DB - Databases
status: unread
title: Quantum Computing and Data Processing for Frequent Itemset Mining
---
# Quantum Computing and Data Processing for Frequent Itemset Mining
> 原文: [https://arxiv.org/abs/2606.09209](https://arxiv.org/abs/2606.09209)

arXiv:2606.09209v3 Announce Type: replace
Abstract: Frequent Itemset Mining (FIM) is an important task in data analytics, where classical algorithms face scalability bottlenecks from the combinatorial growth of candidates and the memory overhead of their data structures. Inspired by recent developments in quantum computing, in this paper, we propose the Quantum Frequent-itemset Mining (QFM) data-processing framework for FIM. Following the level-wise structure of the itemset lattice, QFM introduces three mechanisms: (1) Bit-Vector Qubit Encoding for quantum data representation, which organizes transaction data into branchless bit-vectors to facilitate systematic uncomputation; (2) Mining-Aware Candidate Superposition, which prepares a quantum superposition over valid candidates at each lattice level rather than the full itemset lattice; and (3) Bit-Parallel Threshold Marking, which constructs a logarithmic-depth threshold-marking oracle for reliable repeated support verification within hardware coherence limits. We provide theoretical time complexity analysis, implement QFM on IBM Qiskit and Amazon Braket, and evaluate it on real-world datasets against representative classical baselines, where QFM achieves 96% improvement on average.
