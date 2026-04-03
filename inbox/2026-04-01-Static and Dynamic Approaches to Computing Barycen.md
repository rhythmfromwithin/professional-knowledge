---
interest: medium
link: https://arxiv.org/abs/2603.26940
next_step: skim
priority: medium
slack_ts: '1775185058.899079'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Static and Dynamic Approaches to Computing Barycenters of Probability Measures
  on Graphs
---
# Static and Dynamic Approaches to Computing Barycenters of Probability Measures on Graphs
> 原文: [https://arxiv.org/abs/2603.26940](https://arxiv.org/abs/2603.26940)

arXiv:2603.26940v1 Announce Type: new
Abstract: The optimal transportation problem defines a geometry of probability measures which leads to a definition for weighted averages (barycenters) of measures, finding application in the machine learning and computer vision communities as a signal processing tool. Here, we implement a barycentric coding model for measures which are supported on a graph, a context in which the classical optimal transport geometry becomes degenerate, by leveraging a Riemannian structure on the simplex induced by a dynamic formulation of the optimal transport problem. We approximate the exponential mapping associated to the Riemannian structure, as well as its inverse, by utilizing past approaches which compute action minimizing curves in order to numerically approximate transport distances for measures supported on discrete spaces. Intrinsic gradient descent is then used to synthesize barycenters, wherein gradients of a variance functional are computed by approximating geodesic curves between the current iterate and the reference measures; iterates are then pushed forward via a discretization of the continuity equation. Analysis of measures with respect to given dictionary of references is performed by solving a quadratic program formed by computing geodesics between target and reference measures. We compare our novel approach to one based on entropic regularization of the static formulation of the optimal transport problem where the graph structure is encoded via graph distance functions, we present numerical experiments validating our approach, and we conclude that intrinsic gradient descent on the probability simplex provides a coherent framework for the synthesis and analysis of measures supported on graphs.
