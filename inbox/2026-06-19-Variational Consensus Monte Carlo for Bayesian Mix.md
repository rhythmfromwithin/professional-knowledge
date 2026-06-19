---
title: "Variational Consensus Monte Carlo for Bayesian Mixture"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2606.19643
priority: medium
status: unread
interest: medium
next_step: skim
---
# Variational Consensus Monte Carlo for Bayesian Mixture
> 原文: [https://arxiv.org/abs/2606.19643](https://arxiv.org/abs/2606.19643)

arXiv:2606.19643v1 Announce Type: new
Abstract: Motivated by the privacy, sensitivity and sharing limitations of health data, we present a comprehensive pipeline for inference of Bayesian mixture models within a federated learning setting, i.e. when data cannot be fully shared or pooled across compute nodes. We adopt a Consensus Monte Carlo (CMC) approach, in which an MCMC algorithm is run independently within each data silo to estimate local posterior distributions, which are then aggregated to approximate the posterior over the full data. The variational CMC approach of Rabinovich, Angelino and Jordan (2015) [1] frames the aggregation step as a variational inference problem, but their application to mixtures assumes the number of clusters and key mixture parameters to be known. Our main methodological contributions are: (i) an extension of variational CMC to over-fitted Bayesian mixture models that infer the number of clusters and all model parameters, without requiring conjugacy; (ii) novel cluster-matching algorithms suitable for cross-silo settings in which not every cluster appears in each local dataset; (iii) a number of inference strategies for the aggregation step, matched to different federated learning constraints; and (iv) guidelines for choosing among these in practice. A comprehensive simulation study validates the framework and allows us to compare to state-of-the-art federated learning alternatives. Notably, we show that when the composition of local datasets reflects the underlying clustering structure in the data, our approach can recover small clusters with greater accuracy than standard MCMC applied to the pooled data. We illustrate the framework on large-scale electronic health record data, identifying multi-morbidity patterns in a British geriatric population.
