---
interest: medium
link: https://arxiv.org/abs/2610.28802
next_step: skim
priority: low
slack_ts: '1792642789.743699'
source: cs.CR - Cryptography and Security
status: unread
title: How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context
  in LLM-Driven Vulnerability Discovery
---
# How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context in LLM-Driven Vulnerability Discovery
> 原文: [https://arxiv.org/abs/2610.28802](https://arxiv.org/abs/2610.28802)

arXiv:2610.28802v1 Announce Type: new
Abstract: How much does an agent harness affect vulnerability discovery, and does its value depend on the model? We study 24 model-runner configurations using an open-source harness on a production codebase whose vulnerabilities were non-public at scan time. The pipeline combines static screening, LLM investigation, model self-revalidation, root-cause mapping, independent source review, and isolated proof-of-concept confirmation.
Across 265 confirmed security root causes, the largest two-run configuration covers 60.4%, while 14.3% are found by exactly one model. No single configuration covers all observed findings. In a four-model context experiment, moving from a minimal prompt to an engineered prompt with a CodeQL-derived call graph raises criticality-weighted yield by 20-86% for smaller and mid-tier models, compared with 2% for the frontier model. This comparison changes both prompt and context. Separating those effects shows that the engineered prompt improves yield for all four models, while adding CodeQL context beyond that prompt improves yield only for the smallest model. A held-out CyberGym subset shows the same direction of target-recall improvement for the combined treatment.
Frontier models achieve low false-report rates but do not consistently achieve the highest yield. Strong lower-cost models can deliver similar performance at an order of magnitude lower cost. These results support matching models, prompts, and context to the task, and combining configurations for broader coverage.
