---
title: "Polynomial-Time Optimal Group Selection via the Double-Commutator Eigenvalue Problem"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.00834
priority: high
status: unread
interest: medium
next_step: skim
---
# Polynomial-Time Optimal Group Selection via the Double-Commutator Eigenvalue Problem
> 原文: [https://arxiv.org/abs/2605.00834](https://arxiv.org/abs/2605.00834)

arXiv:2605.00834v1 Announce Type: new
Abstract: The algebraic diversity framework replaces temporal averaging over multiple observations with algebraic group action on a single observation for second-order statistical estimation. The central open problem in this framework is $\textit{group selection}$: given an $M$-dimensional observation with unknown covariance structure, find the finite group whose spectral decomposition best matches the covariance. Naive enumeration of all subgroups of the symmetric group $S\_M$ requires exponential time in $M$. We prove that this combinatorial problem reduces to a generalized eigenvalue problem derived from the double commutator of the covariance matrix, yielding a polynomial-time algorithm with complexity $O(d^2M^2 + d^3)$, where $d$ is the dimension of a generator basis. The minimum eigenvector of the double-commutator matrix directly constructs the optimal group generator in closed form, with no iterative optimization. The reduction is exact: the double-commutator minimum eigenvalue is zero if and only if the optimal generator lies in the span of the basis, and its magnitude provides a certifiable optimality gap when it does not. This problem does not appear in the standard catalogs of computational complexity (Garey and Johnson, 1979) and represents a new class linking group theory, matrix analysis, and statistical estimation. We establish connections to independent component analysis (JADE), structured matrix nearness problems, and simultaneous matrix diagonalization, and we show that the double-commutator formulation is the unique approach that is simultaneously polynomial-time, closed-form, and certifiable.
