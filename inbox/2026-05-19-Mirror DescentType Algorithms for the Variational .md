---
title: "Mirror Descent-Type Algorithms for the Variational Inequality Problem with Functional Constraints"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.16262
priority: high
status: unread
interest: medium
next_step: skim
---
# Mirror Descent-Type Algorithms for the Variational Inequality Problem with Functional Constraints
> 原文: [https://arxiv.org/abs/2605.16262](https://arxiv.org/abs/2605.16262)

arXiv:2605.16262v1 Announce Type: new
Abstract: Variational inequalities play a key role in machine learning research, such as generative adversarial networks, reinforcement learning, adversarial training, and generative models. This paper is devoted to the constrained variational inequality problems with functional constraints (inequality-type constraints). We propose some mirror descent-type algorithms that switch between productive and non-productive steps depending on the values of the functional constraints at iterations, with many different step size rules and stopping criteria. We analyze the proposed algorithms and prove their optimal convergence rate to achieve a solution with desired accuracy, for problems with bounded and monotone operators and Lipschitz convex functional constraints. In addition, we propose a modification of the proposed algorithms by considering each functional constraint in the calculation when we have a productive step, as well as the first constraint that violates the feasibility. This modification can save the running time of algorithms when we have many functional constraints. In addition, we provide an analysis of the proposed algorithms for $\delta$-monotone operators, allowing us to apply the proposed algorithms, as a special case, to constrained minimization problems when we do not have access to the exact information about the subgradient of the objective function. Numerical experiments that illustrate the work and performance of the proposed algorithms are also given.
