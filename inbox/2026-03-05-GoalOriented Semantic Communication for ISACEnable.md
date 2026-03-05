---
title: "Goal-Oriented Semantic Communication for ISAC-Enabled Robotic Obstacle Avoidance"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.02291
priority: medium
status: unread
---
# Goal-Oriented Semantic Communication for ISAC-Enabled Robotic Obstacle Avoidance
> 原文: [https://arxiv.org/abs/2603.02291](https://arxiv.org/abs/2603.02291)

arXiv:2603.02291v1 Announce Type: new
Abstract: We investigate an integrated sensing and communication (ISAC)-enabled BS for the unmanned aerial vehicle (UAV) obstacle avoidance task, and propose a goal-oriented semantic communication (GOSC) framework for the BS to transmit sensing and command and control (C&C) signals efficiently and effectively. Our GOSC framework establishes a closed loop for sensing-C&C generation-sensing and C&C transmission: For sensing, a Kalman filter (KF) is applied to continuously predict UAV positions, mitigating the reliance of UAV position acquisition on continuous sensing signal transmission, and enhancing position estimation accuracy through sensing-prediction fusion. Based on the refined estimation position provided by the KF, we develop a Mahalanobis distance-based dynamic window approach (MD-DWA) to generate precise C&C signals under uncertainty, in which we derive the mathematical expression of the minimum Mahalanobis distance required to guarantee collision avoidance. Finally, for efficient sensing and C&C signal transmission, we propose an effectiveness-aware deep Q-network (E-DQN) to determine the transmission of sensing and C&C signals based on their value of information (VoI). The VoI of sensing signals is quantified by the reduction in uncertainty entropy of UAV's position estimation, while the VoI of C&C signals is measured by their contribution to UAV navigation improvement. Extensive simulations validate the effectiveness of our proposed GOSC framework. Compared to the conventional ISAC transmission framework that transmits sensing and C&C signals at every time slot, GOSC achieves the same 100% task success rate while reducing the number of transmitted sensing and C&C signals by 92.4% and the number of transmission time slots by 85.5%.
