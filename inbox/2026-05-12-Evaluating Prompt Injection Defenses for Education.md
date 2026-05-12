---
title: "Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.06669
priority: low
status: unread
interest: medium
next_step: skim
---
# Evaluating Prompt Injection Defenses for Educational LLM Tutors: Security-Usability-Latency Trade-offs
> 原文: [https://arxiv.org/abs/2605.06669](https://arxiv.org/abs/2605.06669)

arXiv:2605.06669v1 Announce Type: new
Abstract: Educational LLM tutors face a core AI alignment challenge: they must follow user intent while preserving pedagogical constraints and safety policies. We present an evaluation methodology for prompt-injection defenses in this setting, showing that guardrail design entails explicit trade-offs among adversarial robustness, benign-task usability, and response latency. We evaluate a domain-specific multi-layer safeguard pipeline combining deterministic pattern filters, structural validation, contextual sandboxing, and session-level behavioral checks. On a controlled holdout benchmark with 480 queries (369 injection, 111 benign), the pipeline reaches 46.34% bypass, 0.00% false positive rate, and 2.50 ms average latency -- an operating point that prioritizes pedagogical usability (zero false positives) while maintaining measurable attack resistance. We provide a reproducible benchmark protocol for head-to-head comparison under identical conditions, including stratified bootstrap confidence intervals, paired McNemar significance tests, and direct evaluation of Prompt Guard and NeMo Guardrails on the same split with unified instrumentation. Results expose operational trade-offs: NeMo reaches 0% bypass at 16.22% FPR and 1.3s latency, while Prompt Guard yields 38.48% bypass with 3.60% FPR. The framework supports evidence-based guardrail selection for AI tutoring systems under different institutional risk and usability requirements.
