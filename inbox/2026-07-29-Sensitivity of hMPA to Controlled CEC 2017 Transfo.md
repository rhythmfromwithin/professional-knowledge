---
interest: medium
link: https://arxiv.org/abs/2607.22862
next_step: skim
priority: low
slack_ts: '1785295229.596179'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Sensitivity of hMPA to Controlled CEC 2017 Transformations
---
# Sensitivity of hMPA to Controlled CEC 2017 Transformations
> 原文: [https://arxiv.org/abs/2607.22862](https://arxiv.org/abs/2607.22862)

arXiv:2607.22862v1 Announce Type: new
Abstract: The standard CEC 2017 benchmark applies bias, shift, and rotation simultaneously, confounding their individual effects on algorithmic behavior. We introduce a parameterized implementation that controls these transformations independently while preserving the original functions and transformation data. The framework diagnoses the hybrid Marine Predators Algorithm (hMPA), whose predicted-candidate mechanism depends on numerical objective values and coordinate-wise reconstruction. DSC and extended DSC (eDSC) are adapted from algorithm-level comparison to configuration-level diagnosis, enabling, to our knowledge, the first exhaustive analysis of all eight bias-shift-rotation configurations of a parameterized CEC 2017 benchmark. We examine all 56 three-configuration subsets and comparisons with the untransformed control. Experiments cover 29 functions, dimensions 10-100, 30 independent runs, and a budget of 10000\*dim objective-function evaluations. DSC and eDSC detect statistically significant differences among configurations at every dimension, but rankings vary across functions, preventing a consistent ordering. Shift generally worsens objective values; isolated rotation causes no systematic deterioration, while isolated bias has little effect on final-solution distributions. Shift-rotation combinations differ most consistently from the control. Convergence plots reveal function- and dimension-dependent separation, plateaus, and late improvement. Results are limited to hMPA, the chosen parameters, 30 runs, the fixed budget, and the analyzed CEC 2017 functions. Within this scope, the framework provides a reproducible diagnostic protocol extensible to other continuous optimizers and related CEC benchmarks, including CEC 2024 and CEC 2025.
