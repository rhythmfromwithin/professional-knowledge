---
interest: medium
link: https://arxiv.org/abs/2606.06089
next_step: skim
priority: low
slack_ts: '1780718915.947949'
source: econ.GN - General Economics (AI Economics)
status: unread
title: Leveraging LLMs for Unstructured Claims Data Analysis
---
# Leveraging LLMs for Unstructured Claims Data Analysis
> 原文: [https://arxiv.org/abs/2606.06089](https://arxiv.org/abs/2606.06089)

arXiv:2606.06089v1 Announce Type: cross
Abstract: Actuaries rely primarily on structured numerical data for reserving and ratemaking, while valuable predictive information in unstructured text including medical records, adjuster notes, and call transcripts remains largely unused. Manual processing of these documents is time-consuming, inconsistent across reviewers, and unscalable. We present a proof-of-concept framework using large language models (LLMs) to extract structured actuarial variables from unstructured claims data.
We implement a two-stage processing architecture separating document-level extraction (Stage 1) from claim-level synthesis (Stage 2). A modular four-script Python pipeline processes synthetic FHIR-based claims data and real claims documents, extracting 36 actuarial variables across reserving, ratemaking, and claims management categories. We validate 14 core variables using two independent clinical expert reviewers scoring 20 synthetic claims on a five-point Likert rubric, achieving mean scores above 4.0 and a weighted kappa of 0.53. Integration with chain ladder reserving demonstrates practical actuarial value: severity-segmented analysis reduced reserve estimation error from 6.5% to 4.0%. The open-source implementation includes audit trails and confidence scoring, providing a replicable foundation for LLM-based actuarial variable extraction in property-casualty insurance.
