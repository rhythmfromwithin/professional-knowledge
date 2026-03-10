---
title: "Learning Under Extreme Data Scarcity: Subject-Level Evaluation of Lightweight CNNs for fMRI-Based Prodromal Parkinsons Detection"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.00060
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning Under Extreme Data Scarcity: Subject-Level Evaluation of Lightweight CNNs for fMRI-Based Prodromal Parkinsons Detection
> 原文: [https://arxiv.org/abs/2603.00060](https://arxiv.org/abs/2603.00060)

arXiv:2603.00060v1 Announce Type: new
Abstract: Deep learning is often applied in settings where data are limited, correlated, and difficult to obtain, yet evaluation practices do not always reflect these constraints. Neuroimaging for prodromal Parkinsons disease is one such case, where subject numbers are small and individual scans produce many highly related samples. This work examines prodromal Parkinsons detection from resting-state fMRI as a machine learning problem centered on learning under extreme data scarcity.
Using fMRI data from 40 subjects, including 20 prodromal Parkinsons cases and 20 healthy controls, ImageNet-pretrained convolutional neural networks are fine-tuned and evaluated under two different data partitioning strategies. Results show that commonly used image-level splits allow slices from the same subject to appear in both training and test sets, leading to severe information leakage and near-perfect accuracy. When a strict subject-level split is enforced, performance drops substantially, yielding test accuracies between 60 and 81 percent.
Models with different capacity profiles are compared, including VGG19, Inception V3, Inception ResNet V2, and the lightweight MobileNet V1. Under subject-level evaluation, MobileNet demonstrates the most reliable generalization, outperforming deeper architectures despite having significantly fewer parameters. These results indicate that in extreme low-data regimes, evaluation strategy and model capacity have a greater impact on performance than architectural depth. Although the analysis is limited to a single cohort of 40 subjects and does not include external validation or cross-validation, it provides a concrete case study and practical recommendations for evaluating deep learning models under severe data scarcity.
