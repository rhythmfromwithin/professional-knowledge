---
interest: medium
link: https://arxiv.org/abs/2606.28377
next_step: skim
priority: medium
slack_ts: '1782792824.210259'
source: cs.CV - Computer Vision
status: unread
title: Memory-Augmented LSTM Autoencoder for Unsupervised Activity Recognition with
  IMU Sensor Fusion
---
# Memory-Augmented LSTM Autoencoder for Unsupervised Activity Recognition with IMU Sensor Fusion
> 原文: [https://arxiv.org/abs/2606.28377](https://arxiv.org/abs/2606.28377)

arXiv:2606.28377v1 Announce Type: new
Abstract: HAR using Inertial Measurement Unit (IMU) sensors is vital for healthcare monitoring and rehabilitation. Despite deep learning advancements, major challenges remain: reliance on labeled data, multi-sensor fusion complexity, and the limited ability of unsupervised methods to capture spatiotemporal dependencies. These issues are pronounced in real-world scenarios with noisy data, overlapping activities, and missing labels. We propose a fully unsupervised spatiotemporal feature fusion framework using a memory-augmented autoencoder. It enhances activity representations via short temporal windows of multi-sensor IMU data, enabling real-time applications. Our framework extracts hierarchical static features via a Stacked Autoencoder, fusing them within and across sensors. A sequence-to-sequence LSTM Autoencoder then temporally refines these features, incorporating historical motion patterns without labels. We analyze key hyperparameters to identify configurations that maximize feature separability under short-window constraints. Evaluated on DaLiAc and PAMAP2 using realistic inter-class window segmentation, our method achieves 96.6% and 98.4% accuracy, respectively, surpassing supervised baselines and unsupervised approaches. Our method improves feature separability by up to 9% despite shorter temporal windows. While our realistic inter-class segmentation reduces accuracy by ~7%, it was intentionally adopted to better reflect real-world activity transitions and practical relevance.
