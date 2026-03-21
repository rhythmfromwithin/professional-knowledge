---
title: "Guardrails as Infrastructure: Policy-First Control for Tool-Orchestrated Workflows"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.18059
priority: low
status: unread
interest: medium
next_step: skim
---
# Guardrails as Infrastructure: Policy-First Control for Tool-Orchestrated Workflows
> 原文: [https://arxiv.org/abs/2603.18059](https://arxiv.org/abs/2603.18059)

arXiv:2603.18059v1 Announce Type: new
Abstract: Tool-using automation systems, from scripts and CI bots to agentic assistants, fail in recurring patterns. Common failures include unsafe side effects, invalid arguments, uncontrolled retries, and leakage of sensitive outputs. Many mitigations are model-centric and prompt-dependent, so they are brittle and do not generalize to non-LLM callers. We present Policy-First Tooling, a model-agnostic permission layer that mediates tool invocation through explicit constraints, risk-aware gating, recovery controls, and auditable explanations. The paper contributes a compact policy DSL, a runtime enforcement architecture with actionable rationale and fix hints, and a reproducible benchmark based on trace replay with controlled fault and misuse injection. In 225 controlled runs across five policy packs and three fault profiles, stricter packs improve violation prevention from 0.000 in P0 to 0.681 in P4, while task success drops from 0.356 to 0.067. Retry amplification decreases from 3.774 in P0 to 1.378 in P4, and leakage recall reaches 0.875 under injected secret outputs. These results make safety to utility trade-offs explicit and measurable.
