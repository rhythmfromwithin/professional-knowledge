---
title: "From Conflict to Consensus: Boosting Medical Reasoning via Multi-Round Agentic RAG"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.03292
priority: high
status: unread
---
# From Conflict to Consensus: Boosting Medical Reasoning via Multi-Round Agentic RAG
> 原文: [https://arxiv.org/abs/2603.03292](https://arxiv.org/abs/2603.03292)

arXiv:2603.03292v1 Announce Type: new
Abstract: Large Language Models (LLMs) exhibit high reasoning capacity in medical question-answering, but their tendency to produce hallucinations and outdated knowledge poses critical risks in healthcare fields. While Retrieval-Augmented Generation (RAG) mitigates these issues, existing methods rely on noisy token-level signals and lack the multi-round refinement required for complex reasoning. In the paper, we propose \*\*MA-RAG\*\* (\*\*M\*\*ulti-Round \*\*A\*\*gentic RAG), a framework that facilitates test-time scaling for complex medical reasoning by iteratively evolving both external evidence and internal reasoning history within an agentic refinement loop. At each round, the agent transforms semantic \*\*conflict\*\* among candidate responses into actionable queries to retrieve external evidence, while optimizing history reasoning traces to mitigate long-context degradation. MA-RAG extends the \*self-consistency\* principle by leveraging the lack of consistency as a proactive signal for multi-round agentic reasoning and retrieval, and mirrors a \*boosting\* mechanism that iteratively minimizes the residual error toward a stable, high-fidelity medical \*\*consensus\*\*. Extensive evaluations across 7 medical Q&A benchmarks show that MA-RAG consistently surpasses competitive inference-time scaling and RAG baselines, delivering \*\*substantial +6.8 points\*\* on average accuracy over the backbone model. Our code is available at [this url](https://github.com/NJU-RL/MA-RAG).
