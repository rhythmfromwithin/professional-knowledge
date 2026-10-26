---
title: "Omni-UBench: Benchmarking Omni-Modal LLM-based Guardrails Across Safety, Utility, and Reliability"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.31713
priority: low
status: unread
interest: medium
next_step: skim
---
# Omni-UBench: Benchmarking Omni-Modal LLM-based Guardrails Across Safety, Utility, and Reliability
> 原文: [https://arxiv.org/abs/2610.31713](https://arxiv.org/abs/2610.31713)

arXiv:2610.31713v1 Announce Type: new
Abstract: Advances in Omni-modal Large Language Models (OLLMs) have enabled increasingly seamless human-AI interaction, but their unified processing of heterogeneous modalities also expands the attack surface, allowing adversaries to exploit richer input compositions to circumvent safety alignment. To counter such risks, omni-modal guardrails have been proposed to detect and filter unsafe queries across arbitrary modalities. However, their capabilities and limitations remain insufficiently understood due to the absence of a comprehensive evaluation benchmark. In this paper, we present Omni-UBench, the first comprehensive framework for omni-modal safety assessment, evaluating guardrail models along three critical dimensions, i.e., safety, utility, and reliability. Omni-UBench curates over 183k samples drawn from 35+ heterogeneous sources spanning text, image, audio, video, and their cross-modal combinations, annotated with safety labels under a unified risk taxonomy. Benchmarking under Omni-UBench on 15 representative OLLMs and omni-modal guardrails yields several key findings, including: (1) modern OLLMs exhibit strong content moderation potential even without guardrail-specific tuning; (2) existing guardrails still struggle to identify cross-modal queries that conceal harmful intent or involve sophisticated jailbreaks; (3) they further exhibit substantial safety hallucination and over-sensitivity to textual patterns, revealing a deficient understanding of cross-modal safety semantics. Our findings provide valuable insights for developing more trustworthy omni-modal guardrails in future research.
