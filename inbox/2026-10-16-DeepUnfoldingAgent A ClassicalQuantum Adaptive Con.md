---
title: "DeepUnfolding_Agent: A Classical_Quantum Adaptive Control API"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.20615
priority: high
status: unread
interest: medium
next_step: skim
---
# DeepUnfolding_Agent: A Classical_Quantum Adaptive Control API
> 原文: [https://arxiv.org/abs/2610.20615](https://arxiv.org/abs/2610.20615)

arXiv:2610.20615v1 Announce Type: new
Abstract: Adaptive optimization workflows in machine learning, federated learning, quantum machine learning, and hybrid classical quantum systems often embed controller logic directly inside task specific training scripts. This coupling limits reuse, reproducibility, safety validation, and fair comparison across execution environments. This paper presents DeepUnfolding Agent, a schema-driven FastAPI platform that exposes deep unfolded adaptive control as an external software service. External executors register a strategy schema, submit round-level diagnostic variables, receive schema-bounded control actions, execute one optimization round, and return feedback for controller update. The framework separates controller intelligence from domain specific execution through a strategy registry, diagnostic to state adapter, controller factory, safety guard, executor abstraction, feedback update path, SQLite persistence layer, Docker deployment, and reproducible benchmark scripts. The implementation supports classical, quantum-aware, hybrid, Qiskit Aer, and optional IBM quantum processing execution pathways. We validate the software through unit, schema, API, safety, orchestration, Quantum execution, checkpointing, and Docker tests, and demonstrate external user fixed versus adaptive workflows across finance, healthcare, genomics, transport, noisy quantum simulation, and hardware backed IBM Quantum execution. The results show that DeepUnfolding-Agent provides a reusable and traceable adaptive control layer for heterogeneous optimization workflows. Our quantum experiments are interpreted as API level quantum control and hardware portability evidence.
