---
title: "Mixing-Free and Signal-Optimal Learning of Gaussian Graphical Models from Glauber Dynamics"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.18559
priority: medium
status: unread
interest: medium
next_step: skim
---
# Mixing-Free and Signal-Optimal Learning of Gaussian Graphical Models from Glauber Dynamics
> 原文: [https://arxiv.org/abs/2607.18559](https://arxiv.org/abs/2607.18559)

arXiv:2607.18559v1 Announce Type: new
Abstract: Gaussian graphical model selection is usually studied under independent sampling, but in many applications the data arise as a single trajectory of a dependent stochastic process. We study exact recovery of the graph from one trajectory of random-scan Gaussian Glauber dynamics. Existing techniques for this problem either inherit the mixing time of the chain, which can be super-polynomial in the dimension $p$ without strong assumptions, or are suboptimal in the minimum normalized edge strength $\kappa$. We propose two algorithms that are mixing-free and attain the $\kappa^{-2}$ dependence of the information-theoretic lower bounds. Both instantiate a shared dueling-neighborhood search meta-algorithm with a local statistic built directly from the update sequence. The first fits a least-squares regression at the updates of each node and recovers the graph from $\widetilde O(pd^{2}/\kappa^{2})$ updates, where $d$ is the maximum degree. This algorithm's data requirement depends on a local conditioning quantity, but only logarithmically and is provably optimal even when the underlying chain mixes slowly. The second algorithm is based on counting occurences of a specific update pattern and requires $\widetilde O(pd^{4}/\kappa^{2})$ updates, with no dependence on any condition number. The central technical challenge is that both statistics are built from dependent, non-stationary observations. Our analysis tackles this by demonstrating how to extract fresh Gaussian innovations from the update sequence, which yields mixing-free control of appropriate quantities. Neither the algorithms nor their analyses invoke stationarity, a spectral gap, or mixing conditions, and all guarantees hold from an arbitrary initialization.
