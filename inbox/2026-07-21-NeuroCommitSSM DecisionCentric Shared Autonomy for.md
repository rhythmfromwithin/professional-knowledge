---
interest: medium
link: https://arxiv.org/abs/2607.15395
next_step: skim
priority: medium
slack_ts: '1784690754.405859'
source: cs.RO - Robotics
status: unread
title: 'NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation
  via EEG-EMG-ET Commit Readiness'
---
# NeuroCommitSSM: Decision-Centric Shared Autonomy for Safe Assistive Manipulation via EEG-EMG-ET Commit Readiness
> 原文: [https://arxiv.org/abs/2607.15395](https://arxiv.org/abs/2607.15395)

arXiv:2607.15395v1 Announce Type: new
Abstract: We present NeuroCommitSSM, a decision-centric framework that models when to execute, not just what to do, for safe commit-to-execute control in assistive robotic manipulation. NeuroCommitSSM predicts a continuous commit-readiness score c\_t in [0,1] from synchronized electroencephalography (EEG), electromyography (EMG), and eye-tracking (ET), and converts it into discrete commit events through dwell and hysteresis filtering. A three-state finite-state supervisor, HOLD-ASSIST-COMMIT (HAC), gates execution by requiring both a sustained commit-readiness signal from the neural model and real-time perception and robot-state feasibility, including target visibility, inverse kinematics solvability, and collision-free planning, before initiating motion. We evaluate the framework on N=32 subjects performing five activities of daily living (ADL) tasks aligned with the International Classification of Functioning, Disability and Health (ICF), using leave-one-subject-out (LOSO) cross-validation and seven sensor-dropout scenarios (S0-S6). NeuroCommitSSM achieves 0.950 action-balanced accuracy with 0.75 false commit events per 1000 REST windows (FP/1k REST), and maintains low false commits and stable state transitions under sensor loss. For example, in the EEG-only condition, it achieves 0.785 balanced accuracy and 0.29 FP/1k REST, whereas the Temporal Convolutional Network baseline produces 99.95 FP/1k REST under the same condition. Hardware-in-the-loop (HIL) validation on a Kinova Gen3 arm shows that feasibility-checked execution reduces false starts and decision instability without sacrificing task success. Supplementary materials, including code, datasets, videos, and additional analyses, are available at https://madibabaiasl.github.io/NeuroCommitSSM/.
