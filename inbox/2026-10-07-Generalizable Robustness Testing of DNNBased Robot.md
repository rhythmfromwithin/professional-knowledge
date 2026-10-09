---
interest: medium
link: https://arxiv.org/abs/2610.06862
next_step: skim
priority: medium
slack_ts: '1791524733.236389'
source: cs.RO - Robotics
status: unread
title: Generalizable Robustness Testing of DNN-Based Robotic Navigation Systems via
  XAI-Guided Search
---
# Generalizable Robustness Testing of DNN-Based Robotic Navigation Systems via XAI-Guided Search
> 原文: [https://arxiv.org/abs/2610.06862](https://arxiv.org/abs/2610.06862)

arXiv:2610.06862v1 Announce Type: new
Abstract: \*\*Context:\*\* Deep Neural Networks (DNNs) increasingly control Cyber-Physical Systems (CPSs), yet small input perturbations can cause unsafe system-level behavior. Existing approaches often optimize perturbations for individual images and evaluate them only in simulation, limiting their generalizability and practical validity.
\*\*Objectives:\*\* This work aims to generate robustness tests that remain effective across operational observations and to evaluate whether the resulting failures transfer from simulation to a physical robot.
\*\*Methods:\*\* We propose an explainability-guided multi-objective evolutionary approach that generates sparse perturbations over representative images selected through visual and behavioral clustering. Aggregated Integrated Gradients guide mutations toward influential image regions. We evaluate the approach on a DNN-controlled LeoRover in Gazebo, conduct an ablation study, and validate a stratified subset of perturbations on the physical robot.
\*\*Results:\*\* The approach achieved a median success rate of 70.0%, compared with 53.85% for unguided search, and increased median hypervolume from 0.65 to 0.73. Multi-image optimization improved the success rate from 50.0% to 57.5%, while XAI guidance further increased it to 70.0%. In the sim-to-real evaluation, simulation achieved 0.95 precision and 0.67 recall, and simulated and physical failure times showed a significant positive correlation of 0.617.
\*\*Conclusion:\*\* Combining multi-image optimization with explainability-guided search improves robustness testing for DNN-controlled robotic systems. Simulation effectively identifies and prioritizes transferable failures, but physical validation remains necessary because some real-world failures are not reproduced in simulation.
