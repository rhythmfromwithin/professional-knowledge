---
interest: medium
link: https://arxiv.org/abs/2603.08771
next_step: skim
priority: medium
slack_ts: '1773888799.083679'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Micro-Diffusion Compression - Binary Tree Tweedie Denoising for Online Probability
  Estimation
---
# Micro-Diffusion Compression - Binary Tree Tweedie Denoising for Online Probability Estimation
> 原文: [https://arxiv.org/abs/2603.08771](https://arxiv.org/abs/2603.08771)

arXiv:2603.08771v2 Announce Type: new
Abstract: We present Midicoth, a lossless compression system that introduces a micro-diffusion denoising layer for improving probability estimates produced by adaptive statistical models. In compressors such as Prediction by Partial Matching (PPM), probability estimates are smoothed by a prior to handle sparse observations. When contexts have been seen only a few times, this prior dominates the prediction and produces distributions that are significantly flatter than the true source distribution, leading to compression inefficiency. Midicoth addresses this limitation by treating prior smoothing as a shrinkage process and applying a reverse denoising step that corrects predicted probabilities using empirical calibration statistics. To make this correction data-efficient, the method decomposes each byte prediction into a hierarchy of binary decisions along a bitwise tree. This converts a single 256-way calibration problem into a sequence of binary calibration tasks, enabling reliable estimation of correction terms from relatively small numbers of observations. The denoising process is applied in multiple successive steps, allowing each stage to refine residual prediction errors left by the previous one. The micro-diffusion layer operates as a lightweight post-blend calibration stage applied after all model predictions have been combined, allowing it to correct systematic biases in the final probability distribution. Midicoth combines five fully online components: an adaptive PPM model, a long-range match model, a trie-based word model, a high-order context model, and the micro-diffusion denoiser applied as the final stage.
