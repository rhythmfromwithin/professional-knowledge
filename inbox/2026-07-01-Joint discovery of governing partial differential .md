---
interest: medium
link: https://arxiv.org/abs/2606.30699
next_step: skim
priority: high
slack_ts: '1782880933.572969'
source: cs.LG - Machine Learning
status: unread
title: Joint discovery of governing partial differential equations from multi-source
  datasets by competitive optimization
---
# Joint discovery of governing partial differential equations from multi-source datasets by competitive optimization
> 原文: [https://arxiv.org/abs/2606.30699](https://arxiv.org/abs/2606.30699)

arXiv:2606.30699v1 Announce Type: new
Abstract: Discovering governing equations directly from observational data is a key step towards interpretable scientific machine learning. Current data-driven approaches typically operate on a single dataset, inherently limiting their performance when faced with restricted observations. In practice, multiple datasets are often available for the same physical system, distinguished only by distinct initial conditions or boundary configurations. Here, we present a competitive optimization framework designed to discover shared partial differential equations (PDEs) from multi-source datasets, termed MCO-PDE. The framework first trains independent neural surrogates for each data source, and then employs a soft-competitive weighting mechanism to dynamically assess dataset credibility and aggregate a consensus global coefficient. Integrated with a genetic algorithm for structural search, this approach simultaneously identifies the functional forms and parameters of the governing laws. We demonstrate that fusing as few as 50 observations per dataset across seven cases recovers canonical equations with high accuracy. The framework inherently handles two- and three-dimensional domains characterized by irregular boundaries and heterogeneous coefficients, and successfully extracts physically meaningful laws from real-world wave-tank experiments. Overall, this work establishes a promising route for automated scientific discovery via heterogeneous data fusion.
