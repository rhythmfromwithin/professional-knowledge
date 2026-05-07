---
title: "Decompose to Understand, Fuse to Detect: Frequency-Decoupled Anomaly Detection for Encrypted Network Traffic"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.02970
priority: low
status: unread
interest: medium
next_step: skim
---
# Decompose to Understand, Fuse to Detect: Frequency-Decoupled Anomaly Detection for Encrypted Network Traffic
> 原文: [https://arxiv.org/abs/2605.02970](https://arxiv.org/abs/2605.02970)

arXiv:2605.02970v1 Announce Type: new
Abstract: Network traffic anomaly detection represents a critical cybersecurity task, yet widespread encryption makes this task increasingly challenging. In response, image-based methods that model traffic as visual patterns have emerged as the dominant approach. However, this work pioneers the identification of a pervasive ``full-frequency'' characteristic and an associated limitation termed ``spectral mismatch'' within this paradigm. Specifically, while encrypted traffic exhibits prominent high-frequency components, mainstream reconstruction methods demonstrate an inherent bias toward learning low-frequency information. This fundamental mismatch results in incomplete representations that consequently degrade anomaly detection performance. To address this challenge, we propose FreeUp, a novel frequency-decoupled framework designed explicitly for encrypted traffic analysis. FreeUp decomposes traffic data into distinct low- and high-frequency bands, processing them through separate, dedicated branches along with a customized training strategy that ensures stable and independent frequency-specific learning. Furthermore, recognizing that simple reconstruction error proves inadequate for evaluating dual-branch architectures, we introduce an uncertainty-inspired fusion scoring mechanism. This mechanism quantifies the reconstruction uncertainty of the frequency-specific branches and dynamically integrates their outputs, yielding a more comprehensive and reliable anomaly score. Extensive experiments across multiple benchmarks demonstrate that FreeUp consistently outperforms state-of-the-art baselines. The code is available at https://github.com/ikun0124/FreeUp.
