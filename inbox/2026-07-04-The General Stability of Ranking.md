---
interest: medium
link: https://arxiv.org/abs/2607.01546
next_step: skim
priority: low
slack_ts: '1783136978.006499'
source: cs.DB - Databases
status: unread
title: The General Stability of Ranking
---
# The General Stability of Ranking
> 原文: [https://arxiv.org/abs/2607.01546](https://arxiv.org/abs/2607.01546)

arXiv:2607.01546v1 Announce Type: new
Abstract: Rankings derived from weighted scoring functions are widely used in settings such as university rankings and employment candidate evaluations. Since ranking weights are often chosen by organizations or analysts, ranking stability asks whether a reported ranking persists under reasonable weight changes. Prior work on stable rankings formalizes this idea through volume-based stability, which measures the fraction of the weight space that induces the target ranking exactly.
This exact-match requirement can be too blunt: once a perturbed weight vector produces a different ranking, exact stability gives it no credit, whether the change replaces the top-ranked item or only swaps two nearly tied lower-ranked items. We propose general stability, a distance-based generalization that aggregates ranking regions according to a user-defined distance from the target ranking. This lets users specify which ranking changes matter in the application, while recovering exact stability as a special case.
Our algorithmic focus is stability computation: given a reported or user-specified ranking and a distance function, estimate its general-stability score. We give a two-dimensional sweep algorithm and an unbiased multidimensional sampler that extend exact-stability methods, and analyze why sampling can scale poorly as the dimension grows. Motivated by this scaling challenge, we identify quasiconvex distance functions as a tractable subclass and introduce Conv-SC, which reduces stability computation for this subclass to convex-volume approximation, where randomized polynomial-time methods are available. Experiments on eight real datasets and generated instances show that distance-sensitive stability gives informative real-data results, that our estimators are accurate and practical, and that Conv-SC improves scaling with dimension for quasiconvex distance functions.
