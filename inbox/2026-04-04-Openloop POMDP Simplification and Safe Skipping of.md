---
title: "Open-loop POMDP Simplification and Safe Skipping of Replanning with Formal Performance Guarantees"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.01352
priority: medium
status: unread
interest: medium
next_step: skim
---
# Open-loop POMDP Simplification and Safe Skipping of Replanning with Formal Performance Guarantees
> 原文: [https://arxiv.org/abs/2604.01352](https://arxiv.org/abs/2604.01352)

arXiv:2604.01352v1 Announce Type: new
Abstract: Partially Observable Markov Decision Processes (POMDPs) provide a principled mathematical framework for decision-making under uncertainty. However, the exact solution to POMDPs is computationally intractable. In this paper, we address the computational intractability by introducing a novel framework for adaptive open-loop simplification with formal performance guarantees. Our method adaptively interleaves open-loop and closed-loop planning via a topology-based belief tree, enabling a significant reduction in planning complexity. The key contribution lies in the derivation of efficiently computable bounds which provide formal guarantees and can be used to ensure that our simplification can identify the immediate optimal action of the original POMDP problem. Our framework therefore provides computationally tractable performance guarantees for macro-actions within POMDPs. Furthermore, we propose a novel framework for safely skipping replanning during execution, supported by theoretical guarantees on multi-step open-loop action sequences. To the best of our knowledge, this framework is the first to address skipping replanning with formal performance guarantees. Practical online solvers for our proposed simplification are developed, including a sampling-based solver and an anytime solver. Empirical results demonstrate substantial computational speedups while maintaining provable performance guarantees, advancing the tractability and efficiency of POMDP planning.
