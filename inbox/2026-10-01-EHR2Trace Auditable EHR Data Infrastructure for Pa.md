---
interest: medium
link: https://arxiv.org/abs/2609.38193
next_step: skim
priority: high
slack_ts: '1790832434.802359'
source: cs.LG - Machine Learning
status: unread
title: 'EHR2Trace: Auditable EHR Data Infrastructure for Patient World Models and
  Clinical Agents'
---
# EHR2Trace: Auditable EHR Data Infrastructure for Patient World Models and Clinical Agents
> 原文: [https://arxiv.org/abs/2609.38193](https://arxiv.org/abs/2609.38193)

arXiv:2609.38193v1 Announce Type: new
Abstract: Patient world models and clinical agents aim to predict changes in patients' health and support clinical work. Developing these systems requires reliable histories of patient conditions, treatments, and the information available at each decision. Electronic health records (EHRs) contain these histories, but differences in how events are recorded make them difficult to use consistently. We present EHR2Trace, a system that converts EHRs from different sources into traceable patient events for model training and evaluation. It links events to source records, separates event time from information availability, and distinguishes medication orders, dispensing, and administration. A shared event representation supports both OMOP and MEDS exports, with automated validation and reproducible builds. Across three clinical datasets, EHR2Trace converted 846.4 million events, with every applicable check passing except one unit-consistency check on MIMIC-IV, and detected all 28 injected faults. A controlled prediction experiment showed that assigning later diagnoses to admission time substantially inflated measured performance, and that a model trained on such data lost accuracy when deployed on histories filtered by availability. EHR2Trace provides a reusable data foundation for patient world models and clinical agents, helping researchers inspect patient histories, check conversion decisions, and evaluate models with explicit data rules.
