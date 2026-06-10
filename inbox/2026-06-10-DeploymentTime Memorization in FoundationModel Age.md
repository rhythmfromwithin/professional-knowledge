---
interest: medium
link: https://arxiv.org/abs/2606.10062
next_step: skim
priority: high
slack_ts: '1781065403.530879'
source: cs.AI - Artificial Intelligence
status: unread
title: Deployment-Time Memorization in Foundation-Model Agents
---
# Deployment-Time Memorization in Foundation-Model Agents
> 原文: [https://arxiv.org/abs/2606.10062](https://arxiv.org/abs/2606.10062)

arXiv:2606.10062v1 Announce Type: new
Abstract: Foundation-model agents are increasingly long-lived systems that remember users across interactions, making memorization an explicit deployment-time function rather than solely a property of model weights. Existing work addresses parametric memorization or audits fixed memory configurations, but does not characterize how memory-design choices jointly shape personalization utility, extraction risk, and deletion fidelity. We study this surface as deployment-time memorization, formulating agent memory as a privacy-utility frontier measured by Personalization Recall (PR) and Adversarial Extraction Rate (AER), and sweeping three memory-design knobs: summarization aggressiveness, retrieval breadth (k), and deletion mode. We further introduce the Forgetting Residue Score (FRS) to quantify whether deleted information remains recoverable from derived memory tiers. On LongMemEval, key-fact summarization reduces canary extraction by 76% on Gemma 3 12B and 64% on GPT-4o-mini while preserving nearly all personalization recall; critically, once content is compressed away, increasing k no longer restores leakage. The same compression, however, induces a deletion-fidelity failure: raw-only deletion leaves derived summary copies recoverable in approximately 20% of instances, and only full-pipeline purge or tombstone redaction drives worst-tier residue to zero. Together, these results establish that persistent agent memory must be evaluated as a first-class memorization mechanism -- assessed by what it helps agents recall, what it makes extractable, and what it can truly erase.
