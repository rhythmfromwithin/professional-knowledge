---
interest: medium
link: https://arxiv.org/abs/2607.21642
next_step: skim
priority: low
slack_ts: '1785208713.456189'
source: cs.CR - Cryptography and Security
status: unread
title: 'CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents'
---
# CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents
> 原文: [https://arxiv.org/abs/2607.21642](https://arxiv.org/abs/2607.21642)

arXiv:2607.21642v1 Announce Type: new
Abstract: Large Language Model (LLM) agents are increasingly used for coding and terminal automation, making shell-command dispatch a high-stakes runtime control point. We study command-level pre-execution mediation for individual shell commands produced by LLM agents under bounded path context. Existing safeguards remain limited: generic guardrails do not model shell structure in sufficient detail, always-on LLM judges are relatively costly and variable, and shell parsers do not directly prevent harmful execution. We present CARE (Canonicalization, Attribution, and Resolution Engine), a shell-specific, static-first verifier for individual shell commands before execution. CARE canonicalizes generated commands into stable verification targets, derives deterministic evidence over syntax, command semantics, path context, and provenance-backed risk patterns, and escalates only underdetermined cases to an LLM judge. This design keeps the common case fast, reproducible, and auditable while reserving neural adjudication for borderline commands. On the balanced main split, CARE reaches 85.64% F1 with a 0.91% false-positive rate at 2.32 ms mean latency. When deployed in its static enforcement profile, CARE retains 84.99% F1 at 0.34 ms and reduces realised harm on RedCode-gen to 37.33%. Across external-generalization tests and controlled Docker-sandbox execution, these profiles expose a practical trade-off between benign recovery, false-positive burden, latency, and harm reduction. Overall, command-level shell mediation can reduce dispatch-boundary risk for LLM agents while preserving most benign workflows.
