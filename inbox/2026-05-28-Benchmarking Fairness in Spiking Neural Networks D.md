---
interest: medium
link: https://arxiv.org/abs/2605.27407
next_step: skim
priority: low
slack_ts: '1780028387.256259'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Benchmarking Fairness in Spiking Neural Networks: Data Bias, Spurious Features,
  and Hardware Effects'
---
# Benchmarking Fairness in Spiking Neural Networks: Data Bias, Spurious Features, and Hardware Effects
> 原文: [https://arxiv.org/abs/2605.27407](https://arxiv.org/abs/2605.27407)

arXiv:2605.27407v1 Announce Type: new
Abstract: Evaluating fairness in Spiking Neural Networks (SNNs) demands rigorous benchmarks that reflect real-world complexities, yet existing assessments remain limited by superficial dataset diversity and idealized hardware assumptions. This work introduces the first systematic fairness benchmark for SNNs, addressing three critical dimensions of realism: (1) demographic coverage gaps in training data, (2) spurious feature leakage (e.g., skin tone as a proxy for class labels), and (3) deployment-environment mismatches (e.g., edge devices with constrained spike encoding). Our framework integrates four cross-demographic datasets with controlled bias injections and three neuromorphic hardware simulators (Loihi 2, SpiNNaker), enabling isolated analysis of fairness-performance trade-offs under resource constraints. Standardized evaluations of 12 state-of-the-art SNNs reveal stark disparities: models trained on biased data exhibit 23\% higher false positive rates for underrepresented groups, while hardware limitations (e.g., reduced spike precision) further amplify accuracy gaps by up to 41\% in edge deployments. Critically, bias mitigation strategies developed for cloud-based SNNs often degrade under resource constraints, highlighting the need for co-design principles that jointly optimize fairness and hardware efficiency. By bridging algorithmic fairness research with neuromorphic engineering, our benchmark provides a foundation for trustworthy SNNs in socially critical applications such as healthcare and autonomous systems. Our code is available at: https://anonymous.4open.science/r/SNN-Benchmarks-8017.
