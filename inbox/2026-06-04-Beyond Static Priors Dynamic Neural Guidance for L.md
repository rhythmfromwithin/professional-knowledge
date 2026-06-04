---
title: "Beyond Static Priors: Dynamic Neural Guidance for Large-Scale Ant Colony Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2606.04039
priority: low
status: unread
interest: medium
next_step: skim
---
# Beyond Static Priors: Dynamic Neural Guidance for Large-Scale Ant Colony Optimization
> 原文: [https://arxiv.org/abs/2606.04039](https://arxiv.org/abs/2606.04039)

arXiv:2606.04039v1 Announce Type: new
Abstract: Neural-guided Ant Colony Optimization (ACO) suffers from a fundamental training-inference misalignment: policies are typically trained to generate static priors (e.g., heatmaps), yet deployed to guide iterative, long-horizon search processes. In this paper, we present DyNACO, a novel framework that achieves dynamic neural guidance by periodically observing the pheromone distribution and the incumbent solution. To make DyNACO tractable at scale, we pair the policy with a perturbation-based ACO backend and a scope-restricted refinement mechanism that jointly ensure efficacy and stable credit assignment. On TSP, DyNACO scales to 100,000-node instances and outperforms neural baselines while often reducing total runtime compared to the unguided solver. We extend DyNACO to CVRP via a capacity-aware backend, consistently improving the unguided baseline with less than 1% neural overhead. We further provide in-depth analysis validating the model's generalization capabilities and elucidating why dynamic guidance outperforms static priors. Our work underscores the necessity of aligning neural training with iterative search dynamics in learning-guided optimization. The code is available at https://github.com/shoraaa/DyNACO.
