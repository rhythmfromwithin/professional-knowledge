---
interest: medium
link: https://arxiv.org/abs/2606.05252
next_step: skim
priority: low
slack_ts: '1780718912.816639'
source: cs.CR - Cryptography and Security
status: unread
title: 'From Attack Simulation to SIEM Rule: Deterministic Detection-as-Code Synthesis
  with Probe-Level Traceability'
---
# From Attack Simulation to SIEM Rule: Deterministic Detection-as-Code Synthesis with Probe-Level Traceability
> 原文: [https://arxiv.org/abs/2606.05252](https://arxiv.org/abs/2606.05252)

arXiv:2606.05252v1 Announce Type: new
Abstract: Security teams routinely simulate attacks against their own systems to check whether their monitoring would catch a real intruder. These Breach-and-Attack-Simulation (BAS) tools surface findings, but the security information and event management (SIEM) systems that watch production need detection rules -- and today a human bridges that gap by hand, reading each finding and writing the corresponding Sigma rule (a vendor-neutral detection format). We show this translation can be partially automated when probes are drawn from a locked corpus, so each finding carries a stable identifier back to the originating probe. We describe a deterministic synthesis function that maps each finding to a starter Sigma rule through a small template library (N=23, indexed by categories from the OWASP LLM and Web Top 10), with a back-reference to the originating finding and its MITRE ATT&CK technique. On two locked corpora (17-probe LLM, 23-probe Web), every bypassed-probe finding yields a starter rule, and all 17/17 emitted rules parse and convert to Splunk and Elasticsearch backends. Replayed through a live OpenSearch SIEM, the LLM rules fire on 30% of a held-out AdvBench subset and 14% of HarmBench at 7.7% false positives on a benign baseline; the Web side is validated structurally, not against a held-out attack set. The contribution is a verifiable, byte-stable path from BAS finding to operator-deployable starter rule, re-derivable from the published corpus and template library alone -- trading the breadth of LLM-generative methods for exact reproducibility and a typed traceback from any fired alert to the originating probe.
