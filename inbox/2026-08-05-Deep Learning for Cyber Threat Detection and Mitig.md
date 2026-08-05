---
title: "Deep Learning for Cyber Threat Detection and Mitigation in Healthcare-IoT"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.00118
priority: low
status: unread
interest: medium
next_step: skim
---
# Deep Learning for Cyber Threat Detection and Mitigation in Healthcare-IoT
> 原文: [https://arxiv.org/abs/2608.00118](https://arxiv.org/abs/2608.00118)

arXiv:2608.00118v1 Announce Type: new
Abstract: Cybersecurity is a fundamental requirement for protecting wearable devices used in healthcare Internet of Things (H-IoT) systems. Security failures in these resource-constrained systems directly compromise patient safety. Physiological data and network traffic are frequent targets of cyberattacks in H-IoT environments. To address these risks, deep learning-based cybersecurity mechanisms for H-IoT often involve complex architectures with large parameter counts. Existing datasets are also rarely assessed for quality, limiting their applicability. However, this research addresses these challenges by developing multiple realistic datasets and proposing lightweight deep learning models, namely the Temporal Convolutional Network (TCN) and Residual TCN (Res-TCN), for H-IoT. It includes two binary classification datasets for Distributed Denial of Service (DDoS) attacks and a multiclass dataset representing Selective Forwarding (SF), Man-in-the-Middle (MITM), and DDoS attacks. The datasets UL-ECE-MQTT-DDoS-H-IoT2025 and UL-ECE-UDP-DDoS-H-IoT2025 are generated in Cooja and ns-3 to capture transmission behaviours and protocol variations. The third dataset, UL-ECE-MultiAttack-H-IoT2025, integrates physiological and network features to represent multiple cyber threats in H-IoT. Building on this, the TCN model is designed to detect and mitigate DDoS attacks over the MQTT and UDP-based datasets. It incorporates a monitoring frequency-based detection mechanism and a dynamic threshold-based mitigation strategy. To enable edge deployment, the model is quantised and converted into TensorFlow Lite (TFLite) for real-time DDoS detection on Raspberry Pi 4, achieving low latency and power-efficient operation in H-IoT. This thesis establishes a deep learning-based cybersecurity defence mechanism encompassing realistic dataset generation, lightweight model design, and edge deployment for securing H-IoT systems.
