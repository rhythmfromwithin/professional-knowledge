---
interest: medium
link: https://arxiv.org/abs/2606.26591
next_step: skim
priority: low
slack_ts: '1782447555.332769'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Three-Objective Integral R2 Subset Selection: NP-Hardness and Submodular Approximation'
---
# Three-Objective Integral R2 Subset Selection: NP-Hardness and Submodular Approximation
> 原文: [https://arxiv.org/abs/2606.26591](https://arxiv.org/abs/2606.26591)

arXiv:2606.26591v1 Announce Type: cross
Abstract: Selecting a fixed number of representative points from a finite Pareto-front approximation is a fundamental post-processing task in multiobjective optimization. This paper studies this problem for the integral R2 indicator in three objectives, where the indicator is defined as the integral of the lower envelope of weighted Tchebycheff scalarizations over the two-dimensional weight simplex. We provide two complementary algorithmic results. On the positive side, we show that the integral R2 improvement with respect to any fixed baseline is a monotone submodular set function. For the usual ideal-point based R2 indicator, with the ideal point fixed, this yields a direct gap-reduction guarantee: greedy selection closes at least a $(1-1/e)$-fraction of the maximum possible R2 gap between a fixed dominated anchor value and the best cardinality-$k$ value. We also give a tested greedy implementation that evaluates exact integral R2 values by subdivision, with worst-case running time $O(n^6)$. On the negative side, we prove that exact fixed-cardinality subset selection is NP-hard already in three objectives. The hardness proof uses a perspective transformation that maps Tchebycheff-shadow improvements to a weighted anchored-box union problem with density $(x\_1+x\_2+x\_3)^{-4}$, and then adapts the three-dimensional anchored-box construction of Bringmann, Cabello, and Emmerich. Together, these results separate the tractable two-objective case from the three-objective case while identifying a principled approximation route based on submodular optimization.
