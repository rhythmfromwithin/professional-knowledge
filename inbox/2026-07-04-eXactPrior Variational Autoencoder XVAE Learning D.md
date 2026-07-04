---
interest: medium
link: https://arxiv.org/abs/2607.01275
next_step: skim
priority: medium
slack_ts: '1783136981.220529'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'eXact-Prior Variational Autoencoder (X-VAE): Learning Data-Adaptive Gaussian
  Mixture Priors for Latent Distributions'
---
# eXact-Prior Variational Autoencoder (X-VAE): Learning Data-Adaptive Gaussian Mixture Priors for Latent Distributions
> 原文: [https://arxiv.org/abs/2607.01275](https://arxiv.org/abs/2607.01275)

arXiv:2607.01275v1 Announce Type: new
Abstract: Variational Autoencoders (VAEs) commonly assume a standard isotropic Gaussian prior over the latent space, an assumption that often fails to capture the true distribution of latent representations for complex datasets. This mismatch can limit reconstruction accuracy, reduce sample quality, and constrain the expressive power of the learned latent space. We propose the eXact-Prior Variational Autoencoder (X-VAE), a framework that replaces the conventional standard normal prior with a Gaussian prior derived from the latent representations of a pretrained autoencoder (AE). Specifically, the empirical mean and standard deviation of the AE latent codes are used to parameterize a data-adaptive prior that more closely reflects the underlying structure of the training data. During generation, X-VAE introduces a latent scaling factor that enables explicit control over the variance of the sampled latent vectors, providing a simple mechanism for balancing sample diversity and fidelity. This flexibility makes the proposed approach particularly well suited for applications such as industrial and engineering design, where generated solutions must satisfy strict structural or functional constraints while still permitting meaningful design exploration. We present the mathematical formulation of well-suited X-VAE, derive the corresponding KL divergence objective for the proposed prior, and evaluate the method on standard benchmark datasets. Experimental results demonstrate that X-VAE preserves reconstruction quality while producing latent representations that better align with the empirical data distribution, leading to improved controllability and more realistic generated samples.
