---
interest: medium
link: https://arxiv.org/abs/2610.03846
next_step: skim
priority: medium
slack_ts: '1791266368.758779'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Probability flow ODEs in score-based and reflected diffusion models
---
# Probability flow ODEs in score-based and reflected diffusion models
> 原文: [https://arxiv.org/abs/2610.03846](https://arxiv.org/abs/2610.03846)

arXiv:2610.03846v1 Announce Type: new
Abstract: Probability-flow ordinary differential equations (PF-ODEs) are widely used as deterministic samplers for score-based diffusion models. Their usual justification is that the Fokker--Planck equation of a diffusion can be rewritten as a continuity equation driven by the score function of the forward diffusion. This identity does not, however, guarantee that the resulting velocity field generates a well-posed flow. We provide theoretical insights into the design of such deterministic samplers for generative models based on diffusions and reflected diffusions. We identify sufficient conditions for a regular Lagrangian PF-ODE flow to exist; reverse sampling and invertibility require two-sided divergence control. For learned scores, sampler stability is controlled by an unweighted velocity error, exposing a mismatch with density-weighted score matching and motivating architectural control of Jacobians, divergence, growth, and compression. Under the manifold hypothesis, positive-time regularization justifies an early-stopped PF-ODE while constants deteriorate near the data endpoint; an explicit sphere example shows that the exact deterministic flow becomes singular as the noise level vanishes even though the diffusion marginals remain well defined.
These theoretical insights translate into concrete design principles for stable, invertible, and constraint-preserving diffusion samplers. We illustrate the practical relevance of these design principles using controlled numerical experiments.
