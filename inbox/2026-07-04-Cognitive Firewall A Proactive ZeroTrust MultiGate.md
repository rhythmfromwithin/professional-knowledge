---
interest: medium
link: https://arxiv.org/abs/2607.01277
next_step: skim
priority: low
slack_ts: '1783136960.582469'
source: cs.CR - Cryptography and Security
status: unread
title: 'Cognitive Firewall: A Proactive, Zero-Trust, Multi-Gate Framework for LLM
  Safety'
---
# Cognitive Firewall: A Proactive, Zero-Trust, Multi-Gate Framework for LLM Safety
> 原文: [https://arxiv.org/abs/2607.01277](https://arxiv.org/abs/2607.01277)

arXiv:2607.01277v1 Announce Type: new
Abstract: Large language models (LLMs) can be induced to produce harmful content through multi turn strategies in which no single user message appears clearly unsafe. Existing runtime safeguards commonly evaluate prompts or responses as isolated messages, which limits their ability to recover ac-cumulated intent, verify asserted authority, or detect harmful objectives decomposed across a dialogue. This paper presents the Cognitive Firewall, a proactive runtime oversight framework that interposes an independent oversight model between a user and a protected target mod l. The framework decomposes safety assessment into four categorical gates: an intent gate that identi-fies the operational objective of a request, a zero trust context gate that treats claimed roles and permissions as unverified evidence, a consistency gate that detects escalation and decomposition across turns, and an output risk gate that inspects candidate responses before release. Gate decisions are combined through escalation rather than score averaging, allowing any confident danger signal to block an interaction while preserving an auditable rationale. Experiments on four jailbreak benchmarks and a benign safety test set show that the Cognitive Firewall substantially reduces attack success across single turn, multi turn, authority based, and human crafted attacks. It lowers attack success to 2 percent or below on three attack sets and to 14 percent on the most difficult human crafted set, while maintaining an 8 percent over refusal rate. These results indicate that decomposed, conversation level oversight can improve proactive containment and auditability for LLM safety.
