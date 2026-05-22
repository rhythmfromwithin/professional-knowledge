---
interest: medium
link: https://arxiv.org/abs/2605.18931
next_step: skim
priority: medium
slack_ts: '1779423487.849289'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Markov Chain Decoders Overcome the Heavy-Tail Limitations of Lipschitz Generative
  Models
---
# Markov Chain Decoders Overcome the Heavy-Tail Limitations of Lipschitz Generative Models
> 原文: [https://arxiv.org/abs/2605.18931](https://arxiv.org/abs/2605.18931)

arXiv:2605.18931v1 Announce Type: new
Abstract: Heavy-tailed distributions are prevalent in performance evaluation, network traffic, and risk modeling. This behavior poses a fundamental challenge for modern deep generative models. Standard Variational Autoencoders (VAEs) employ Gaussian decoder likelihoods and Lipschitz-constrained neural networks, a combination that is structurally incapable of producing heavy-tailed outputs: the Gaussian tail decays exponentially, and Lipschitz continuity prevents the decoder from amplifying rare events from the latent space input to sufficiently overcome this decay. We provide both a theoretical characterization of this limitation and a controlled empirical demonstration using synthetic Pareto data across a grid of tail indices $\alpha$ $\in$ {2, 3, 5, 30} and dimensions d $\in$ {1, 5, 10}. As a solution, we replace the Gaussian decoder with a Phase-Type (PH) distribution based on Markov chains, while keeping the encoder, latent space, and training procedure identical. PH distributions allow for arbitrarily precise approximations of any positive-valued distributions, including heavy-tailed families. Experiments showed that the PH-based model reduces tail Kolmogorov-Smirnov distance by up to x6 and extreme quantile error by up to x10 compared to the Gaussian baseline for heavy-tailed data. These results demonstrate that integrating Markov chain-based distributions into the decoder of a generative model institutes a principled and practically effective solution to the heavy-tail generation problem.
