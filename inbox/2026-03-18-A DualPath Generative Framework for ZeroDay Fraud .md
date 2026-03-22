---
interest: medium
link: https://arxiv.org/abs/2603.13237
next_step: skim
priority: high
slack_ts: '1774148044.543799'
source: cs.AI - Artificial Intelligence
status: unread
title: A Dual-Path Generative Framework for Zero-Day Fraud Detection in Banking Systems
---
# A Dual-Path Generative Framework for Zero-Day Fraud Detection in Banking Systems
> 原文: [https://arxiv.org/abs/2603.13237](https://arxiv.org/abs/2603.13237)

arXiv:2603.13237v1 Announce Type: new
Abstract: High-frequency banking environments face a critical trade-off between low-latency fraud detection and the regulatory explainability demanded by GDPR. Traditional rule-based and discriminative models struggle with "zero-day" attacks due to extreme class imbalance and the lack of historical precedents. This paper proposes a Dual-Path Generative Framework that decouples real-time anomaly detection from offline adversarial training. The architecture employs a Variational Autoencoder (VAE) to establish a legitimate transaction manifold based on reconstruction error, ensuring <50ms inference latency. In parallel, an asynchronous Wasserstein GAN with Gradient Penalty (WGAN-GP) synthesizes high-entropy fraudulent scenarios to stress-test the detection boundaries. Crucially, to address the non-differentiability of discrete banking data (e.g., Merchant Category Codes), we integrate a Gumbel-Softmax estimator. Furthermore, we introduce a trigger-based explainability mechanism where SHAP (Shapley Additive Explanations) is activated only for high-uncertainty transactions, reconciling the computational cost of XAI with real-time throughput requirements.
