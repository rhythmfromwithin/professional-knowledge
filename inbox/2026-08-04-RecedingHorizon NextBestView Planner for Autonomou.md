---
title: "Receding-Horizon Next-Best-View Planner for Autonomous Leaf Surface Reconstruction"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.28995
priority: medium
status: unread
interest: medium
next_step: skim
---
# Receding-Horizon Next-Best-View Planner for Autonomous Leaf Surface Reconstruction
> 原文: [https://arxiv.org/abs/2607.28995](https://arxiv.org/abs/2607.28995)

arXiv:2607.28995v1 Announce Type: new
Abstract: Accurate plant leaf modeling is fundamental to downstream tasks such as plant growth monitoring, and phenotyping for yield estimation. Autonomous robotic reconstruction for large-scale field deployment must address limitations on robot planning budget and computation resources while optimizing viewpoint utility for leaf surface reconstruction. Existing approaches either focus on rigid objects, point-cloud coverage or plant reconstruction without fully addressing the system limitations or exploiting task-driven point cloud utility. In this work, we study next-best-view (NBV) planning for leaf surface reconstruction under travel constraints. We develop a novel Centroid-based Information Gain (CIG) function that measures the spatial distribution of observed points relative to the centroid of the existing point cloud to compute viewpoint utility. We also develop a receding-horizon variant that reasons over future viewpoints. To benchmark our work, we use the LAST-STRAW [1] public dataset that includes point clouds of strawberry plants over different growth stages and compare our method with attention-driven NBV [2] that uses a visibility-based information gain approach. The proposed receding-horizon approach consistently reduces surface reconstruction error and improves geometric fidelity across multiple growth stages, especially under increased inter-leaf occlusion. Results demonstrate that our approach is able to visit viewpoints that reduce surface reconstruction error and improves reconstruc-tion accuracy as compared to the baseline by upto 10%.
