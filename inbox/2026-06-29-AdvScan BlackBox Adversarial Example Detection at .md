---
interest: medium
link: https://arxiv.org/abs/2606.27704
next_step: skim
priority: low
slack_ts: '1782708418.732569'
source: cs.CR - Cryptography and Security
status: unread
title: 'AdvScan: Black-Box Adversarial Example Detection at Runtime through Power
  Analysis'
---
# AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis
> 原文: [https://arxiv.org/abs/2606.27704](https://arxiv.org/abs/2606.27704)

arXiv:2606.27704v1 Announce Type: new
Abstract: TinyML models deployed on edge devices are increasingly adopted in safety/security-critical applications, making them a prime target for adversarial example (AE) attacks where inputs are modified to cause misclassifications. However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. To address these challenges, we propose AdvScan, a runtime power analysis-based methodology for AE detection that operates in a black-box scenario while inducing minimal latency. AdvScan is based on the observation that AEs produce anomalous neuron activations, which in turn generate distinctive power-consumption signatures. The algorithm initially constructs a baseline distribution of power signatures from known benign inputs; then, at runtime, it applies a one-sample t-test to determine whether a test input's power signature significantly deviates from this baseline, thereby detecting AEs. We evaluated AdvScan using three adversarial example generation algorithms: Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), and Carlini-Wagner (C&W), on three MLPerf Tiny benchmark models implemented on two target devices: the STM32F303RC (ARM Cortex-M4) and STM32L562RE (ARM Cortex-M33) microcontrollers. Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives. These results demonstrate the viability of power-based AE detection for secure, accuracy-critical TinyML deployments in black-box environments.
