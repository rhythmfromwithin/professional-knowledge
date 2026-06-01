---
interest: medium
link: https://arxiv.org/abs/2605.30534
next_step: skim
priority: low
slack_ts: '1780290098.314409'
source: cs.CR - Cryptography and Security
status: unread
title: 'Strengthening Polymorphic Prompt Assembling: Dynamic Separator Generation
  Against Emerging Prompt Injection Attacks'
---
# Strengthening Polymorphic Prompt Assembling: Dynamic Separator Generation Against Emerging Prompt Injection Attacks
> 原文: [https://arxiv.org/abs/2605.30534](https://arxiv.org/abs/2605.30534)

arXiv:2605.30534v1 Announce Type: new
Abstract: Polymorphic Prompt Assembling (PPA) defends LLM agents against prompt injections by randomly selecting separator pairs from a fixed pool to isolate user input from system instructions. Although effective, static pool reuse exposes a blast-radius vulnerability: once a separator leaks, it can be exploited in future requests. We propose a dynamic per-request separator generation using domain-separated SHA-256 digests keyed on the timestamp, session identifier, and cryptographic nonce. Each assembled prompt receives a unique (BEGIN, END) canary pair, thereby limiting leakage exposure to a single request. We evaluated our extension against 16 injection payloads on Llama-3.3-70B-Instruct-Turbo, with cross-model validation on DeepSeek-V4-Flash model. Against the M1 obfuscation payload (leetspeak + urgency), the dynamic mode reduces the Attack Success Rate (ASR) from 0.88 to 0.38, yielding a statistically significant 2.3 x mitigation verified by non-overlapping 95% Wilson confidence intervals. Against format\_breakout\_salad, static separator leakage (leak\_rate = 0.467) is eliminated entirely in the dynamic mode (0.000), confirming the blast-radius reduction in practice. The implementation requires no model fine-tuning, adds 2.7 microseconds prompt-assembly overhead per request, and is backward compatible with the existing PPA SDK.
