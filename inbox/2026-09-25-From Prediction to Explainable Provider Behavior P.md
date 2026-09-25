---
interest: medium
link: https://arxiv.org/abs/2609.28477
next_step: skim
priority: medium
slack_ts: '1790310831.568049'
source: cs.CY - Computers and Society
status: unread
title: From Prediction to Explainable Provider Behavior Profiles for Fraud, Waste,
  and Abuse Review
---
# From Prediction to Explainable Provider Behavior Profiles for Fraud, Waste, and Abuse Review
> 原文: [https://arxiv.org/abs/2609.28477](https://arxiv.org/abs/2609.28477)

arXiv:2609.28477v1 Announce Type: new
Abstract: Claims data can show that provider behavior changed but cannot by itself explain why. FWA (fraud, waste, and abuse) review requires identifying material behavior, locating the codes and dollars driving it, and testing plausible explanations. A common alternative, predictive modeling, flags deviations from an expected-utilization forecast -- but a forecast has limited value unless it beats simple persistence and explains why a deviation matters. In our quarterly provider-procedure data, the latest observation captures most forecastable variation, and added model structure adds little accuracy. Residuals conflate growth, service-line shifts, code maintenance, and incomplete observation with potentially concerning behavior, making point forecasts incomplete.
We instead formulate provider review as a descriptive representation problem: billed revenue y = s \* p, where s measures provider scale and p describes procedure composition. The profile records scale history, effective-dated code lineage, clinical-family shares, first-use events, billing context, and Medicare-versus-client differences. An optional rank-32 nonnegative factorization of procedure co-occurrence adds a fixed semantic geometry for similarity and retrieval, surfacing evidence for review without inferring intent or adjudicating FWA.
In an eight-quarter proprietary Medicare Carrier+DME audit of 1.22 million providers, simple descriptions outperform complex forecasts: regularized AR(1) attains the lowest log MAE, while persistence attains the lowest dollar WAPE. The learned semantic dictionary raises recall at 10 from 35.9% to 44.7% and high-cost-rare recall at 50 from zero to 51.8%. A lineage-aware family profile stays compact and interpretable, correlating 0.790 with learned-state movement, supporting a layered architecture where transparent descriptions form the core and learned representations add optional context.
