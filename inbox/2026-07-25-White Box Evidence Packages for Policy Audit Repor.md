---
title: "White Box Evidence Packages for Policy Audit Reports"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2607.21462
priority: medium
status: unread
interest: medium
next_step: skim
---
# White Box Evidence Packages for Policy Audit Reports
> 原文: [https://arxiv.org/abs/2607.21462](https://arxiv.org/abs/2607.21462)

arXiv:2607.21462v1 Announce Type: new
Abstract: As AI governance moves from benchmark scores toward auditable oversight, a central question is how reviewers can tell whether an LLM-generated audit report is actually supported by evidence. This paper studies that question in passage-anchored policy audits, where a report must interpret a given policy passage and cite evidence for its claims. We introduce a controlled evaluation framework that holds the passage, rubric, and auditor model fixed while changing only the evidence interface supplied to the auditor. Across 60 AGORA policy cases, we generate 600 structured reports under ten evidence conditions, including passage-based evidence, internal model evidence, a hybrid package, and a shuffled control that preserves evidence format while breaking case relevance. Five human reviewers evaluate the primary interfaces for correctness, passage grounding, diagnostic usefulness, and evidence misuse. The results show that internal evidence changes how reports cite and reason about evidence, but more internal citations do not by themselves make a report more valid. A white-box diagnostic explains the failure mode: causal localization is narrow, while reports readily reuse broader readable labels and token directions. The hybrid interface is the most useful on average, while the shuffled control exposes a key governance risk: reports can sound substantively plausible while citing irrelevant internal evidence. This study reframes internal model access as an evidence design problem for audit workflows, rather than as a guarantee of transparency.
