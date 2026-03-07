---
title: "Decorrelating the Future: Joint Frequency Domain Learning for Spatio-temporal Forecasting"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.04418
priority: high
status: unread
---
# Decorrelating the Future: Joint Frequency Domain Learning for Spatio-temporal Forecasting
> 原文: [https://arxiv.org/abs/2603.04418](https://arxiv.org/abs/2603.04418)

arXiv:2603.04418v1 Announce Type: new
Abstract: Standard direct forecasting models typically rely on point-wise objectives such as Mean Squared Error, which fail to capture the complex spatio-temporal dependencies inherent in graph-structured signals. While recent frequency-domain approaches such as FreDF mitigate temporal autocorrelation, they often overlook spatial and cross spatio-temporal interactions. To address this limitation, we propose FreST Loss, a frequency-enhanced spatio-temporal training objective that extends supervision to the joint spatio-temporal spectrum. By leveraging the Joint Fourier Transform (JFT), FreST Loss aligns model predictions with ground truth in a unified spectral domain, effectively decorrelating complex dependencies across both space and time. Theoretical analysis shows that this formulation reduces estimation bias associated with time-domain training objectives. Extensive experiments on six real-world datasets demonstrate that FreST Loss is model-agnostic and consistently improves state-of-the-art baselines by better capturing holistic spatio-temporal dynamics.
