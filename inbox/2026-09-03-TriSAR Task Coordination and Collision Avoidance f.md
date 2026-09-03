---
title: "TriSAR: Task Coordination and Collision Avoidance for Aerial Robot Teams in Disaster Response"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.01731
priority: medium
status: unread
interest: medium
next_step: skim
---
# TriSAR: Task Coordination and Collision Avoidance for Aerial Robot Teams in Disaster Response
> 原文: [https://arxiv.org/abs/2609.01731](https://arxiv.org/abs/2609.01731)

arXiv:2609.01731v1 Announce Type: new
Abstract: Multi-Unmanned Aerial Vehicle (UAV) disaster-response systems require coordinated task assignment and local trajectory control, yet the individual and combined contributions of these coordination layers to mission efficiency and operational safety remain insufficiently characterised under controlled experimental conditions. TriSAR is evaluated as a five-UAV coordination system operating in a physics-based Gazebo simulation of an earthquake-damaged urban environment. A 2 x 2 factorial design compares two task-allocation strategies (Genetic Algorithm and greedy fitness-based allocation) with reactive collision avoidance enabled or disabled. Each of the four configurations was evaluated over 30 stochastic episodes in a common scenario of five UAVs and eight targets. Under greedy allocation, enabling repulsion eliminated recorded collision-threshold violations, confirmed by a Mann-Whitney test (U = 885, p = 4.03 x 10^-12, rank-biserial r = 0.97). Under GA allocation, the same protective effect was confirmed (U = 675, p = 1.26 x 10^-5, rank-biserial r = 0.50). For mission-efficiency metrics, GA-based allocation showed no statistically detectable advantage over greedy allocation when repulsion was enabled, but a significant advantage in steps, path length, and energy when repulsion was disabled (Welch's t-tests, |g| between 0.92 and 1.76). These results show that reactive repulsion provides a substantial, allocation-dependent safety benefit, while the additional computational complexity of GA-based task allocation yields a detectable mission-efficiency benefit only when repulsion is disabled.
