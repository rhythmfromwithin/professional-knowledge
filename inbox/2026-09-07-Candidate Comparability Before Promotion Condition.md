---
interest: medium
link: https://arxiv.org/abs/2609.04388
next_step: skim
priority: low
slack_ts: '1788840717.987439'
source: cs.CR - Cryptography and Security
status: unread
title: 'Candidate Comparability Before Promotion: Conditional Validation in Adaptive
  Network Intrusion Detection'
---
# Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection
> 原文: [https://arxiv.org/abs/2609.04388](https://arxiv.org/abs/2609.04388)

arXiv:2609.04388v1 Announce Type: new
Abstract: Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent. Promotion is security-relevant because it changes the model responsible for subsequent attack detection, and evaluating it has a methodological problem: promotion conclusions may depend on how the challenger was constructed and on how much evidence supports it. We test that dependence on CICIDS2017, UNSW-NB15 and ToN-IoT with self-contained challenger pipelines, nested candidate-size controls, a common-harness comparison of nine update policies, and a final sensitivity confining every exact feature vector to one evaluation, training or probe role. Incumbent-owned frozen preprocessing amplified apparent promotion harm; with self-contained challenger pipelines the mean full-drift harm did not persist. Raising nominal candidate evidence from 512 to 2,000 samples per class improved promotion under pool-constructed progressive drift by +0.53, +1.67 and +0.38 balanced-accuracy points: positive and statistically resolved in all three benchmarks, but materially benchmark-dependent rather than homogeneous, and driven mainly by fewer false positives. Policy conclusions were partially robust: policy ordering changed with candidate comparability, no policy globally dominated, and earlier compatibility statements for a label-free estimator and a calibrated ensemble narrowed. Validation helped evidence-disadvantaged challengers but added no average benefit at parity. Thirteen replays on real, time-ordered traffic showed no net harm from always deploying. Challenger construction and evidence should be controlled, reported and interpreted explicitly when promotion is evaluated.
