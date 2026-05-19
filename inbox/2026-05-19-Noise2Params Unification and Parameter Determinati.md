---
title: "Noise2Params: Unification and Parameter Determination from Noise via a Probabilistic Event Camera Model"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.16317
priority: medium
status: unread
interest: medium
next_step: skim
---
# Noise2Params: Unification and Parameter Determination from Noise via a Probabilistic Event Camera Model
> 原文: [https://arxiv.org/abs/2605.16317](https://arxiv.org/abs/2605.16317)

arXiv:2605.16317v1 Announce Type: new
Abstract: Accurate, unified models for event cameras (ECs) remain elusive, hampering calibration and algorithm design. We develop a foundational probabilistic model for EC event detection, grounded in photon statistics, that unifies the description of static scene noise events and step response curves (S-curves) within a single analytical framework. Three formulations of the probability distributions are derived, spanning all intensity regimes: exact Poisson, saddle-point, and Gaussian. The model reveals the underlying connection between these otherwise disparate EC behaviors and clarifies the interpretation of S-curves, which we show is more nuanced than selecting a fixed probability threshold. Based on this model, we propose Noise2Params, a method for determining camera-specific values of the log-contrast threshold $B$, the lux-to-photon conversion factor $\alpha$, and the leakage term $\theta$ (found to be intensity dependent), via error minimization against observed noise-event distributions. Noise2Params requires only recordings of static, uniform scenes, offering an experimentally accessible alternative to approaches that demand specialized dynamic light sources. We further support the validity the model by training convolutional neural networks (CNNs) on synthetic noise images generated from our distributions and evaluating their ability to reconstruct static scenes from experimental data. We further demonstrate the utility of our model by showing that CNNs incorporating synthetic data outperform those trained solely on experimental data. Our framework provides a quantitative foundation for EC calibration, noise-aware algorithm design, and applications in photon-limited regimes.
