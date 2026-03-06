---
title: "Empirical Evaluation of No Free Lunch Violations in Permutation-Based Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.03613
priority: low
status: unread
---
# Empirical Evaluation of No Free Lunch Violations in Permutation-Based Optimization
> 原文: [https://arxiv.org/abs/2603.03613](https://arxiv.org/abs/2603.03613)

arXiv:2603.03613v1 Announce Type: cross
Abstract: The No Free Lunch (NFL) theorem guarantees equal average performance only under uniform sampling of a function space closed under permutation (c.u.p.). We ask when this averaging ceases to reflect what benchmarking actually reports. We study an iterative-search setting with sampling without replacement, where algorithms differ only in evaluation order. Binary objectives allow exhaustive evaluation in the fully enumerable case, and efficiency is defined by the first time the global minimum is reached. We then construct two additional benchmarks by algebraically recombining the same baseline functions through sums and differences. Function-algorithm relations are examined via correlation structure, hierarchical clustering, delta heatmaps, and PCA. A one-way ANOVA with Tukey contrasts confirms that algebraic reformulations induce statistically meaningful shifts in performance patterns. The uniformly sampled baseline remains consistent with the global NFL symmetry. In contrast, the algebraically modified benchmarks yield stable re-rankings and coherent clusters of functions and sampling policies. Composite objectives can also exhibit non-additive search effort despite being built from simpler components. Monte Carlo experiments indicate that order effects persist in larger spaces and depend on function class. Taken together, the results show how objective reformulation and benchmark design can generate structured local departures from NFL intuition. They motivate algorithm choice that is aware of both the problem class and the objective representation. This message applies to evolutionary computation as well as to statistical procedures based on relabeling, resampling, and permutation tests.
