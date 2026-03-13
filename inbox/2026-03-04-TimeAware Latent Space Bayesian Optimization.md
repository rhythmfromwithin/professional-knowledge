---
interest: medium
link: https://arxiv.org/abs/2603.00935
next_step: skim
priority: medium
slack_ts: '1773369790.611459'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Time-Aware Latent Space Bayesian Optimization
---
# Time-Aware Latent Space Bayesian Optimization
> 原文: [https://arxiv.org/abs/2603.00935](https://arxiv.org/abs/2603.00935)

arXiv:2603.00935v1 Announce Type: new
Abstract: Latent-space Bayesian optimization (LSBO) extends Bayesian optimization to structured domains, such as molecular design, by searching in the continuous latent space of a generative model. However, most LSBO methods assume a fixed objective, whereas real design campaigns often face temporal drift (e.g., evolving preferences or shifting targets). Bringing time-varying BO into LSBO is nontrivial: drift can affect not only the surrogate, but also the latent search space geometry induced by the representation. We propose Time-Aware Latent-space Bayesian Optimization (TALBO), which incorporates time in both the surrogate and the learned generative representation via a GP-prior variational autoencoder, yielding a latent space aligned as objectives evolve. To evaluate timevarying LSBO systematically, we adapt widely used molecular design tasks to drifting multi-property objectives and introduce metrics tailored to changing targets. Across these benchmarks, TALBO consistently outperforms strong LSBO baselines and remains robust across drift speeds and design choices, while remaining competitive under actually time-invariant objectives.
