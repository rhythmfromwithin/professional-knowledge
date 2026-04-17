---
title: "Weakly-supervised Learning for Physics-informed Neural Motion Planning via Sparse Roadmap"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.13204
priority: medium
status: unread
interest: medium
next_step: skim
---
# Weakly-supervised Learning for Physics-informed Neural Motion Planning via Sparse Roadmap
> 原文: [https://arxiv.org/abs/2604.13204](https://arxiv.org/abs/2604.13204)

arXiv:2604.13204v1 Announce Type: new
Abstract: The motion planning problem requires finding a collision-free path between start and goal configurations in high-dimensional, cluttered spaces. Recent learning-based methods offer promising solutions, with self-supervised physics-informed approaches such as Neural Time Fields (NTFields) solving the Eikonal equation to learn value functions without expert demonstrations. However, existing physics-informed methods struggle to scale in complex, multi-room environments, where simply increasing the number of samples cannot resolve local minima or guarantee global consistency. We propose Hierarchical Neural Time Fields (H-NTFields), a weakly-supervised framework that combines weak supervision from sparse roadmaps with physics-informed PDE regularization. The roadmap provides global topological anchors through upper and lower bounds on travel times, while PDE losses enforce local geometric fidelity and obstacle-aware propagation. Experiments on 18 Gibson environments and real robotic platforms show that H-NTFields substantially improves robustness over prior physics-informed methods, while enabling fast amortized inference through a continuous value representation.
