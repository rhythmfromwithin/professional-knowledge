---
title: "AutoPyVerifier: Learning Compact Executable Verifiers for Large Language Model Outputs"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.22937
priority: high
status: unread
interest: medium
next_step: skim
---
# AutoPyVerifier: Learning Compact Executable Verifiers for Large Language Model Outputs
> 原文: [https://arxiv.org/abs/2604.22937](https://arxiv.org/abs/2604.22937)

arXiv:2604.22937v1 Announce Type: new
Abstract: Verification is becoming central to both reinforcement-learning-based training and inference-time control of large language models (LLMs). Yet current verifiers face a fundamental trade-off: LLM-based verifiers are expressive but hard to control and prone to error, while deterministic executable verifiers are reliable and interpretable but often limited in capability. We study the following question: given a development set of LLM outputs and labels for a target objective, such as correctness, can we automatically induce a minimal set of Python verifiers whose joint satisfaction closely matches that objective? We propose AutoPyVerifier, a framework that uses an LLM to synthesize candidate verifier functions and then refines them through search over a directed acyclic graph (DAG). By navigating the DAG, AutoPyVerifier systematically explores the space of deterministic executable verifiers and selects a compact verifier set whose joint satisfaction best approximates the target objective. Across mathematical reasoning, coding, function calling, and instruction-following benchmarks for several state-of-the-art LLMs, AutoPyVerifier improves target-objective prediction by up to 55.0 F1 points over the initial LLM-generated verifier sets. Additional analyses show that the most useful verification targets vary by benchmark and model, and that the DAG-based search shifts the learned verifier sets toward more structural and semantically grounded checks. We further show that exposing the discovered verifier set to an LLM as an external tool improves downstream accuracy by up to 17.0 points. We release our code
