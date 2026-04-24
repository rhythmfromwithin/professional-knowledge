---
interest: medium
link: https://arxiv.org/abs/2604.18611
next_step: skim
priority: low
slack_ts: '1777001711.139059'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Neuromorphic Continual Learning for Sequential Deployment of Nuclear Plant
  Monitoring Systems
---
# Neuromorphic Continual Learning for Sequential Deployment of Nuclear Plant Monitoring Systems
> 原文: [https://arxiv.org/abs/2604.18611](https://arxiv.org/abs/2604.18611)

arXiv:2604.18611v1 Announce Type: new
Abstract: Anomaly detection in nuclear industrial control systems (ICS) requires continuous, energy-efficient monitoring across multiple subsystems that are often deployed at different stages of plant commissioning. When a conventional neural network is sequentially trained to monitor new subsystems, it catastrophically forgets previously learned anomaly patterns, a safety-critical failure mode. We present the first spiking neural network (SNN)-based anomaly detection system with continual learning for nuclear ICS, addressing both challenges simultaneously. Our approach introduces spike-encoded asynchronous sensor fusion, a delta-based encoding that converts heterogeneous sensor streams into sparse spike trains at rates dictated by each sensor's natural dynamics, achieving 92.7% input sparsity. We evaluate five continual learning strategies, including sequential fine-tuning, Elastic Weight Consolidation (EWC), Synaptic Intelligence (SI), experience replay, and a hybrid EWC+Replay approach, on the HAI 21.03 nuclear ICS security dataset across three sequentially deployed subsystems (boiler, turbine, water treatment). The hybrid EWC+Replay method achieves an average F1 score of 0.979 with near-zero average forgetting (AF = 0.000 single seed; 0.035 +/- 0.039 across three seeds), while requiring 12.6x fewer operations (an estimated 2.5x in energy based on published hardware specifications) than an equivalent artificial neural network. The system detects all tested attacks with a mean latency of 0.6 seconds. These results demonstrate that neuromorphic computing offers a viable path toward always-on, energy-efficient, and adaptable safety monitoring for next-generation nuclear facilities.
