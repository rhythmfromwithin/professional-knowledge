---
interest: medium
link: https://arxiv.org/abs/2610.08864
next_step: skim
priority: low
slack_ts: '1791610118.058949'
source: cs.CR - Cryptography and Security
status: unread
title: 'Adversarial RL for Port-Scan Evasion: Attacker Feature Visibility in Edge-Deployed
  IDS'
---
# Adversarial RL for Port-Scan Evasion: Attacker Feature Visibility in Edge-Deployed IDS
> 原文: [https://arxiv.org/abs/2610.08864](https://arxiv.org/abs/2610.08864)

arXiv:2610.08864v1 Announce Type: new
Abstract: Machine learning-based intrusion detection systems (IDS) are increasingly used in resource-constrained Internet of Things (IoT) environments, yet their robustness is often evaluated against static attacks rather than adversaries that adapt to detection feedback. This paper investigates adaptive port-scan evasion against ML-based IDS models deployed on a Raspberry Pi 3B+. We implement a live Zeek-based IDS pipeline with XGBoost, a multi-layer perceptron, and a 1D convolutional neural network trained on TON\_IoT telemetry, and use a Deep Q-Network (DQN) adversary to learn evasive combinations of probe timing, TCP flags, and payload size under black-box, gray-box, and white-box feature-visibility settings. Although the deployed IDS models detect conventional port scans at 91.1--99.8%, DQN final-50-episode evasion rates range from 61.9% to 98.3% across feature-visibility settings. Greater feature visibility does not monotonically improve evasion, and its effect is model-dependent: against XGBoost, the black-box agent achieves 92.9% evasion, compared with 61.9% and 76.9% for gray-box and white-box agents, respectively, whereas 1D-CNN is most vulnerable under white-box access at 98.1%. Because standard DQN can overestimate action values, we additionally spot-check representative conditions using Double DQN. The gray-box condition remains unstable in this check, providing no evidence that overestimation bias alone explains the observed instability. These results show that limited feature knowledge can still enable effective adaptive evasion against static edge-deployed IDS models, motivating more robust defenses for IoT edge environments.
