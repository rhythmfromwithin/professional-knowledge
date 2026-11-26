---
interest: medium
link: https://arxiv.org/abs/2611.28152
next_step: skim
priority: low
slack_ts: '1795679635.561339'
source: cs.CR - Cryptography and Security
status: unread
title: 'STEGOGUARD-LM: Evaluating End-to-End Protection Against LLM Covert Channels'
---
# STEGOGUARD-LM: Evaluating End-to-End Protection Against LLM Covert Channels
> 原文: [https://arxiv.org/abs/2611.28152](https://arxiv.org/abs/2611.28152)

arXiv:2611.28152v1 Announce Type: new
Abstract: A defense that disrupts hidden messages may still provide little protection if its detector rarely triggers an intervention. We present StegoGuard-LM, a controlled framework for evaluating defenses against covert messages in large language model outputs. We examine token-rank and synonym channels, with Unicode concealment as a structural control, and track messages through detection, intervention, and recovery. Deterministic rewriting prevented full recovery of 103 of 104 synonym-encoded messages when applied unconditionally, but only one when intervention depended on a detector set to limit false alarms. In a four-round replay on a 48-response subset, an attacker selecting from a fixed catalog recovered more bits by switching channels, although paired gains were not statistically significant after correction for multiple comparisons. Randomized rewriting showed no sustained advantage in this pilot. A more sensitive detector improved protection but modified about one-third of clean responses. These findings show how uneven detection can undermine effective rewriting and why protection must be evaluated alongside attacker adaptation and intervention on legitimate text.
