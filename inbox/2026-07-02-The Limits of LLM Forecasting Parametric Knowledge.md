---
interest: medium
link: https://arxiv.org/abs/2607.00018
next_step: skim
priority: medium
slack_ts: '1782965370.821439'
source: cs.CY - Computers and Society
status: unread
title: 'The Limits of LLM Forecasting: Parametric Knowledge Gaps Across Conflict Zones'
---
# The Limits of LLM Forecasting: Parametric Knowledge Gaps Across Conflict Zones
> 原文: [https://arxiv.org/abs/2607.00018](https://arxiv.org/abs/2607.00018)

arXiv:2607.00018v1 Announce Type: new
Abstract: Media coverage of armed conflict is deeply asymmetric: we document a 224$\times$ gap between the most and least covered conflict zones in English-language media across 22 countries (2020--2026). We evaluate zero-shot conflict escalation forecasting across all 22 countries on a 660-case held-out test set, comparing Llama-3.3-70B and GPT-4o against three structured baselines.
The central finding is not a performance gradient but a qualitative failure: LLMs do not forecast conflict -- they categorize it. Llama predicts escalation on every under-covered case, matching the trivial Always-YES baseline to three decimals; GPT-4o predicts NO on every over-covered case, missing all five actual escalation events. A logistic regression using only eleven observation-window features with \emph{no country information} achieves F1~=~0.402, outperforming both LLMs in every measurable tier. This failure cannot be resolved at inference time: adding structured ACLED evidence degrades performance on under-covered zones (GPT-4o F1: 0.323~$\to$~0.168) and falls below LR by a factor of 2.4. The bottleneck is not data availability but the LLM's interpretation of temporal signal under a country-categorical prior.
Under-covered populations receive not just less accurate AI, but qualitatively different AI that cannot distinguish stable from escalating periods. We call for coverage-stratified benchmarking, conflict NLP datasets for under-covered zones, and training data documentation standards for geographic conflict representation.
