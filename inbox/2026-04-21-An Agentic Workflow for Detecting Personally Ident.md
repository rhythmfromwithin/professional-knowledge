---
interest: medium
link: https://arxiv.org/abs/2604.15369
next_step: skim
priority: low
slack_ts: '1776742299.611239'
source: cs.CR - Cryptography and Security
status: unread
title: An Agentic Workflow for Detecting Personally Identifiable Information in Crash
  Narratives
---
# An Agentic Workflow for Detecting Personally Identifiable Information in Crash Narratives
> 原文: [https://arxiv.org/abs/2604.15369](https://arxiv.org/abs/2604.15369)

arXiv:2604.15369v1 Announce Type: new
Abstract: Crash narratives in crash reports provide crucial contextual information for traffic safety analysis. Yet, their broader use is hindered by the presence of personally identifiable information (PII), including names, home addresses, and license plate numbers. Because PII appears sparsely and inconsistently in crash narratives, manual detection is not scalable, and existing rule-based approaches often fail to capture context-dependent PII. This study develops and evaluates a locally deployable, agentic workflow for PII detection in crash narratives by leveraging large language models (LLMs). The workflow contains a Hybrid Extractor and a Verifier. The Hybrid Extractor routes structured PII (e.g., phone numbers and email addresses) to a rule-based model (i.e., Presidio) and context-dependent PII (e.g., names, home addresses, and alphanumeric identifiers) to a domain-adapted, fine-tuned LLM. To address ambiguity in challenging categories, the workflow incorporates ensemble LLM extraction and an agentic verification step that filters false detections through evidence-based reasoning. Evaluated on a real-world crash dataset, the agentic workflow achieves strong performance with a precision of 0.82, a recall of 0.94, an F1 of 0.87, and an accuracy of 0.96, outperforming multiple baseline methods. Moreover, the ablation results suggest that ensemble LLM extraction and Verifier offer improved detection for home addresses and alphanumeric identifiers. The workflow runs locally, supporting privacy-sensitive operational settings where external APIs are restricted. This work offers a practical and robust path for scalable, privacy-preserving crash data processing, enabling broader research and safety interventions while safeguarding individual privacy.
