---
title: "Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.11969
priority: medium
status: unread
interest: medium
next_step: skim
---
# Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection
> 原文: [https://arxiv.org/abs/2607.11969](https://arxiv.org/abs/2607.11969)

arXiv:2607.11969v1 Announce Type: new
Abstract: Point-adjustment (PA), long the default scoring protocol in time-series anomaly detection (TSAD), was shown by Kim et al. (2022) to award near-perfect F1 to random scores. The field migrated to replacement metrics: PA%K, range-based precision/recall, affiliation precision/recall, and Volume-Under-the-Surface (VUS) ROC/PR. But did the fix work? Every robustness check to date is proposer-run or theoretical; no independent, adversarial, SOTA-relative audit on real benchmarks exists. We provide one. We stress-test 12 adopted metrics against trivial and adversarial no-skill score generators on the 250-series UCR Anomaly Archive (primary) plus five further benchmarks (SMD, SMAP, MSL, NAB, PSM), under a pre-registered SOTA-relative gameability criterion (a metric is gamed on a series if a no-skill generator reaches >=90% of the best real detector's score). The fix is only partial: affiliation-F1 (gamed on 99% of series) and every ROC-based metric tested (all roughly 62-64%) are gamed by no-skill detectors, genuinely so (real detectors score 0.97-1.00 on the very series they game), while the PR-based metrics and PA%K resist (14-18%). A decisive, one-directional McNemar split: VUS-ROC is gamed on 119 series where its sibling VUS-PR is not, and the reverse on none. The ROC-over-PR direction replicates across all five further benchmarks and never reverses, but the absolute gameability rate is benchmark-dependent and no single metric stays safe on all six (even VUS-PR is gamed on NAB). We release a pip-installable stress-test harness with all metric implementations vendored at frozen commits, plus a metric-selection decision protocol: prefer a PR-based metric or PA%K, treat affiliation-F1 and the ROC-AUC variants as gameable, and verify per benchmark rather than assuming robustness.
