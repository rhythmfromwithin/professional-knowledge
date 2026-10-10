---
interest: medium
link: https://arxiv.org/abs/2610.09041
next_step: skim
priority: low
slack_ts: '1791610120.369769'
source: cs.DB - Databases
status: unread
title: Building Navigable Graphs Without Search in Three Composable Stages
---
# Building Navigable Graphs Without Search in Three Composable Stages
> 原文: [https://arxiv.org/abs/2610.09041](https://arxiv.org/abs/2610.09041)

arXiv:2610.09041v1 Announce Type: new
Abstract: Navigable graphs can be built without searching for neighbors: partition the data, evaluate every pair inside each part, and select each point's edges from the candidates. We give such a construction in three separable stages and show that the middle one decides the quality. The pool is any partition with a few memberships per point. The ending turns a point's candidates into out-edges; ours keeps a bounded heap, prunes by occlusion with a per-corpus slack, and appends reverse edges, re-pruning only where a list overflows. The spine is any edge set, exempt from the prune, that keeps the graph reachable from its entry; ours, half-space-proximal edges over a random sample, routes monotonically to every sampled point and replaces a spanning tree at 1/10 to 1/500 of its cost. The ending composes with any partitioner: on PiPNN's own candidate pool it beats PiPNN's ending on each of six corpora from $10^6$ to $10^8$ points, by 3 to 14% in distance evaluations at equal recall, and with 60 to 120 memberships per point the composed build matches or beats a full dense construction at k=10 and k=100 on all six, in 0.5 to 0.9 of its build time, deterministically. The analysis explains why. Once a pool is localised its quality is set by the data: every pool built on GIST lands within 4% of the exact-kNN ceiling, and the pairs a block cover misses are predicted, point by point, by the local clustering of the kNN graph, whose zero-clustering tail sets the memberships a corpus needs and grows with n. All code, patches and logs are public.
