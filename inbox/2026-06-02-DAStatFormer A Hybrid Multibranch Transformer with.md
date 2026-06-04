---
interest: medium
link: https://arxiv.org/abs/2606.00081
next_step: skim
priority: high
slack_ts: '1780548653.092199'
source: cs.LG - Machine Learning
status: unread
title: 'DAStatFormer: A Hybrid Multibranch Transformer with Statistical Feature Integration
  for DAS-Based Pattern Recognitions'
---
# DAStatFormer: A Hybrid Multibranch Transformer with Statistical Feature Integration for DAS-Based Pattern Recognitions
> 原文: [https://arxiv.org/abs/2606.00081](https://arxiv.org/abs/2606.00081)

arXiv:2606.00081v1 Announce Type: new
Abstract: Distributed Acoustic Sensing (DAS) enables large-scale monitoring through optical fibers, but its high dimensionality and complex spatio-temporal patterns make event classification demanding. Existing deep learning approaches-CNNs, recurrent models, and Transformer variants-either fail to capture long-range dependencies or require processing raw DAS matrices at prohibitive cost. We propose DAStatFormer, a hybrid multibranch Transformer that combines compact multidomain statistical features with Gated Transformer Networks. Instead of raw signals, we extract 24 ANOVA-selected attributes per channel from the temporal, waveform, and spectral domains, reducing data size by orders of magnitude while preserving discriminative information. Each domain is processed via dedicated step-wise and channel-wise attention branches, fused by an adaptive gating mechanism. Experiments on the open $\Phi$-OTDR benchmark and a real-scenario DAS dataset show that DAS-tatFormer achieves up to 99.4% accuracy and near-perfect real-world performance, while using significantly fewer parameters and lower inference cost than models such as DASFormer and DeepViT. These results demonstrate its suitability for scalable, real-time DAS-based monitoring. We release our code at https://github.com/MichelD-git/DAStatFormer
