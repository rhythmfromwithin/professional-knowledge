---
title: "Uncertainty propagation in auto-regressive random neural network models"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.20483
priority: low
status: unread
interest: medium
next_step: skim
---
# Uncertainty propagation in auto-regressive random neural network models
> 原文: [https://arxiv.org/abs/2608.20483](https://arxiv.org/abs/2608.20483)

arXiv:2608.20483v1 Announce Type: cross
Abstract: We develop analytical and particle-based methods for uncertainty propagation in random neural network models, where both the inputs and network parameters are allowed to be random. Building on the piecewise-linear structure of the Leaky ReLU activation function, we derive a local approximation of the neural network output with respect to perturbations in both its inputs and parameters. This approximation is exact for perturbations that preserve the network activation pattern, and it allows us to compute analytical expressions for the probability density function and characteristic function of the network output, together with closed-form approximations for its mean and covariance. We extend this uncertainty propagation framework to autonomous dynamical systems whose one-step evolution map is represented by a random neural network. Repeated application of this map defines an autoregressive model, for which we derive recursive equations to propagate uncertainty in both the state and network parameters over time. These equations explicitly account for the state-parameter cross-covariance that develops under successive iterations of the network. Numerical experiments on the Lorenz-63 system and the Kuramoto-Sivashinsky equation demonstrate accurate uncertainty propagation through the predictability horizon and the applicability of the proposed framework to high-dimensional dynamical systems.
