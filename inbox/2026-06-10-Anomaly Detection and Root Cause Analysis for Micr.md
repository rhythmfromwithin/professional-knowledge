---
interest: medium
link: https://arxiv.org/abs/2606.09942
next_step: skim
priority: low
slack_ts: '1781065399.464949'
source: cs.SE - Software Engineering
status: unread
title: Anomaly Detection and Root Cause Analysis for Microservice Systems
---
# Anomaly Detection and Root Cause Analysis for Microservice Systems
> 原文: [https://arxiv.org/abs/2606.09942](https://arxiv.org/abs/2606.09942)

arXiv:2606.09942v1 Announce Type: new
Abstract: Microservice systems are widely used to build cloud applications, yet their complexity makes failures inevitable, degrading user experience and causing economic loss. Automated anomaly detection and root cause analysis (RCA) are now active research areas, but existing techniques share five limitations. First, most treat anomaly detection and RCA separately, assuming anomalies are detected correctly, and falter when detection is imprecise due to noise or delay. Second, they focus on metrics, logs, and traces, leaving event data such as API calls and configuration changes underexplored. Third, many require a given service call graph and cannot diagnose without one. Fourth, the field lacks standardised datasets and evaluation frameworks, so methods are hard to compare fairly. Fifth, although causal inference-based RCA has become dominant, its effectiveness, efficiency, and robustness remain unclear.
This thesis addresses these limitations through two groups of contributions. The first introduces methods that exploit observability data both independently and collectively. BARO is an end-to-end anomaly detection and RCA approach for metric data. EventADL is an end-to-end framework for event data. TORAI is a multimodal RCA framework that requires no service call graph. Extensive experiments on real microservice systems demonstrate their effectiveness and robustness. The second group delivers benchmarking datasets, an evaluation framework, and systematic evaluation efforts. RCAEval is a comprehensive benchmark providing ready-to-use datasets and reproducible baselines for future research. A systematic evaluation of existing RCA methods, especially causal inference-based approaches, offers insights that guide future directions. This thesis thereby advances automated anomaly detection and RCA for microservice failures, enabling future research on incident mitigation and remediation.
