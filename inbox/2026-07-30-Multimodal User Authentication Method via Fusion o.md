---
interest: medium
link: https://arxiv.org/abs/2607.24747
next_step: skim
priority: low
slack_ts: '1785555369.014869'
source: cs.CR - Cryptography and Security
status: unread
title: Multimodal User Authentication Method via Fusion of Keystroke Dynamics and
  Glove-Based Hand Kinematics
---
# Multimodal User Authentication Method via Fusion of Keystroke Dynamics and Glove-Based Hand Kinematics
> 原文: [https://arxiv.org/abs/2607.24747](https://arxiv.org/abs/2607.24747)

arXiv:2607.24747v1 Announce Type: new
Abstract: Although keystroke dynamics are cost-effective behavioral biometrics, their practical deployment is hindered by susceptibility to environmental variations. To address this, we propose a robust multimodal authentication framework that augments traditional keystroke dynamics using 19-dimensional hand kinematics. Features are captured using a bespoke data glove equipped with 10 piezoresistive pressure sensors and a 9-axis IMU. A hybrid CNN-LSTM architecture effectively fuses these heterogeneous time-series streams. To ensure real-world applicability, we implemented a rigorous "unseen" evaluation protocol: the model was trained on a desktop keyboard using data from 1 target user and 8 "known" impostors, but evaluated on a laptop keyboard (cross-domain) against the target and an "unknown" impostor excluded from training. Averaged over five trials, the multimodal method achieved a mean Equal Error Rate (EER) of 2.12% for individual 600-ms authentication events (Window 1). Crucially, aggregating scores over 10 events (6 seconds) using a temporal smoothing window yielded perfect authentication (0.00% EER). While our ablation study showed IMU kinematics alone achieved equivalent performance in a static laboratory, error analysis confirmed that pressure and IMU sensors, despite strong physical correlation, possess distinct sensitivities to error factors. Fusing these modalities establishes a vital fail-safe against real-world vulnerabilities like spatial spoofing and environmental noise, highlighting that combined physical traits provide much stronger biometric discrimination than timing features alone.
