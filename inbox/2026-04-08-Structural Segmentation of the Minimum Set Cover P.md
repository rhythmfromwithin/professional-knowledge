---
title: "Structural Segmentation of the Minimum Set Cover Problem: Exploiting Universe Decomposability for Metaheuristic Optimization"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2604.03234
priority: high
status: unread
interest: medium
next_step: skim
---
# Structural Segmentation of the Minimum Set Cover Problem: Exploiting Universe Decomposability for Metaheuristic Optimization
> 原文: [https://arxiv.org/abs/2604.03234](https://arxiv.org/abs/2604.03234)

arXiv:2604.03234v1 Announce Type: new
Abstract: The Minimum Set Cover Problem (MSCP) is a classical NP-hard combinatorial optimization problem with numerous applications in science and engineering. Although a wide range of exact, approximate, and metaheuristic approaches have been proposed, most methods implicitly treat MSCP instances as monolithic, overlooking potential intrinsic structural properties of the universe. In this work, we investigate the concept of \emph{universe segmentability} in the MSCP and analyze how intrinsic structural decomposition (universe segmentability) can be exploited to enhance heuristic optimization. We propose an efficient preprocessing strategy based on disjoint-set union (union--find) to detect connected components induced by element co-occurrence within subsets, enabling the decomposition of the original instance into independent subproblems. Each subproblem is solved using the GRASP metaheuristic, and partial solutions are combined without compromising feasibility. Extensive experiments on standard benchmark instances and large-scale synthetic datasets show that exploiting natural universe segmentation consistently improves solution quality and scalability, particularly for large and structurally decomposable instances. These gains are supported by a succinct bit-level set representation that enables efficient set operations, making the proposed approach computationally practical at scale.
