---
title: "Surrogate Model-Based Near-Optimal Gain Selection for Approach-Angle-Constrained Two-Phase Pure Proportional Navigation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.03371
priority: medium
status: unread
interest: medium
next_step: skim
---
# Surrogate Model-Based Near-Optimal Gain Selection for Approach-Angle-Constrained Two-Phase Pure Proportional Navigation
> 原文: [https://arxiv.org/abs/2604.03371](https://arxiv.org/abs/2604.03371)

arXiv:2604.03371v1 Announce Type: new
Abstract: In guidance literature, Pure Proportional Navigation (PPN) guidance is widely used for aerodynamically driven vehicles. A two-phase extension of PPN (2pPPN), which uses different navigation gains for an orientation phase and a final phase, has been presented to achieve any desired approach angle within an angular half-space. Recent studies show that the orientation phase can be realized through multiple feasible trajectories, creating an opportunity to select navigation gains that minimize overall guidance effort. This paper addresses the problem of near-optimal gain selection for given initial and desired terminal engagement geometries. Two optimization problems are considered: i) determination of the optimal orientation-phase gain for a specified final-phase gain, and ii) simultaneously determining the optimal gain pair for both phases that minimizes the total guidance effort. Determining the optimal gains analytically for arbitrary engagement geometries is intractable. Numerical simulations further reveal that these optimal gains vary smoothly with respect to the engagement conditions. Exploiting this property, a neural network (NN)-based regression model is developed in this paper to learn the nonlinear mapping between optimal gains and initial and desired terminal engagement geometries. The trained NN serves as a computationally efficient surrogate for generating the optimal gains manifold, enabling near-optimal realization of 2pPPN guidance. Numerical simulation studies demonstrate that the developed NN-based architecture predicts optimal gains with high accuracy, achieving very high (close to 0.9) value of coefficient of determination.
