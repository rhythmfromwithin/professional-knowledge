---
title: "Designing Dense Satellite Clusters for Distributed Space-based Datacenters"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.15335
priority: medium
status: unread
interest: medium
next_step: skim
---
# Designing Dense Satellite Clusters for Distributed Space-based Datacenters
> 原文: [https://arxiv.org/abs/2605.15335](https://arxiv.org/abs/2605.15335)

arXiv:2605.15335v1 Announce Type: new
Abstract: Recent proposals for datacenters in sun-synchronous Low Earth Orbit rely on a large number of compute satellites formation-flying in dense clusters. Designing such satellite clusters requires optimizing the satellites' orbital geometry under several safety and operational constraints applied throughout the cluster's entire orbit. These constraints include guaranteeing a minimum inter-satellite spacing, obstruction-less solar power for every satellite, and that each satellite have a stable set of nearest neighbors with which it can maintain inter-satellite links (ISLs). In this work, we propose two main cluster orbital designs, parametrized by the minimum inter-satellite spacing $R\_{min}$ and the cluster radius $R\_{max}$: a planar cluster, and a 3D cluster. We show by construction and numerical analysis that both cluster orbital designs are consistent with the inter-satellite spacing, unobstructed sun-vector, and inter-satellite line of sight constraints. The proposed planar architecture is the most efficient packing of satellites in a plane for given $R\_{min}$ and $R\_{max}$ values, and our 3D architecture allows for the number of datacenter satellites to scale proportional to $(R\_{max}/R\_{min})^3$, an improvement over all previous LEO datacenter cluster designs. Finally, for a given satellite cluster, we formulate and solve an integer optimization problem that maps a VL2-like Clos network datacenter switching fabric onto the satellites and their corresponding set of feasible ISLs. We confirm that for both the planar and 3D architectures, there are sufficiently many permanently unobstructed ISLs within the cluster to replicate the switching fabric of terrestrial datacenters. We also examine the tradeoff between the number of ISLs each satellite can simultaneously sustain, and the corresponding number of cluster satellites that must be dedicated as aggregation and intermediate switches.
