---
title: "Optimize, Learn, Refine: Whole-Body Grasping and Pick-and-Throw with a Spiral Soft Robot"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.38202
priority: medium
status: unread
interest: medium
next_step: skim
---
# Optimize, Learn, Refine: Whole-Body Grasping and Pick-and-Throw with a Spiral Soft Robot
> 原文: [https://arxiv.org/abs/2609.38202](https://arxiv.org/abs/2609.38202)

arXiv:2609.38202v1 Announce Type: new
Abstract: Soft continuum robots can exploit distributed compliance for whole-body manipulation, but synthesizing behavior through changing contacts remains difficult. We address whole-body grasping and pick-and-throw from an initially ungrasped state through outcome-based actuation-space optimization. Grasping is quantified by tip angular sweep and body-object enclosure, while throwing further incorporates release-direction alignment and minimum release speed. These objectives allow grasping, acceleration, and release to emerge from compliant interaction without prescribing contact forces, contact locations, or body configurations. Because the resulting actuation-to-outcome mapping is nonsmooth, we utilize derivative-free CMA-ES within an optimize-learn-refine framework. CMA-ES generates solutions for sampled conditions, a task-conditioned predictor learns warm starts, and CMA-ES refines them for unseen conditions. In simulation, the method achieves 492/500 successful grasps (98.4%) and success rates of 98%, 97%, and 94% across three directional throwing trials. Learned initialization increases grasping success from 78.6% to 98.4% while reducing the median rollout count from 1184 to 816 in CMA-ES. Hardware experiments achieve a 100% grasping success rate across 50 executions and a 100% pick-and-throw success rate across 30 executions, with 10 repetitions per direction. Together, these simulation and hardware results demonstrate the effectiveness of the proposed framework across both simulated and physical whole-body manipulation tasks.
