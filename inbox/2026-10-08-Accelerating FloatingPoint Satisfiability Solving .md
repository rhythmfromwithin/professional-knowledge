---
title: "Accelerating Floating-Point Satisfiability Solving via Gradient Normalization"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.08808
priority: high
status: unread
interest: medium
next_step: skim
---
# Accelerating Floating-Point Satisfiability Solving via Gradient Normalization
> 原文: [https://arxiv.org/abs/2610.08808](https://arxiv.org/abs/2610.08808)

arXiv:2610.08808v1 Announce Type: new
Abstract: Satisfiability Modulo Theories (SMT) solvers are foundational to software verification, program analysis, and compiler testing, particularly over the theory of Quantifier-Free Floating-Point (QF\_FP). While recent optimization-based SMT solvers have successfully applied gradient descent to continuous relaxations of logical formulas, they are fundamentally bottlenecked by gradient domination, a phenomenon where a small subset of difficult clauses hijacks the optimization trajectory, preventing the solver from satisfying the broader formula and trapping it in local minima.
To overcome this, we present GradSAT, a novel framework that bridges optimization-based SMT solving with Multi-Task Learning (MTL). GradSAT reformulates the constraint satisfaction process by treating each SMT clause as an independent MTL task. By applying dynamic gradient normalization (GradNorm), GradSAT actively balances the gradient magnitudes across all clauses at runtime, systematically penalizing dominant gradients and accelerating lagging clauses to ensure uniform convergence. GradSAT implements this through a highly optimized, two-stage hybrid pipeline. First, a GPU-accelerated PyTorch backend leveraging symbolic compilation and operator fusion navigates the continuous relaxation to a high-quality basin. Second, the candidate assignment is handed off to a bit-precise local search engine to rapidly resolve the exact, rigorous assignment. By stabilizing the continuous search dynamics, GradSAT mitigates the brittleness of prior gradient-based solvers and provides a robust, highly parallelizable architecture for complex constraint solving.
