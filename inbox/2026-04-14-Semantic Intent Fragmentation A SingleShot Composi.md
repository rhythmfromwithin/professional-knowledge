---
title: "Semantic Intent Fragmentation: A Single-Shot Compositional Attack on Multi-Agent AI Pipelines"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.08608
priority: low
status: unread
interest: medium
next_step: skim
---
# Semantic Intent Fragmentation: A Single-Shot Compositional Attack on Multi-Agent AI Pipelines
> 原文: [https://arxiv.org/abs/2604.08608](https://arxiv.org/abs/2604.08608)

arXiv:2604.08608v1 Announce Type: new
Abstract: We introduce Semantic Intent Fragmentation (SIF), an attack class against LLM orchestration systems where a single, legitimately phrased request causes an orchestrator to decompose a task into subtasks that are individually benign but jointly violate security policy. Current safety mechanisms operate at the subtask level, so each step clears existing classifiers -- the violation only emerges at the composed plan. SIF exploits OWASP LLM06:2025 through four mechanisms: bulk scope escalation, silent data exfiltration, embedded trigger deployment, and quasi-identifier aggregation, requiring no injected content, no system modification, and no attacker interaction after the initial request. We construct a three-stage red-teaming pipeline grounded in OWASP, MITRE ATLAS, and NIST frameworks to generate realistic enterprise scenarios. Across 14 scenarios spanning financial reporting, information security, and HR analytics, a GPT-20B orchestrator produces policy-violating plans in 71% of cases (10/14) while every subtask appears benign. Three independent signals validate this: deterministic taint analysis, chain-of-thought evaluation, and a cross-model compliance judge with 0% false positives. Stronger orchestrators increase SIF success rates. Plan-level information-flow tracking combined with compliance evaluation detects all attacks before execution, showing the compositional safety gap is closable.
