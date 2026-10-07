---
title: "RMRRT: Riemannian Barrier Metric RRT for Inequality-Aware Steering on Equality Manifolds"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.06863
priority: medium
status: unread
interest: medium
next_step: skim
---
# RMRRT: Riemannian Barrier Metric RRT for Inequality-Aware Steering on Equality Manifolds
> 原文: [https://arxiv.org/abs/2610.06863](https://arxiv.org/abs/2610.06863)

arXiv:2610.06863v1 Announce Type: new
Abstract: This paper presents a motion planning framework that unifies equality and inequality constraints within a single geometric formulation for sampling-based planning in high-dimensional robotic systems. In conventional sampling-based planners, equality constraints are typically enforced through projection, whereas inequality constraints are handled separately through binary validity checks such as collision testing, often leading to inefficient exploration. To address this limitation, we propose Riemannian Barrier Metric RRT (RMRRT), which constructs a unified local geometry for planning on equality-constrained manifolds. RMRRT first builds an ambient barrier metric from inequality-sensitive barrier terms and then induces a tangent-space metric via a (G)-orthogonal projection associated with the equality constraints. The resulting tangent-space metric is used consistently in both steering and nearest-neighbor selection, biasing exploration away from nearby inequality boundaries while preserving first-order equality consistency. In this work, the metric is instantiated from signed-distance-based geometric proxy inequalities to provide collision-informative tangent-space directions; hard feasibility is enforced separately through standard validity checks. Experimental results show that RMRRT achieves a 100% success rate across diverse constrained manipulation tasks in both simulation and real-world settings, while reducing planning time relative to representative constrained planning baselines. Ablation studies further demonstrate that the proposed metric improves exploration quality by reducing rejected samples and shortening path length. Experiment videos and source code are available at: https://rmrrt-anonymous.github.io
