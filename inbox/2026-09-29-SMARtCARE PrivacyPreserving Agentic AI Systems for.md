---
interest: medium
link: https://arxiv.org/abs/2609.31763
next_step: skim
priority: high
slack_ts: '1790832418.814359'
source: cs.AI - Artificial Intelligence
status: unread
title: 'SMARtCARE: Privacy-Preserving Agentic AI Systems for Bounded-Autonomy Clinical
  Decision Support'
---
# SMARtCARE: Privacy-Preserving Agentic AI Systems for Bounded-Autonomy Clinical Decision Support
> 原文: [https://arxiv.org/abs/2609.31763](https://arxiv.org/abs/2609.31763)

arXiv:2609.31763v1 Announce Type: new
Abstract: Long-context clinical AI systems can miss relevant patient history when prior admissions fall outside the active reasoning context. In ICU monitoring, this can cause early vital-sign drift to appear nonspecific even when it resembles a prior deterioration pattern. SMARtCARE addresses this gap through a four-state clinical decision-support architecture: Stable, Meta-cognitive, Assisted, and Regulated (Revoked). Rather than automatically retrieving prior records, SMARtCARE uses a lossy six-channel fingerprint of the patient's prior trajectory. When current drift matches that fingerprint and the prior record is absent from context, the system raises a Meta-cognitive escalation for clinician review; full retrieval occurs only through clinician action in the Assisted state. A patient-identity guard is designed to enforce correct attribution across data loading, logging, and audit layers. Evaluation combines a synthetic Monte Carlo study that validates the state-transition logic and estimator stability, not clinical performance, with real-data runs on both the MIMIC-III and MIMIC-IV Clinical Database Demos. On MIMIC-III, one prior-pattern recurrence was identified among 14 two-admission patients; on MIMIC-IV, the same pipeline produced no fingerprint matches among 9 two-admission patients, which illustrates a key limitation of a fixed canonical pattern library. Across both runs all logged decisions were fully traceable and correctly attributed. The results support SMARtCARE as a traceable, privacy-aware mechanism for surfacing middle-context risk; they are not a clinical efficacy claim.
