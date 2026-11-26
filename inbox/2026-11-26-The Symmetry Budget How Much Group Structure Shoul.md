---
title: "The Symmetry Budget: How Much Group Structure Should a Network Architecture Assume?"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.33169
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Symmetry Budget: How Much Group Structure Should a Network Architecture Assume?
> 原文: [https://arxiv.org/abs/2611.33169](https://arxiv.org/abs/2611.33169)

arXiv:2611.33169v1 Announce Type: new
Abstract: A network architecture is, in large part, a symmetry assumption: convolution ties weights across translations, attention ties them across permutations, and a fully connected layer ties nothing. When the data are only approximately symmetric, tying trades approximation error against estimation error, and the right amount of tying is a property of the dataset, not of the architecture alone. We study this trade-off in an exactly solvable model: linear maps on signals over the cyclic group $\mathbb{Z}\_d$, with architectures indexed by the subgroup lattice of $\mathbb{Z}\_d$, so that a single integer $k \mid d$ interpolates between an unconstrained layer ($k=1$, $d^2$ parameters) and a fully equivariant one ($k=d$, $d$ parameters). We derive the finite-sample excess risk in closed form, show that for a generic symmetry defect the leading-order risk is affine in $1/k$, and prove that intermediate architectures are then never strictly optimal: the lattice collapses to an all-or-nothing choice with phase boundary $n^\star = \sigma^2 d(d-1)/\varepsilon^2$. Structured defects break this collapse and restore interior optima, and we give a closed-form defect profile for a graded defect. Measurements agree with the theory on $60/60$ cells of a $(\varepsilon,n)$ phase diagram and $48/48$ cells of a second phase diagram at $d=16$, recover the predicted exponent as $-1.92$ against $-2$, and exhibit the predicted $k^\star: 12 \to 4 \to 1$ ladder under graded defects; a two-layer nonlinear control reproduces the crossover. We also characterize when the affine collapse survives for non-abelian groups.
