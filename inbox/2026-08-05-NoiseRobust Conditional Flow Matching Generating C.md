---
title: "Noise-Robust Conditional Flow Matching: Generating Clean Samples from Noisy Datasets"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.00064
priority: medium
status: unread
interest: medium
next_step: skim
---
# Noise-Robust Conditional Flow Matching: Generating Clean Samples from Noisy Datasets
> 原文: [https://arxiv.org/abs/2608.00064](https://arxiv.org/abs/2608.00064)

arXiv:2608.00064v2 Announce Type: new
Abstract: Generative models learn the statistical properties of their training data, so high-quality generation depends on clean and representative datasets. In scientific imaging, acquisition often yields noisy measurements, while collecting clean references can be costly, impractical or even unattainable. Training directly on these measurements results in a model that reproduces the corrupted data. This can be circumvented by learning the clean population distribution directly from the noisy data. Conditional flow matching (CFM) combines a simple regression objective with stable training, efficient sampling, and strong image-generation performance, making it a natural framework for this setting. We introduce Noise-Robust Conditional Flow Matching (NR-CFM), an unconditional generator that learns from one corrupted observation per image. NR-CFM provides a closed-form clean endpoint correction for additive white Gaussian noise and learns a data-driven correction for general Gaussian corruptions with more complex covariance structure. Across the evaluated corruption settings, NR-CFM outperforms NR-GAN in most cases and remains competitive with Ambient Diffusion in the high-noise regime. We further evaluate NR-CFM on scientific data at signal-to-noise ratios as low as $0.001$, where it generates plausible particle images from severely corrupted measurements.
