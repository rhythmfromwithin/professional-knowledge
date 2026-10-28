---
title: "Anchored Stein Variational Gradient Descent Algorithm for Non-smooth Sampling"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.36018
priority: medium
status: unread
interest: medium
next_step: skim
---
# Anchored Stein Variational Gradient Descent Algorithm for Non-smooth Sampling
> 原文: [https://arxiv.org/abs/2610.36018](https://arxiv.org/abs/2610.36018)

arXiv:2610.36018v1 Announce Type: new
Abstract: We introduce a Stein variational framework for sampling from a target density $p\propto e^{-U}$ when the target potential $U$ is possibly non-smooth. The key idea is to introduce a smoother reference potential $U\_0$ and the anchor weight $a=e^{U-U\_0}$. The resulting anchored Stein variational gradient descent (SVGD) algorithm is able to target $p\propto e^{-U}$ without computing the gradient of $U$ and include standard SVGD as a special case.
In particular, we allow the target potential $U$ to be locally Lipschitz while the reference potential $U\_0$ is continuously differentiable, along with other suitable assumptions. Under this low regularity regime, we establish a Kullback-Leibler first variation formula for anchored perturbations, identify the corresponding steepest descent direction in the reproducing kernel Hilbert space and prove a nonasymptotic convergence bound for the anchored SVGD algorithm in terms of an anchored kernelized Stein discrepancy. Finally, we also provide guidance on constructing a suitable reference potential $U\_0$ based on $U$.
