---
interest: medium
link: https://arxiv.org/abs/2604.22096
next_step: skim
priority: low
slack_ts: '1777434587.893119'
source: cs.CR - Cryptography and Security
status: unread
title: Who Audits the Auditor? Tamper-Proof Fraud Detection with Blockchain-Anchored
  Explainable ML
---
# Who Audits the Auditor? Tamper-Proof Fraud Detection with Blockchain-Anchored Explainable ML
> 原文: [https://arxiv.org/abs/2604.22096](https://arxiv.org/abs/2604.22096)

arXiv:2604.22096v1 Announce Type: new
Abstract: In enterprise fraud detection, model accuracy alone is insufficient when insiders can tamper with audit logs or bypass approval workflows. Real-world incidents show that fraud often persists not because detection algorithms fail, but because the audit trail itself is controllable by privileged operators. This exposes a fundamental trust gap: \*who audits the auditor?\*
We present a tamper-evident fraud detection system that anchors both ML predictions and workflow execution to an immutable blockchain ledger. Rather than using blockchain as passive storage, we enforce the entire approval process through smart contracts, ensuring that every transaction, prediction, and explanation is atomically recorded and cannot be retroactively modified. Our detection module achieves competitive accuracy (F1 = 0.895, PR-AUC = 0.974) while providing cryptographically verifiable decision trails that support regulatory auditability requirements (e.g., GDPR Article 22). System evaluation shows sub-25 ms inference latency and economically viable deployment on Layer-2 networks at under \$0.01 per transaction (validated against PolygonScan data), supporting enterprise-scale workloads of 10,000+ monthly payments.
