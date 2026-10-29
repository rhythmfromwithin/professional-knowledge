---
interest: medium
link: https://arxiv.org/abs/2610.33108
next_step: skim
priority: low
slack_ts: '1793251499.380439'
source: cs.SE - Software Engineering
status: unread
title: 'ToolContractGate: Versioned Trusted Contracts for Drift-Safe Agent Tool Invocation'
---
# ToolContractGate: Versioned Trusted Contracts for Drift-Safe Agent Tool Invocation
> 原文: [https://arxiv.org/abs/2610.33108](https://arxiv.org/abs/2610.33108)

arXiv:2610.33108v1 Announce Type: new
Abstract: Agent tool approval and input validation do not, by themselves, bind a request to an approved source artifact. ToolContractGate provides a deterministic runtime contract evaluator for OpenAPI-derived agent tools. Each versioned ToolContract combines a stored OpenAPI fingerprint with access, schema, and behavioral declarations. The full evaluator applies ten checks, including a cached boot-time provenance result; four execution modes and five evaluation configurations support baseline, ablation, and non-blocking shadow analysis. On a synthetic benchmark of 45 cases (35 unsafe cases across 12 drift classes and 10 safe cases), the full pipeline detects all 35 faults: 29 BLOCK, 3 REVIEW, and 3 WARN decisions, with no false blocks on the safe cases. The archived run reports a mean gate latency of 0.18 ms and a 95th percentile (p95) of 2 ms using integer-millisecond measurements. The open-source artifact includes seven OpenAPI specifications, twelve enterprise contracts, 29 unit tests, and a 900-record evaluation. Results characterize contract-decision coverage; downstream enforcement requires a host that honors the returned decision. Production traffic, semantic backend drift, and dynamic provenance refresh remain evaluation and integration opportunities.
