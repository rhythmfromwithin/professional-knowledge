---
interest: medium
link: https://arxiv.org/abs/2605.27409
next_step: skim
priority: low
slack_ts: '1780202381.150359'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'STARS: Spike Tail-Aware Relational Synthesis for ANN-to-SNN Data-Free Knowledge
  Distillation'
---
# STARS: Spike Tail-Aware Relational Synthesis for ANN-to-SNN Data-Free Knowledge Distillation
> 原文: [https://arxiv.org/abs/2605.27409](https://arxiv.org/abs/2605.27409)

arXiv:2605.27409v1 Announce Type: new
Abstract: SNNs promise energy-efficient and low-latency inference, but their performance still trails that of ANNs. ANN-to-SNN knowledge distillation helps narrow this gap, yet the original training data are often unavailable in practical deployment settings. Existing data-free knowledge distillation (DFKD) methods synthesize surrogate data by matching teacher-side priors, especially BN statistics, but these ANN-oriented constraints mainly regularize mean and variance and therefore remain under-constrained for SNN students whose responses depend on threshold-crossing dynamics. In this paper, we propose Spike Tail-Aware Relational Synthesis (STARS), a plug-and-play method for ANN-to-SNN DFKD that augments standard BN-guided synthesis with two complementary objectives: Relational Consistency Alignment, which preserves cross-sample relational consistency between teacher and student, and Tail-Aware Regularization, which regularizes threshold-relevant tail probabilities through soft exceedance over teacher-derived thresholds. Together, these objectives generate synthetic batches that remain teacher-valid while becoming more informative for SNN students. Experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet across multiple ANN-SNN pairs show that our method consistently improves conventional DFKD baselines and even surpasses several KD methods, with gains of up to 4.6\% on CIFAR-10 and 6.7\% on CIFAR-100, highlighting the importance of complementing BN matching with relational and tail-aware constraints in SNN-oriented DFKD.
