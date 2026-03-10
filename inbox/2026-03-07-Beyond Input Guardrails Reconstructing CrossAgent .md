---
interest: medium
link: https://arxiv.org/abs/2603.04469
next_step: skim
priority: low
slack_ts: '1773132474.475649'
source: cs.CR - Cryptography and Security
status: unread
title: 'Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware
  Attack Detection'
---
# Beyond Input Guardrails: Reconstructing Cross-Agent Semantic Flows for Execution-Aware Attack Detection
> 原文: [https://arxiv.org/abs/2603.04469](https://arxiv.org/abs/2603.04469)

arXiv:2603.04469v1 Announce Type: new
Abstract: Multi-Agent System is emerging as the \textit{de facto} standard for complex task orchestration. However, its reliance on autonomous execution and unstructured inter-agent communication introduces severe risks, such as indirect prompt injection, that easily circumvent conventional input guardrails. To address this, we propose \SysName, a framework that shifts the defensive paradigm from static input filtering to execution-aware analysis. By extracting and reconstructing Cross-Agent Semantic Flows, \SysName synthesizes fragmented operational primitives into contiguous behavioral trajectories, enabling a holistic view of system activity. We leverage a Supervisor LLM to scrutinize these trajectories, identifying anomalies across data flow violations, control flow deviations, and intent inconsistencies. Empirical evaluations demonstrate that \SysName effectively detects over ten distinct compound attack vectors, achieving F1-scores of 85.3\% and 66.7\% for node-level and path-level end-to-end attack detection, respectively. The source code is available at https://anonymous.4open.science/r/MAScope-71DC.
