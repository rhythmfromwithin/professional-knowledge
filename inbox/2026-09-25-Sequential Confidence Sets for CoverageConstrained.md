---
interest: medium
link: https://arxiv.org/abs/2609.28522
next_step: skim
priority: medium
slack_ts: '1790397483.885599'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Sequential Confidence Sets for Coverage-Constrained Conformal Model Selection
---
# Sequential Confidence Sets for Coverage-Constrained Conformal Model Selection
> 原文: [https://arxiv.org/abs/2609.28522](https://arxiv.org/abs/2609.28522)

arXiv:2609.28522v1 Announce Type: new
Abstract: Modern conformal forecasting systems often maintain several adaptive pipelines that differ in base forecasters, conformity scores, calibration windows, and update rules. Comparing them is difficult because coverage is a hard constraint, whereas efficiency should be optimized only among feasible pipelines. We formulate this problem as sequential inference for a stochastic constrained argmin. At each time, the target is the set of minimum-cost pipelines satisfying multiple prefix-average conditional miscoverage constraints. We introduce Coverage-Constrained Sequential Model Confidence Sets (CC-SMCS), which separate certifiably feasible, possibly feasible, and possibly constrained-optimal pipelines. Using simultaneous martingale confidence sequences, CC-SMCS projects a rectangular confidence region onto the constrained argmin and admits an exact closed-form rule. With probability at least $1-\delta$, it contains every constrained-optimal pipeline simultaneously over all times. This finite-sample guarantee requires no stationarity or mixing assumptions and remains valid under data-dependent stopping. We also establish an impossibility result for safe certification at the coverage boundary and extend the construction to delayed multi-horizon feedback and outcome-dependent efficiency objectives.
