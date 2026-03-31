---
title: "SAHMM-VAE: A Source-Wise Adaptive Hidden Markov Prior Variational Autoencoder for Unsupervised Blind Source Separation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.25776
priority: medium
status: unread
interest: medium
next_step: skim
---
# SAHMM-VAE: A Source-Wise Adaptive Hidden Markov Prior Variational Autoencoder for Unsupervised Blind Source Separation
> 原文: [https://arxiv.org/abs/2603.25776](https://arxiv.org/abs/2603.25776)

arXiv:2603.25776v1 Announce Type: new
Abstract: We propose SAHMM-VAE, a source-wise adaptive Hidden Markov prior variational autoencoder for unsupervised blind source separation. Instead of treating the latent prior as a single generic regularizer, the proposed framework assigns each latent dimension its own adaptive regime-switching prior, so that different latent dimensions are pulled toward different source-specific temporal organizations during training. Under this formulation, source separation is not implemented as an external post-processing step; it is embedded directly into variational learning itself. The encoder, decoder, posterior parameters, and source-wise prior parameters are optimized jointly, where the encoder progressively learns an inference map that behaves like an approximate inverse of the mixing transformation, while the decoder plays the role of the generative mixing model. Through this coupled optimization, the gradual alignment between posterior source trajectories and heterogeneous HMM priors becomes the mechanism through which different latent dimensions separate into different source components. To instantiate this idea, we develop three branches within one common framework: a Gaussian-emission HMM prior, a Markov-switching autoregressive HMM prior, and an HMM state-flow prior with state-wise autoregressive flow transformations. Experiments show that the proposed framework achieves unsupervised source recovery while also learning meaningful source-wise switching structures. More broadly, the method extends our structured-prior VAE line from smooth, mixture-based, and flow-based latent priors to adaptive switching priors, and provides a useful basis for future work on interpretable and potentially identifiable latent source modeling.
