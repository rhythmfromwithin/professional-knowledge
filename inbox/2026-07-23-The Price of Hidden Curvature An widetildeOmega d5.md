---
title: "The Price of Hidden Curvature: An $\widetilde{\Omega} (d^{5/4} \sqrt{T})$ Lower Bound for Bandit Convex Optimization"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.18652
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Price of Hidden Curvature: An $\widetilde{\Omega} (d^{5/4} \sqrt{T})$ Lower Bound for Bandit Convex Optimization
> 原文: [https://arxiv.org/abs/2607.18652](https://arxiv.org/abs/2607.18652)

arXiv:2607.18652v1 Announce Type: new
Abstract: We establish a $\widetilde\Omega(d^{5/4}\sqrt T)$ lower bound on the minimax expected regret of stochastic bandit convex optimization of $1$-Lipschitz functions on the Euclidean ball. This presents the first nontrivial regret lower bound that grows faster than $d\sqrt{T}$ for this problem, establishing that stochastic bandit convex optimization is fundamentally harder than linear bandits.
The hard class of convex functions we construct takes the following form in dimension $2d$: for an action $a = (a^1,a^2) \in \mathbb{B}^{2d}\_2$, each function is the scaled soft maximum of a "tube", $r^{-1} \| W^\star a^1 - \frac{r}{8\varepsilon} a^2 \|\_2$ (hyperparameterized by $\varepsilon,r$), and a squared distance function, $\frac12 \| a^1 - u^\star \|\_2^2 - \frac12 \| u^\star \|\_2^2$. Here, $W^\star \in \mathbb{R}^{d \times d}$ is an unknown linear transformation, and $u^\star \in \mathbb{R}^{d}$ is an unknown vector which must be learned to minimize the function. Observations are informative about $u^\star$ only when the learner's action lies near the tube determined by $W^\star$, satisfying $a^2 \approx \frac{8\varepsilon}{r} W^\star a^1$: thus the learner must either find this tube without knowing $W^\star$, or spend observations learning useful directions of $W^\star$. Formally, our regret analysis exploits this tradeoff by bounding the posterior spread of Fisher information matrices obtained under an adaptive sequence of actions. Together, these ingredients give a sample complexity lower bound of $\widetilde{\Omega}(d^{5/2}/\varepsilon^2)$ to find an $\varepsilon$-optimal action, which translates to an $\widetilde{\Omega} (d^{5/4} \sqrt{T})$ regret lower bound. We also extend this lower bound to the unconstrained setting where the action space is $\mathbb{R}^d$.
