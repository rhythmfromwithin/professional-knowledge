---
interest: medium
link: https://arxiv.org/abs/2610.22705
next_step: skim
priority: low
slack_ts: '1792470516.187069'
source: cs.DB - Databases
status: unread
title: Data Provenance Aggregation and Structural Descriptors for Query-Template Identification
---
# Data Provenance Aggregation and Structural Descriptors for Query-Template Identification
> 原文: [https://arxiv.org/abs/2610.22705](https://arxiv.org/abs/2610.22705)

arXiv:2610.22705v1 Announce Type: new
Abstract: Runtime query similarity identification supports several activities, including workload analysis, identifying recurring behaviour, auditing, debugging, and anomaly detection. Existing methods for evaluating query similarity mostly rely on SQL text, execution plans, or result values but do not account for input data or how results are derived during query execution.
This paper proposes a novel approach using data provenance for query-template identification. We construct query-level profiles that capture explicit data dependencies, occurrence frequencies, and structural properties by aggregating tuple-level Lineage and Why-provenance across entire query results. We also derive Provenance Structural Descriptors (PSD), which summarise these profiles using a small set of numerical features.
We evaluate our proposals using these profiles to identify query templates over \(12{,}500\) distinct query instances generated from parametrised TPC-DS query templates. The experimental evaluation shows that query templates can be identified solely from their provenance footprints, and that accuracy improves as more historical data becomes available. It also shows that PSD achieve high classification accuracy with limited training history and low test-processing cost.
