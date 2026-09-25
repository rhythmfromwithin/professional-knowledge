---
interest: medium
link: https://arxiv.org/abs/2609.28709
next_step: skim
priority: medium
slack_ts: '1790310834.670289'
source: cs.RO - Robotics
status: unread
title: 'OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight'
---
# OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight
> 原文: [https://arxiv.org/abs/2609.28709](https://arxiv.org/abs/2609.28709)

arXiv:2609.28709v1 Announce Type: new
Abstract: Autonomous UAV flight through cluttered and partially unknown environments requires reasoning not only about observed obstacles but also about occluded regions that the sensor cannot observe. We present OA-MPPI, an obstacle- and occlusion-aware extension of Model Predictive Path Integral (MPPI) control for quadrotor flight that accounts for potential moving agents emerging from these regions into the vehicle's path. At every planning step, we extract a 3D occlusion boundary from the online occupancy map and use it to model the regions that hidden agents could reach over the prediction horizon. We penalize trajectories that enter these expanding regions within MPPI rollouts generated using nonlinear quadrotor dynamics and accounting for individual rotor thrust limits. We validate the proposed approach in simulation and hardware flight experiments, with the complete pipeline running onboard the vehicle in real time. Results show increased clearance from occlusion boundaries compared to baseline MPPI in both settings, as well as avoidance of an agent emerging from occlusion in simulation.
