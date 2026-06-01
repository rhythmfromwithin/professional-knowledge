---
title: "Gait2Hip-60: A Unified Deep Learning Benchmark for Predicting Hip Muscle Forces and Joint Moments from Multi-Cadence Gait Kinematics"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.30374
priority: high
status: unread
interest: medium
next_step: skim
---
# Gait2Hip-60: A Unified Deep Learning Benchmark for Predicting Hip Muscle Forces and Joint Moments from Multi-Cadence Gait Kinematics
> 原文: [https://arxiv.org/abs/2605.30374](https://arxiv.org/abs/2605.30374)

arXiv:2605.30374v1 Announce Type: new
Abstract: Estimating hip muscle forces and joint moments during gait typically relies on musculoskeletal simulation, which is informative but time-consuming and difficult to apply in clinical settings. This study developed a deep learning framework to predict these hip dynamics parameters directly from lower-limb gait kinematics and compared three representative sequence models under a unified protocol. Gait data were collected from 60 healthy adults under three metronome-guided cadence conditions. Ten bilateral lower-limb joint angles were used as inputs, and OpenSim-derived hip muscle forces and hip joint moments were used as reference outputs. Three deep learning models of LSTM, Transformer, and Mamba were trained and evaluated using the same subject-level split, preprocessing pipeline, and metrics. The best model was then directly tested on an external cohort of 9 patients with osteonecrosis of the femoral head (ONFH) without retraining. In the healthy-subject benchmark, Transformer achieved the best subject-level mean performance for both hip muscle force prediction (RMSE = 1.33 N/kg, MAE = 0.57 N/kg, R2 = 0.819) and hip joint moment prediction (RMSE = 0.11 Nm/kg, MAE = 0.07 Nm/kg, R2 = 0.862), with similar advantages across walking cadences. In zero-shot external validation, Transformer retained moderate predictive ability in ONFH for hip muscle force prediction (RMSE = 1.51 N/kg, MAE = 0.70 N/kg, R2 = 0.537) and hip joint moment prediction (RMSE = 0.17 Nm/kg, MAE = 0.12 Nm/kg, R2 = 0.569). These findings support the feasibility of estimating hip dynamics from gait kinematics, identify Transformer as a strong baseline, and highlight the need for broader pathological validation and improved generalization before clinical application.
