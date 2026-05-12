---
interest: medium
link: https://arxiv.org/abs/2605.06995
next_step: skim
priority: low
slack_ts: '1778558028.336989'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Partitioning Neural Co-Variability
---
# Partitioning Neural Co-Variability
> 原文: [https://arxiv.org/abs/2605.06995](https://arxiv.org/abs/2605.06995)

arXiv:2605.06995v1 Announce Type: cross
Abstract: Trial-to-trial variability of neural responses has been linked to important aspects of neural computation and is essential for understanding how neuronal populations respond. While current overdispersion models treat each neuron's gain as independent of each other, this assumption fails to capture the network statistics of neuronal populations. As no existing model can capture overdispersed structured spiking gain-modulation across a neural population, network-level gain covariance remains largely unstudied. We thus present the Poisson matrix-normal latent variable (PMNLV) model, which extends single-neuron overdispersion to neural populations by placing a matrix-normal prior over the latent gain with a Kronecker-factored covariance. Spike counts are Poisson-distributed with a rate equal to the sum of a per-neuron stimulus tuning term and a matrix-normal gain, passed through a quadratic soft-rectifying link. We derive two complementary estimation algorithms: a variational EM (VEM) with a matrix-normal posterior that recovers dense Kronecker factors without structural assumptions, and a Kernel Tournament Method (KTM) that performs data-driven selection over a biologically motivated kernel dictionary and composite likelihood. On simulated data, both algorithms recover the inter-neuron and temporal covariance factors and accurate tuning curves. Applying VEM to Neuropixel recordings across four cortical regions of mouse visual hierarchy, we replicate a previous finding that single-neuron marginal variability changes little across cortical areas. We then show that shared population co-variability, invisible to scalar summaries e.g., the Fano factor, peaks in primary visual cortex and declines in higher visual areas. The PMNLV framework is applicable to any simultaneously recorded population where structured gain covariance is of scientific interest.
