---
interest: medium
link: https://arxiv.org/abs/2608.18296
next_step: skim
priority: medium
slack_ts: '1787276742.894289'
source: cs.CY - Computers and Society
status: unread
title: 'FairGlucose: A CGM Fairness Benchmark Reveals Subgroup Disparities Hidden
  in Population-Level Validation'
---
# FairGlucose: A CGM Fairness Benchmark Reveals Subgroup Disparities Hidden in Population-Level Validation
> 原文: [https://arxiv.org/abs/2608.18296](https://arxiv.org/abs/2608.18296)

arXiv:2608.18296v1 Announce Type: new
Abstract: As CGM-based AI tools approach clinical deployment, whether their accuracy is equitable across patient demographics remains insufficiently tested. To enable this evaluation, we constructed FairGlucose, a 300-patient CGM cohort balanced across 12 demographic strata (age x gender x type 1/type 2 diabetes), with 132,480 forecasting samples and 3,945 unique behavioral events (meals, exercise, medication) logged by 81 patients. Benchmarking 33 models across four families on 2-hour glucose forecasting, we find that population-level external validation can conceal substantial subgroup disparities. Aggregate out-of-distribution metrics appear stable (approximately 1.0), yet subgroup-level ratios range from 0.8 to 1.4, with T1D patients showing 6 mg/dL higher prediction error than T2D (p < 0.001). This disparity persists across all 33 models, suggesting a property of the prediction task rather than any single architecture. Further analysis shows that subgroup performance gaps align with the proportion of clinically hard cases, and that input-length sensitivity varies across demographics, motivating personalized configurations. Frontier LLMs underperform specialized neural models by 1-6 mg/dL; behavioral events contribute negligibly (approximately 0.1 mg/dL) even under oracle event access. These findings establish that population-level validation alone is insufficient for equity assessment of digital health AI, motivating subgroup-disaggregated reporting as a default standard.
