---
interest: medium
link: https://arxiv.org/abs/2610.20659
next_step: skim
priority: medium
slack_ts: '1792296494.497139'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Latent Annealed Posterior Sampling with a Variance-Preserving Bridge for Sparsely
  Observed Random Fields
---
# Latent Annealed Posterior Sampling with a Variance-Preserving Bridge for Sparsely Observed Random Fields
> 原文: [https://arxiv.org/abs/2610.20659](https://arxiv.org/abs/2610.20659)

arXiv:2610.20659v1 Announce Type: new
Abstract: Posterior inference for random fields from sparse observations presents two major challenges: accurately characterizing complex spatial uncertainty and preventing conditional sampling costs from growing substantially as the spatial grid is refined. To address these challenges, we propose latent annealed posterior sampling (LAPS). LAPS first maps the random field into a latent space with reduced dimensionality, while a coordinate decoder composed of Branch and Trunk networks enables field evaluation at arbitrary spatial locations. Flow matching is then used to learn the latent prior distribution. Based on this learned prior, posterior sampling is performed entirely in the latent space, with the observation likelihood incorporated progressively through an annealing procedure. To control local covariance inflation, we introduce a variance-preserving (VP) bridge that allocates a covariance budget between the transported latent state and a Gaussian perturbation. Numerical experiments demonstrate that LAPS accurately approximates posterior distributions, preserves distinct posterior modes, and reduces the dependence of conditional sampling costs on spatial resolution. Across two Gaussian benchmarks, LAPS attains small errors against exact posterior references, with sliced Wasserstein distances only 2 to 3 percent higher than the reference values obtained from exact posterior samples. In a bimodal posterior problem, LAPS reduces the sliced Wasserstein distance from 0.2693 to 0.1499 and consistently recovers both modes across all test scenarios. For a two dimensional Navier-Stokes random field, LAPS substantially improves marginal posterior calibration, while its evaluation time remains nearly constant as the output grid is refined from 64^2 to 512^2. These results demonstrate that LAPS achieves a favorable tradeoff among posterior accuracy, uncertainty calibration, and computational efficiency.
