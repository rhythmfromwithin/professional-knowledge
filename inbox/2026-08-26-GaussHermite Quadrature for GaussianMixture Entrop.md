---
interest: medium
link: https://arxiv.org/abs/2608.21467
next_step: skim
priority: medium
slack_ts: '1787708809.590459'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Gauss--Hermite Quadrature for Gaussian-Mixture Entropy with an Action-Space
  Hermite Surrogate
---
# Gauss--Hermite Quadrature for Gaussian-Mixture Entropy with an Action-Space Hermite Surrogate
> 原文: [https://arxiv.org/abs/2608.21467](https://arxiv.org/abs/2608.21467)

arXiv:2608.21467v1 Announce Type: new
Abstract: Gaussian distributions are used to model uncertainty in signals and states, and Gaussian mixtures are often used when the underlying distribution is multimodal. Unlike a single Gaussian, a Gaussian mixture generally has no closed-form expression for differential entropy and therefore requires numerical approximation. We propose a Gauss--Hermite quadrature method for evaluating Gaussian mixture differential entropy. The quadrature order controls the numerical resolution of the approximation. The method is evaluated on one- and two-dimensional Gaussian mixture benchmarks against Taylor approximations, analytic entropy bounds, and numerical integration references.
For repeated optimization over continuous actions, we also propose a Hermite polynomial surrogate in action space. In a radar pointing benchmark, its second-order form achieves substantially lower surrogate error and optimizer regret than a second-order Taylor surrogate based on local derivatives at the nominal action, while both methods use nine direct objective evaluations per replanning step. The Hermite surrogate also improves pointing performance in the tested benchmark.
