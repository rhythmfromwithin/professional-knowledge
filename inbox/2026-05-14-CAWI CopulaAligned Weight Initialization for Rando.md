---
title: "CAWI: Copula-Aligned Weight Initialization for Randomized Neural Networks"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.12580
priority: high
status: unread
interest: medium
next_step: skim
---
# CAWI: Copula-Aligned Weight Initialization for Randomized Neural Networks
> 原文: [https://arxiv.org/abs/2605.12580](https://arxiv.org/abs/2605.12580)

arXiv:2605.12580v1 Announce Type: new
Abstract: Randomized neural networks (RdNNs) enable efficient, backpropagation-free training by freezing randomly initialized input-to-hidden weights, which permits a closed-form solution for the output layer. However, conventional random initialization is blind to inter-feature dependence, ignoring correlations, asymmetries, and tail dependence in the data, which degrades conditioning and predictive performance. To the best of our knowledge, this limitation remains unaddressed in the RdNN literature. To close this gap, we propose CAWI (Copula-Aligned Weight Initialization), a framework that draws input-to-hidden weights from a data-fitted copula that matches empirical dependence, ensuring the frozen projections respect inter-feature dependence without sacrificing the closed-form solution. CAWI (i) maps each feature to the unit interval using empirical CDFs, (ii) fits a multivariate copula that captures rank-based dependence among features, and (iii) samples each weight column w\_j from the fitted copula and applies a fixed inverse marginal transform to set scale. The objective, solver, and "freeze-once" paradigm remain unchanged; only the sampling law for W becomes dependence-aware. For dependence modeling, we consider two copula families: elliptical (Gaussian, t) and Archimedean (Clayton, Frank, Gumbel). This enables CAWI to handle diverse dependence, including tail dependence. We evaluate CAWI across 83 diverse classification benchmarks (binary and multiclass) and two biomedical datasets, BreaKHis and the Schizophrenia dataset, using standard shallow and deep RdNN architectures. CAWI consistently delivers significant improvements in predictive performance over conventional random initialization. Code is available at: https://github.com/mtanveer1/CAWI
