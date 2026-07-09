---
interest: medium
link: https://arxiv.org/abs/2607.02615
next_step: skim
priority: low
slack_ts: '1783569520.034159'
source: cs.CR - Cryptography and Security
status: unread
title: 'The agent creates, we validate: A Lightweight Framework for Agentic Artifact
  Generation'
---
# The agent creates, we validate: A Lightweight Framework for Agentic Artifact Generation
> 原文: [https://arxiv.org/abs/2607.02615](https://arxiv.org/abs/2607.02615)

arXiv:2607.02615v1 Announce Type: new
Abstract: Generating structured artifacts with Large Language Models - e.g. database queries, threat framework mappings, entity schemas - is relatively straightforward; however, making them reliable enough for production deployments presents challenges. We present a lightweight framework based on a core principle: LLMs generate, we validate. This reframing shifts responsibility from generation quality to validation rigor. The framework rests on three key attributes: First, test driven generation: when tests fail, the LLM receives indicative error messages that expose why the output failed, enabling the LLM to understand its mistakes and refine subsequent attempts. Second, deterministic and LLM-based tests: deterministic tests catch heuristics that can be programmatically verified (schema, syntax, cross-reference), while LLM-based tests evaluate nuanced semantic and delicate features that resist programmatic inspection (intent alignment, logical consistency, domain correctness). Third, expert-distilled judges: LLM-based tests are calibrated to distill and replicate human expert decision distribution, transforming manual human quality gates into scalable, reusable evaluation proxies that reflect professional-grade validation standards. We demonstrate the framework on three artifact types in the security domain - KQL query generation, MITRE ATT\&CK mapping, and entity mapping - deployed in production at Microsoft Sentinel. We believe this framework can be applied beyond security to other artifact generation tasks, providing a path to reliable, high-quality outputs without sacrificing the efficiency gains of LLM generation.
