---
interest: medium
link: https://arxiv.org/abs/2608.26169
next_step: skim
priority: medium
slack_ts: '1788066032.426599'
source: cs.CY - Computers and Society
status: unread
title: Revision-Aware Success Prediction from Multi-Attempt Programming Trajectories
---
# Revision-Aware Success Prediction from Multi-Attempt Programming Trajectories
> 原文: [https://arxiv.org/abs/2608.26169](https://arxiv.org/abs/2608.26169)

arXiv:2608.26169v1 Announce Type: new
Abstract: Programming outcome prediction plays a central role in data-driven programming education, supporting learner modeling, timely intervention, and adaptive assistance. Yet predicting submission success is difficult due to heterogeneous error states, short-term revisions, and uneven future-horizon availability in programming trajectories. This study examines three prediction tasks under a unified formulation: whether the current attempt is accepted (Task~1), whether the next attempt is accepted (Task~2), and whether acceptance is reached within a three-attempt recovery window (Task~3). Each task is evaluated across current-only, pairwise, and multi-step input regimes using ML, DL, and transformer-based pretrained models (PTM), represented by LinearSVM, XGBoost, BiGRU, BiLSTM, GraphCodeBERT, and CodeT5+. Results show a consistent pattern: the current-only regime is the most reliable, while pairwise and multi-step history provide no consistent gain. ML models are the strongest and most stable overall, particularly in Tasks~1 and~3, and Task~2 is the hardest across all model families. DL and PTMs perform well on Task~3 but are more task-dependent. In the Task~3 current-only setting, XGBoost achieves AP/PR-AUC of 99.09% and MCC of 0.6325, while GraphCodeBERT and CodeT5+ reach F1 scores of 80.00% and 73.68%, respectively. A sensitivity analysis confirms that Task~3 conclusions hold most robustly for ML models under stricter future-horizon control. Across all settings, ML models remain highly effective for programming success prediction, while complex models offer value in specific settings. This work provides a systematic comparison across predictive formulations and offers robust modeling guidance for submission-aware analytics in programming education, where near-future success prediction can inform timely intervention in online judge platforms and adaptive programming support systems.
