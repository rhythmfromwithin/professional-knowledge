---
title: "Fast Distributed $(\Delta + 1)$-Edge Coloring in Bipartite Graphs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.22690
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fast Distributed $(\Delta + 1)$-Edge Coloring in Bipartite Graphs
> 原文: [https://arxiv.org/abs/2610.22690](https://arxiv.org/abs/2610.22690)

arXiv:2610.22690v1 Announce Type: new
Abstract: We show that, on bipartite $n$-vertex graphs in the LOCAL model of distributed computation, $(\Delta + 1)$-edge coloring can be solved deterministically in $O(f(\Delta) \log n)$ rounds for some function $f$.
In particular this implies a deterministic $O(\log n)$-round upper bound for $(\Delta + 1)$-edge coloring on bipartite constant-degree graphs.
Our results improve on the previous state-of-the-art bounds (which hold already on general graphs) whose $n$-dependencies are $\widetilde{O}(\log^5 n)$ rounds deterministically and $\widetilde{O}(\log^2 n)$ rounds randomized [Bernshteyn and Dhawan, J.\ Comb.\ Theory 2025].
In fact, we obtain the aforementioned results already for a more restrictive version of $(\Delta + 1)$-edge coloring that corresponds to a \emph{local-palette} strengthening of Vizing's theorem shown recently to hold [Christiansen, STOC 2023].
In this version, every edge $\{u, v\}$ has to be colored with a color from $\{1, \dots, \max(\operatorname{deg}(u), \operatorname{deg}(v))+ 1\}$.
For all of our results, the vertices do not need to know on which side of the bipartition they lie---the structural promise of bipartiteness suffices.
