---
title: "A Design Space for Data Agents: Insights from KDD Cup 2026"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.28970
priority: low
status: unread
interest: medium
next_step: skim
---
# A Design Space for Data Agents: Insights from KDD Cup 2026
> 原文: [https://arxiv.org/abs/2611.28970](https://arxiv.org/abs/2611.28970)

arXiv:2611.28970v1 Announce Type: new
Abstract: Data agents interpret analytical requests, gather evidence from heterogeneous sources, and compute results within finite resource budgets. We analyze the final code submissions of the ten highest-ranked teams in the KDD Cup 2026 Data Agents for Complex Data Analysis competition. We organize the observed design choices into three interacting layers, covering workflow orchestration, analytical functions, and working state. The comparison reveals recurring patterns for allocating computation in response to task progress, structuring evidence for computation and assessment, and preserving reusable artifacts with their provenance. Candidates that rely on the same evidence can inherit the same error, so interpreting their agreement requires tracing those dependencies. The design space motivates controlled evaluations of how resource allocation, evidence sharing, and targeted recovery affect task completion and correctness.
