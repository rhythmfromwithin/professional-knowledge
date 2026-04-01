---
title: "Boundary-aware Prototype-driven Adversarial Alignment for Cross-Corpus EEG Emotion Recognition"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.26713
priority: high
status: unread
interest: medium
next_step: skim
---
# Boundary-aware Prototype-driven Adversarial Alignment for Cross-Corpus EEG Emotion Recognition
> 原文: [https://arxiv.org/abs/2603.26713](https://arxiv.org/abs/2603.26713)

arXiv:2603.26713v1 Announce Type: new
Abstract: Electroencephalography (EEG)-based emotion recognition suffers from severe performance degradation when models are transferred across heterogeneous datasets due to physiological variability, experimental paradigm differences, and device inconsistencies. Existing domain adversarial methods primarily enforce global marginal alignment and often overlook class-conditional mismatch and decision boundary distortion, limiting cross-corpus generalization. In this work, we propose a unified Prototype-driven Adversarial Alignment (PAA) framework for cross-corpus EEG emotion recognition. The framework is progressively instantiated in three configurations: PAA-L, which performs prototype-guided local class-conditional alignment; PAA-C, which further incorporates contrastive semantic regularization to enhance intra-class compactness and inter-class separability; and PAA-M, the full boundary-aware configuration that integrates dual relation-aware classifiers within a three-stage adversarial optimization scheme to explicitly refine controversial samples near decision boundaries. By combining prototype-guided subdomain alignment, contrastive discriminative enhancement, and boundary-aware aggregation within a coherent adversarial architecture, the proposed framework reformulates emotion recognition as a relation-driven representation learning problem, reducing sensitivity to label noise and improving cross-domain stability. Extensive experiments on SEED, SEED-IV, and SEED-V demonstrate state-of-the-art performance under four cross-corpus evaluation protocols, with average improvements of 6.72\%, 5.59\%, 6.69\%, and 4.83\%, respectively. Furthermore, the proposed framework generalizes effectively to clinical depression identification scenarios, validating its robustness in real-world heterogeneous settings. The source code is available at \textit{https://github.com/WuCB-BCI/PAA}
