---
title: "DRAFTO: Decoupled Reduced-space and Adaptive Feasibility-repair Trajectory Optimization for Robotic Manipulators"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.11074
priority: medium
status: unread
interest: medium
next_step: skim
---
# DRAFTO: Decoupled Reduced-space and Adaptive Feasibility-repair Trajectory Optimization for Robotic Manipulators
> 原文: [https://arxiv.org/abs/2603.11074](https://arxiv.org/abs/2603.11074)

arXiv:2603.11074v1 Announce Type: new
Abstract: This paper introduces a new algorithm for trajectory optimization, Decoupled Reduced-space and Adaptive Feasibility-repair Trajectory Optimization (DRAFTO). It first constructs a constrained objective that accounts for smoothness, safety, joint limits, and task requirements. Then, it optimizes the coefficients, which are the coordinates of a set of basis functions for trajectory parameterization. To reduce the number of repeated constrained optimizations while handling joint-limit feasibility, the optimization is decoupled into a reduced-space Gauss-Newton (GN) descent for the main iterations and constrained quadratic programming for initialization and terminal feasibility repair. The two-phase acceptance rule with a non-monotone policy is applied to the GN model, which uses a hinge-squared penalty for inequality constraints, to ensure globalizability. The results of our benchmark tests against optimization-based planners, such as CHOMP, TrajOpt, GPMP2, and FACTO, and sampling-based planners, such as RRT-Connect, RRT\*, and PRM, validate the high efficiency and reliability across diverse scenarios and tasks. The experiment involving grabbing an object from a drawer further demonstrates the potential for implementation in complex manipulation tasks. The supplemental video is available at https://youtu.be/XisFI37YyTQ.
