---
interest: medium
link: https://arxiv.org/abs/2609.17619
next_step: skim
priority: medium
slack_ts: '1789619683.739509'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Stability-Constrained Approximation in Spline KANs: Exact Layer Balancing
  and Budget-Compatible Saturation'
---
# Stability-Constrained Approximation in Spline KANs: Exact Layer Balancing and Budget-Compatible Saturation
> 原文: [https://arxiv.org/abs/2609.17619](https://arxiv.org/abs/2609.17619)

arXiv:2609.17619v1 Announce Type: new
Abstract: Deep spline superposition networks face a tension between approximation order and stability across depth. We study approximation under a hard layerwise Lipschitz budget, and organise it around two quantities: the factorisation stability complexity of a given deep factorisation, and the budget-compatible approximation complexity of a discretisation operator.
First, we solve exactly the finite-depth diagonal balancing problem for a fixed chain of nonnegative envelope matrices: the optimal uniform layer budget equals $\|M\_{L-1}\cdots M\_0\|\_{\infty\to\infty}^{1/L}$, attained by an explicit one-pass minimiser, for rectangular layers, with a complete treatment of degeneracies and non-attainment. The optimum can be arbitrarily larger than the Lipschitz constant of the network itself, because passing to envelopes destroys sign cancellation.
Second, we give a constructive spline discretisation theorem preserving the budget up to a controlled slack, with an explicit grid threshold. Conversely, for linear spline-valued operators that preserve the budget exactly, we prove budget-compatible minimax lower bounds on classes constrained simultaneously in the first and third derivative norms -- a constraint pair that is forced by the problem and that rules out the usual scaling escapes.
Finally, we show that the corresponding layer errors need not cancel under composition: for every operator of the class there is a stable depth-$L$ tower realising a constant fraction of the accumulated error, so the linear-in-depth accumulation of the upper bound is not a proof artefact.
