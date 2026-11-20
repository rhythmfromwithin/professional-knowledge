---
title: "Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.25067
priority: medium
status: unread
interest: medium
next_step: skim
---
# Mapping the Wind to Find the Source: Online Physics-Informed Gas Source Localization with Mobile Robots
> 原文: [https://arxiv.org/abs/2611.25067](https://arxiv.org/abs/2611.25067)

arXiv:2611.25067v1 Announce Type: new
Abstract: Gas Source Localization (GSL) with mobile robots is challenging because wind and gas measurements are spatially sparse, noisy, and potentially affected by robot motion. Indoor airflow can vary substantially across space, while detailed environmental layouts, boundary conditions, or precomputed airflow fields are often unavailable. Moreover, hazardous sources must be localized as quickly as possible, making exhaustive exploration impractical. This paper presents a lightweight physics-informed probabilistic framework for efficient GSL under spatially varying indoor airflow. As the robot navigates, it continuously collects wind and gas measurements and reconstructs the spatially varying airflow field online. The estimated wind field drives a forward dispersion model that predicts the gas pattern for each candidate source location. These predictions are compared with the measured gas pattern to update a probabilistic belief over the source location. As the wind field is reconstructed incrementally, the framework also accounts for the spatially non-uniform reliability of wind field estimation and its influence on the source estimation. The resulting belief map is then used for informative path planning to guide the robot toward informative regions. High-fidelity simulations provide a comprehensive evaluation of the individual components and their integrations within the complete system, while physical indoor experiments assess the system performance under realistic sensing, motion, and airflow conditions. The results demonstrate that incorporating lightweight physical knowledge significantly improves localization robustness under spatially complex airflow and enables more efficient exploration.
