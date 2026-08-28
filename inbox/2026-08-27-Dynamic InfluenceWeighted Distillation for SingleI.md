---
interest: medium
link: https://arxiv.org/abs/2608.24904
next_step: skim
priority: high
slack_ts: '1787914962.883609'
source: cs.LG - Machine Learning
status: unread
title: Dynamic Influence-Weighted Distillation for Single-IMU Activity Recognition
---
# Dynamic Influence-Weighted Distillation for Single-IMU Activity Recognition
> 原文: [https://arxiv.org/abs/2608.24904](https://arxiv.org/abs/2608.24904)

arXiv:2608.24904v1 Announce Type: new
Abstract: Inertial sensors at multiple body locations can improve activity recognition, but requiring every sensor at inference increases the deployment burden. We study whether four synchronized IMUs available during training can improve a student that uses only the right-arm IMU during fitting and inference. A frozen four-IMU teacher provides logit and feature targets. Fixed-weight knowledge distillation applies each target with the same strength to every fitting sample, although the student may not benefit equally from them. We introduce dynamic influence weighting (DIW), which tests a one-step candidate update on separate fold-internal training participants. DIW then assigns separate sample-wise gates to the logit and feature losses. On WEAR, we evaluate 19 labels and 68,298 complete windows from 22 participants using subject-disjoint five-fold cross-validation. Pooled out-of-fold macro-F1 is 0.561820 for Supervised and 0.571623 for Fixed-weight KD. DIW reaches 0.638451, gains of 7.66 and 6.68 percentage points, respectively. It exceeds Supervised for 18 of 19 labels and 21 of 22 held-out participants. All three routes retain the same 80,915-parameter right-arm student at inference. Under this protocol, DIW converts training-only multi-position information into a stronger single-IMU model without changing deployed sensing or the student forward graph.
