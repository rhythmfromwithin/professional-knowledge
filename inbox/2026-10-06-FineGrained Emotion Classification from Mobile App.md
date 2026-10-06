---
title: "Fine-Grained Emotion Classification from Mobile App Reviews: An Empirical Study with Large Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.03802
priority: high
status: unread
interest: medium
next_step: skim
---
# Fine-Grained Emotion Classification from Mobile App Reviews: An Empirical Study with Large Language Models
> 原文: [https://arxiv.org/abs/2610.03802](https://arxiv.org/abs/2610.03802)

arXiv:2610.03802v1 Announce Type: new
Abstract: Context: Fine-grained emotion classification of mobile app reviews enables requirements engineering activities that go beyond polarity-based opinion mining, including emotionally informed issue prioritisation and feature-oriented feedback analysis. However, automatic fine-grained emotion extraction from app reviews remains understudied. Objectives: Building on a previously published annotation framework and human-labelled ground truth adapted from Plutchik's taxonomy, this paper investigates how large language models can be leveraged for automatic multi-label emotion classification under severe class imbalance. Methods: We compare encoder-only fine-tuning under multi-label and binary-ensemble formulations, decoder-only zero- and few-shot prompting across open-source and proprietary models, and a catalogue of imbalance mitigation strategies (loss reweighting, resampling, generative data augmentation), with the synthetic-review generator and prompting strategy selected via an intrinsic augmentation-utility ranking. Results: Fine-tuned encoders trail the best decoder-only few-shot prompting (macro-F1 0.642) by a wide margin at baseline (multi-label: 0.387; binary ensemble: 0.450); pairing the best multi-label encoder with generative data augmentation and positive-weighted loss closes most of this gap (+0.204) at up to three orders of magnitude lower inference latency than the decoders, with the largest gains on the rarest emotions, from undetected to gains of up to +0.501 F1. Conclusion: Large language models make fine-grained, multi-label emotion classification of app reviews feasible for requirements engineering pipelines, with modest macro-F1, and the best formulation and mitigation strategy are backbone- and formulation-dependent. We release the experimental pipeline, synthetic corpora, and fine-tuned checkpoints for replication and reuse.
