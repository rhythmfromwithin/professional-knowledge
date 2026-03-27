---
title: "From Untamed Black Box to Interpretable Pedagogical Orchestration: The Ensemble of Specialized LLMs Architecture for Adaptive Tutoring"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2603.23990
priority: medium
status: unread
interest: medium
next_step: skim
---
# From Untamed Black Box to Interpretable Pedagogical Orchestration: The Ensemble of Specialized LLMs Architecture for Adaptive Tutoring
> 原文: [https://arxiv.org/abs/2603.23990](https://arxiv.org/abs/2603.23990)

arXiv:2603.23990v1 Announce Type: new
Abstract: Monolithic Large Language Models (LLMs) used in educational dialogue often behave as "black boxes," where pedagogical decisions are implicit and difficult to audit, frequently violating instructional constraints by providing answers too early. We introduce the Ensemble of Specialized LLMS (ES-LLMS) architecture that separates decision-making from wording. Pedagogical actions are selected by a deterministic rules-based orchestrator coordinating specialized agents covering tutoring, assessment, feedback, scaffolding, motivation and ethics-guided by an interpretable Bayesian Knowledge Tracing (BKT) student model. An LLM renderer surface-realizes the chosen action in natural language. This design emphasizes reliability and controllability: constraints such as "attempt-before-hint" and hint caps are enforced as explicit rules, and the system logs per-turn agent traces and constraint checks. Validation of pedagogical quality via human expert reviewers (N=6) and a multi-LLM-as-Judge panel (six state-of-the-art models) showed that ES-LLMs were preferred in 91.7% and 79.2% of cases, respectively. The architecture significantly outperformed monolithic baselines across all seven dimensions, particularly in Scaffolding & Guidance, and Trust & Explainability. Furthermore, a Monte Carlo simulation (N=2,400) exposed a "Mastery Gain Paradox," where monolithic tutors inflated short-term performance through over-assistance. In contrast, ES-LLMs achieved 100% adherence to pedagogical constraints (e.g., attempt-before-hint) and a 3.3x increase in hint efficiency. Operationally, ES-LLMs reduced costs by 54% and latency by 22% by utilizing stateless prompts. We conclude that structural decoupling is essential for transforming stochastic models into trustworthy, verifiable and resource-efficient pedagogical agents.
