---
interest: medium
link: https://arxiv.org/abs/2607.13078
next_step: skim
priority: low
slack_ts: '1784432002.571059'
source: cs.CR - Cryptography and Security
status: unread
title: Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety
  Workflows
---
# Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows
> 原文: [https://arxiv.org/abs/2607.13078](https://arxiv.org/abs/2607.13078)

arXiv:2607.13078v1 Announce Type: new
Abstract: LLMs are now proposed for fraud detection, scam investigation, content moderation, and other trust-and-safety workflows. Much of the public literature still evaluates them as models, with less attention to their behavior as components in operational pipelines. This creates a practical evidence question: what would justify placing an LLM inside a live workflow with latency, cost, escalation, human-review, and adversarial-risk constraints?
We address this question through a fraud-first survey of deployment evidence. We code 49 operationally relevant sources on LLM use in fraud detection, investigation support, content moderation, and cross-cutting robustness (18 fraud, 14 moderation, 17 cross-cutting), supplemented by 15 contextual references that establish the survey boundaries. These sources include systems, benchmarks, frameworks, and deployment-relevant surveys, not 49 production deployments.
The main finding is an evidence imbalance. Fraud supplies the largest task-specific portion of the coded corpus. The moderation papers, however, include more explicit public evidence on latency, cost, governance, and fairness. Among the 18 fraud and investigation sources, none report clean per-decision latency, per-decision dollar cost, or calibration evidence; most report offline task performance, retrieval gains, or case-study accuracy instead.
The survey contributes a role-and-evidence organizing frame, FORTE, for locating LLMs as classifiers, retrieval interfaces, explanation generators, reviewer assistants, agents, feature extractors, or escalation components. It also contributes a minimum deployment-evidence checklist covering latency budget, cost per decision, decision threshold, explanation integrity, and adversarial pressure. The resulting agenda identifies studies needed to support deployment claims for LLM-based fraud and trust-and-safety work.
