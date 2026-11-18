---
title: "Better Calibrated, Better Planned: Uncertainty-Aware Multi-ASV Informative Path Planning for Oil Spill Monitoring"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.21783
priority: medium
status: unread
interest: medium
next_step: skim
---
# Better Calibrated, Better Planned: Uncertainty-Aware Multi-ASV Informative Path Planning for Oil Spill Monitoring
> 原文: [https://arxiv.org/abs/2611.21783](https://arxiv.org/abs/2611.21783)

arXiv:2611.21783v1 Announce Type: new
Abstract: Monitoring oil spills with fleets of Autonomous Surface Vehicles (ASVs) requires mapping a heterogeneous pollutant field from sparse, noisy measurements under tight time and energy budgets. Informative Path Planning (IPP) addresses this problem by coupling a reconstruction model, which infers the field and its uncertainty, with a planner that decides where to sample next. Prior work has focused on planning strategies and has largely relied on Gaussian Processes (GPs), leaving the calibration of the model's uncertainty underexplored. We study how uncertainty calibration conditions multi-vehicle IPP with a fleet of ASVs that coordinates online through a shared uncertainty map. We introduce Evidential Deep Learning (EDL) as an uncertainty-calibrated information model. We benchmark EDL, Monte Carlo Dropout and Deep Ensembles against a GP in closed loop with five planners on physics-based oil spill simulations. Across 60 maps, the choice of model dominates the outcome, explaining 80\% of the variance of the final reconstruction error, against 1\% for the planner among the deep models. EDL achieves the lowest error and the highest IoU under every planner, is the best calibrated model and runs at 3.9 ms per step. With 50 cells per vehicle it reconstructs the spill better than MC Dropout and Deep Ensembles with 150. Deep Ensembles become more confident as their error grows, whereas EDL is unaffected. Robustness of the information model to the data its own planner collects is therefore a requirement of uncertainty-aware IPP.
