---
title: "Interpretable Collision Avoidance and Feasibility Guarantees through an Uncertainty Aware Pipeline"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.33186
priority: medium
status: unread
interest: medium
next_step: skim
---
# Interpretable Collision Avoidance and Feasibility Guarantees through an Uncertainty Aware Pipeline
> 原文: [https://arxiv.org/abs/2610.33186](https://arxiv.org/abs/2610.33186)

arXiv:2610.33186v1 Announce Type: new
Abstract: Autonomous vehicles (AVs) operating in dynamic, challenging conditions such as intersections and roundabouts must guarantee collision avoidance under uncertainty while maintaining real-time feasibility. Most existing planners struggle to simultaneously guarantee both requirements. Chance-constrained formulations embed safety constraints directly in the optimization but become infeasible as uncertainty compounds; deterministic planners provide feasible solutions but fail to address the uncertainty that causes collisions; end-to-end learned policies provide neither guarantee in an interpretable form.
We present a modular perception-prediction-planning pipeline that closes this gap by propagating uncertainty as structured, interpretable quantities across module boundaries. Rather than embedding probabilistic risk directly in the optimization, our pipeline resolves collision probabilities upstream and constructs convex safe sets within which the planner provides a guaranteed feasible solution at every cycle -- decoupling the safety guarantee from solver feasibility.
Across Monte Carlo trials in a four-way unsignalized intersection, our pipeline achieves 0% collisions and 0% solver infeasibility at 12.7ms per cycle, compared to 36% and 10% collision rates for deterministic and chance-constrained baselines respectively. The ablation study confirms the necessity of each uncertainty source and the hardware deployment on Clearpath Jackal UGVs validates the pipeline's real-time viability on physical platforms.
