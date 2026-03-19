---
interest: medium
link: https://arxiv.org/abs/2603.12450
next_step: skim
priority: low
slack_ts: '1773888827.515879'
source: cs.CR - Cryptography and Security
status: unread
title: 'Bridging the Gap Between Security Metrics and Key Risk Indicators: An Empirical
  Framework for Vulnerability Prioritization'
---
# Bridging the Gap Between Security Metrics and Key Risk Indicators: An Empirical Framework for Vulnerability Prioritization
> 原文: [https://arxiv.org/abs/2603.12450](https://arxiv.org/abs/2603.12450)

arXiv:2603.12450v1 Announce Type: new
Abstract: Organisations overwhelmingly prioritize vulnerability remediation using Common Vulnerability Scoring System (CVSS) severity scores, yet CVSS classifiers achieve an Area Under the Precision-Recall Curve (AUPRC) of 0.011 on real-world exploitation data, near random chance. We propose a composite Key Risk Indicator grounded in expected-loss decomposition, integrating dimensions of threat, impact, and exposure. We evaluated the KRI framework against the Known Exploited Vulnerabilities (KEV) catalog using a comprehensive dataset of 280,694 Common Vulnerabilities and Exposures (CVEs). KRI achieves Receiver Operating Characteristic Area Under the Curve (ROC-AUC) 0.927 and AUPRC 0.223 versus 0.747 and 0.011 for CVSS (24 percents, 20). Ablation analysis shows Exploit Prediction Scoring System (EPSS) alone achieves AUPRC 0.365, higher than full KRI (0.223), confirming that EPSS and KRI serve distinct objectives: EPSS maximizes raw exploit detection, while KRI re-orders by impact and exposure, capturing 92.3 percents of impact-weighted remediation value at k=500 versus 82.6 percents for EPSS, and surfacing 1.75 more Critical-severity exploited CVEs. KRI's net benefit exceeds EPSS whenever the severity premium exceeds 2. While EPSS serves as a robust baseline for exploit detection, the KRI framework is the superior choice for organizations seeking to align remediation efforts with tangible risk reduction.
