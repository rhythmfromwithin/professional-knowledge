---
interest: medium
link: https://arxiv.org/abs/2604.14233
next_step: skim
priority: low
slack_ts: '1776569841.268159'
source: cs.CR - Cryptography and Security
status: unread
title: 'Anomaly Detection in IEC-61850 GOOSE Networks: Evaluating Unsupervised and
  Temporal Learning for Real-Time Intrusion Detection'
---
# Anomaly Detection in IEC-61850 GOOSE Networks: Evaluating Unsupervised and Temporal Learning for Real-Time Intrusion Detection
> 原文: [https://arxiv.org/abs/2604.14233](https://arxiv.org/abs/2604.14233)

arXiv:2604.14233v1 Announce Type: new
Abstract: The IEC-61850 GOOSE protocol underpins time-critical communication in modern digital substations but lacks native security mechanisms, leaving it vulnerable to replay, masquerade, and data injection attacks. Intrusion detection in this setting is challenging due to strict latency constraints (sub-4ms) and limited availability of labeled attack data. This paper evaluates whether unsupervised temporal modeling can provide effective and deployable anomaly detection for GOOSE networks. Five models are compared on the ERENO IEC-61850 dataset: a supervised Random Forest baseline, a feedforward Autoencoder, and three recurrent sequence autoencoders (RNN, LSTM, and GRU). The supervised Random Forest achieves the highest detection performance (F1=0.9516) but fails to meet real-time constraints at 21.8ms per prediction. All four unsupervised models satisfy the 4ms requirement, with the GRU achieving the best accuracy to latency tradeoff among them (F1=0.8737 at 1.118ms). A cross-environment evaluation on an independent dataset shows that all models degrade under distribution shift. However, recurrent models retain substantially higher relative performance than the supervised baseline, suggesting that temporal sequence modeling generalizes better than fitting labeled attack distributions. Anomaly thresholds for the unsupervised models are selected on a held out validation partition to avoid test set leakage. These results support unsupervised temporal models as a practical choice for real-time GOOSE intrusion detection, particularly in environments where labeled training data may be unavailable or where large-scale deployment across diverse substations is required.
