---
interest: medium
link: https://arxiv.org/abs/2604.08570
next_step: skim
priority: high
slack_ts: '1776137324.190239'
source: cs.LG - Machine Learning
status: unread
title: 'QuanBench+: A Unified Multi-Framework Benchmark for LLM-Based Quantum Code
  Generation'
---
# QuanBench+: A Unified Multi-Framework Benchmark for LLM-Based Quantum Code Generation
> 原文: [https://arxiv.org/abs/2604.08570](https://arxiv.org/abs/2604.08570)

arXiv:2604.08570v1 Announce Type: new
Abstract: Large Language Models (LLMs) are increasingly used for code generation, yet quantum code generation is still evaluated mostly within single frameworks, making it difficult to separate quantum reasoning from framework familiarity. We introduce QuanBench+, a unified benchmark spanning Qiskit, PennyLane, and Cirq, with 42 aligned tasks covering quantum algorithms, gate decomposition, and state preparation.
We evaluate models with executable functional tests, report Pass@1 and Pass@5, and use KL-divergence-based acceptance for probabilistic outputs. We additionally study Pass@1 after feedback-based repair, where a model may revise code after a runtime error or wrong answer. Across frameworks, the strongest one-shot scores reach 59.5% in Qiskit, 54.8% in Cirq, and 42.9% in PennyLane; with feedback-based repair, the best scores rise to 83.3%, 76.2%, and 66.7%, respectively. These results show clear progress, but also that reliable multi-framework quantum code generation remains unsolved and still depends strongly on framework-specific knowledge.
