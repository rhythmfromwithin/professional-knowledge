---
title: "PDGMM-VAE: A Variational Autoencoder with Adaptive Per-Dimension Gaussian Mixture Model Priors for Nonlinear ICA"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.23547
priority: medium
status: unread
interest: medium
next_step: skim
---
# PDGMM-VAE: A Variational Autoencoder with Adaptive Per-Dimension Gaussian Mixture Model Priors for Nonlinear ICA
> 原文: [https://arxiv.org/abs/2603.23547](https://arxiv.org/abs/2603.23547)

arXiv:2603.23547v1 Announce Type: new
Abstract: Independent component analysis is a core framework within blind source separation for recovering latent source signals from observed mixtures under statistical independence assumptions. In this work, we propose PDGMM-VAE, a source-oriented variational autoencoder in which each latent dimension, interpreted explicitly as an individual source signal, is assigned its own Gaussian mixture model prior. Unlike conventional VAE formulations with a shared simple prior, the proposed framework imposes per-dimension heterogeneous prior constraints, enabling the model to capture diverse non-Gaussian source statistics and thereby promote source separation under a probabilistic encoder-decoder architecture. Importantly, the parameters of these per-dimension GMM priors are not fixed in advance, but are adaptively learned and automatically refined toward convergence together with the encoder and decoder parameters under the overall training objective. Within this formulation, the encoder serves as a demixing mapping from observations to latent sources, while the decoder reconstructs the observed mixtures from the inferred components. The proposed model provides a systematic study of an idea that had previously only been noted in our preliminary form, namely, equipping different latent sources with different GMM priors for ICA, and formulates it as a full VAE framework with end-to-end training and per-dimension prior learning. Experimental results on both linear and nonlinear mixing problems demonstrate that PDGMM-VAE can recover latent source signals and achieve satisfactory separation performance.
