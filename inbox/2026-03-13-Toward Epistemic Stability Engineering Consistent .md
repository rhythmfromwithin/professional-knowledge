---
interest: medium
link: https://arxiv.org/abs/2603.10047
next_step: skim
priority: low
slack_ts: '1773974638.719369'
source: cs.SE - Software Engineering
status: unread
title: 'Toward Epistemic Stability: Engineering Consistent Procedures for Industrial
  LLM Hallucination Reduction'
---
# Toward Epistemic Stability: Engineering Consistent Procedures for Industrial LLM Hallucination Reduction
> 原文: [https://arxiv.org/abs/2603.10047](https://arxiv.org/abs/2603.10047)

arXiv:2603.10047v1 Announce Type: new
Abstract: Hallucinations in large language models (LLMs) are outputs that are syntactically coherent but factually incorrect or contextually inconsistent. They are persistent obstacles in high-stakes industrial settings such as engineering design, enterprise resource planning, and IoT telemetry platforms. We present and compare five prompt engineering strategies intended to reduce the variance of model outputs and move toward repeatable, grounded results without modifying model weights or creating complex validation models. These methods include: (M1) Iterative Similarity Convergence, (M2) Decomposed Model-Agnostic Prompting, (M3) Single-Task Agent Specialization, (M4) Enhanced Data Registry, and (M5) Domain Glossary Injection. Each method is evaluated against an internal baseline using an LLM-as-Judge framework over 100 repeated runs per method (same fixed task prompt, stochastic decoding at $\tau = 0.7$. Under this evaluation setup, M4 (Enhanced Data Registry) received ``Better'' verdicts in all 100 trials; M3 and M5 reached 80\% and 77\% respectively; M1 reached 75\%; and M2 was net negative at 34\% when compared to single shot prompting with a modern foundation model. We then developed enhanced version 2 (v2) implementations and assessed them on a 10-trial verification batch; M2 recovered from 34\% to 80\%, the largest gain among the four revised methods. We discuss how these strategies help overcome the non-deterministic nature of LLM results for industrial procedures, even when absolute correctness cannot be guaranteed. We provide pseudocode, verbatim prompts, and batch logs to support independent assessment.
