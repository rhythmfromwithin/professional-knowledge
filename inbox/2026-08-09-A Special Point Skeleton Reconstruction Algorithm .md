---
title: "A Special Point Skeleton Reconstruction Algorithm for Dynamic Multiobjective Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.06096
priority: low
status: unread
interest: medium
next_step: skim
---
# A Special Point Skeleton Reconstruction Algorithm for Dynamic Multiobjective Optimization
> 原文: [https://arxiv.org/abs/2608.06096](https://arxiv.org/abs/2608.06096)

arXiv:2608.06096v1 Announce Type: new
Abstract: To address the issue that existing dynamic multi-objective optimization algorithms mainly rely on individual migration or independent special point sampling after environmental changes, while failing to fully exploit the structural relationships among representative solutions, a Special Point Skeleton Reconstruction based Dynamic Multi-Objective Evolutionary Algorithm (SPSR-DMOEA) is proposed. First, the centroid, knee points, and extreme points are extracted from the Pareto optimal solution set of the current environment, and their positions in the new environment are adaptively predicted according to their movement velocities across consecutive environments. Subsequently, in the decision space, the centroid is connected with other anchor points, and a minimum spanning tree is constructed among the non-centroid anchor points, thereby establishing a prediction skeleton capable of describing the overall population structure. According to the lengths of the skeleton edges, the number of individuals allocated to each edge is determined proportionally. Candidate solutions are uniformly generated along each edge, and random orthogonal perturbations are introduced to expand the search region around the skeleton. Experimental results on the DF dynamic multi-objective benchmark suite demonstrate the effectiveness of the proposed method in dynamic tracking capability.
