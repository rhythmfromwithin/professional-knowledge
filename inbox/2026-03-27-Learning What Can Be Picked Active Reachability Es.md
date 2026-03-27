---
title: "Learning What Can Be Picked: Active Reachability Estimation for Efficient Robotic Fruit Harvesting"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.23679
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning What Can Be Picked: Active Reachability Estimation for Efficient Robotic Fruit Harvesting
> 原文: [https://arxiv.org/abs/2603.23679](https://arxiv.org/abs/2603.23679)

arXiv:2603.23679v1 Announce Type: new
Abstract: Agriculture remains a cornerstone of global health and economic sustainability, yet labor-intensive tasks such as harvesting high-value crops continue to face growing workforce shortages. Robotic harvesting systems offer a promising solution; however, their deployment in unstructured orchard environments is constrained by inefficient perception-to-action pipelines. In particular, existing approaches often rely on exhaustive inverse kinematics or motion planning to determine whether a target fruit is reachable, leading to unnecessary computation and delayed decision-making. Our approach combines RGB-D perception with active learning to directly learn reachability as a binary decision problem. We then leverage active learning to selectively query the most informative samples for reachability labeling, significantly reducing annotation effort while maintaining high predictive accuracy. Extensive experiments demonstrate that the proposed framework achieves accurate reachability prediction with substantially fewer labeled samples, yielding approximately 6--8% higher accuracy than random sampling and enabling label-efficient adaptation to new orchard configurations. Among the evaluated strategies, entropy- and margin-based sampling outperform Query-by-Committee and standard uncertainty sampling in low-label regimes, while all strategies converge to comparable performance as the labeled set grows. These results highlight the effectiveness of active learning for task-level perception in agricultural robotics and position our approach as a scalable alternative to computation-heavy kinematic reachability analysis. Our code is available through https://github.com/wsu-cyber-security-lab-ai/active-learning.
