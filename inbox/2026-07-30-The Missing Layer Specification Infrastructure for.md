---
title: "The Missing Layer: Specification Infrastructure for AI Oversight"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.24866
priority: low
status: unread
interest: medium
next_step: skim
---
# The Missing Layer: Specification Infrastructure for AI Oversight
> 原文: [https://arxiv.org/abs/2607.24866](https://arxiv.org/abs/2607.24866)

arXiv:2607.24866v1 Announce Type: new
Abstract: AI safety has a missing layer. Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere. We diagnose this as a coordination gap, not a research gap, and propose a two-axis taxonomy: five technical layers (Legibility, Specification, Mediation, Evaluation, Escalation) crossed with six concerns spanning alignment, robustness, adversarial defense, security, governance, and accountability, populating the resulting 5x6 matrix with existing work. Layer 2 (Specification), where humans translate intent into machine-checkable artifacts, is the connective tissue every layer depends on, yet it lacks four marks of a mature engineering discipline: shared vocabulary, design principles, composability standards, and governance practices. We propose six design principles for Layer 2, from elicitability and composability to adversary-awareness, traceability, and governability, made concrete through worked examples and a reference architecture turning specifications into runtime enforcement, evaluation, and escalation. Existing systems such as Cedar, Constitutional AI, and Open Policy Agent each address a fragment of Layer 2 well and the matrix poorly; treating them as fragments of one shared layer makes composition tractable. As evidence, we introduce CARMA, a Layer 2 prototype for autonomous ETL agents in which one specification drives enforcement, evaluation, and escalation, with every decision traceable to a versioned specification, naming what AI oversight is missing and giving independent teams principles to build the missing pieces so they compose.
