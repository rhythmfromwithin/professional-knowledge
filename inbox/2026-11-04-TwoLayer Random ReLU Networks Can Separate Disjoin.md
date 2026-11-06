---
interest: medium
link: https://arxiv.org/abs/2611.04211
next_step: skim
priority: medium
slack_ts: '1793945320.184899'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Two-Layer Random ReLU Networks Can Separate Disjoint Classes
---
# Two-Layer Random ReLU Networks Can Separate Disjoint Classes
> 原文: [https://arxiv.org/abs/2611.04211](https://arxiv.org/abs/2611.04211)

arXiv:2611.04211v1 Announce Type: new
Abstract: Set separation by continuous linear functionals is fundamental in functional analysis and convex optimization and underlies binary classification in machine learning. Support vector machines provide maximum-margin affine separators for linearly separable data, while kernel methods represent nonlinear decision rules through linear separation in a reproducing-kernel Hilbert space. We study when two classes, not necessarily convex or linearly separable in the input space, can be separated with positive margin by finite ReLU networks and by random ReLU features.
At the deterministic level, we prove that positive-margin separation by a finite ReLU network is equivalent to the existence of finite closed convex covers whose opposite-label members have positive pairwise distances, and exactly two hidden layers suffice. For random separation, suppose each class is represented as a finite union of nonempty closed convex cells, possibly unbounded. If every opposite-label cell pair has positive distance and its closed difference cone is pointed, then two independent random ReLU layers yield a common positive-margin affine separator with high probability.
The first layer separates the feature image of each negative cell from the feature image of the positive class by a hyperplane through the origin. It also controls all cross-class distances uniformly. The second layer combines cellwise scores through Chebyshev polynomials and realizes the resulting polynomial using Gaussian Hermite features, followed by a uniform finite-width approximation. With the remaining geometric, bias, and confidence parameters fixed, each sufficient width is quadratic in the largest Gaussian width of a spherical difference-cone section, hence at most linear in its span dimension. An example shows that this squared Gaussian-width dependence is sharp for both layers.
