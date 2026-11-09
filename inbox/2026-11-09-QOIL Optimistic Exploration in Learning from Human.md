---
title: "Q-OIL: Optimistic Exploration in Learning from Human Interventions"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2611.08576
priority: medium
status: unread
interest: medium
next_step: skim
---
# Q-OIL: Optimistic Exploration in Learning from Human Interventions
> 原文: [https://arxiv.org/abs/2611.08576](https://arxiv.org/abs/2611.08576)

arXiv:2611.08576v1 Announce Type: new
Abstract: As robots are deployed in the real world, they will inevitably make mistakes. Human interventions provide valuable feedback for improving their behavior, enabling them to adapt online to new scenarios. However, studying human-in-the-loop robot learning is difficult: real-world experiments are slow and expensive, so most algorithm development relies on simulated human models. We show that common human modeling assumptions do not match how real people intervene in practice. Through analyzing intervention data from human participants, we find that humans tend to intervene when agent progress stalls, and that their corrective actions are often suboptimal. Motivated by these findings, we introduce a progress-based model of human intervention that achieves higher rank correlation with real-user algorithm rankings, enabling realistic algorithm benchmarking and development in simulation. Building on these insights, we propose Q-OIL, a method that adds optimistic bonuses to intervention transitions in reinforcement learning and softly guides exploration toward human corrections. We find that decoupled critics are critical for stability because they prevent the bonuses from backing up to pre-intervention states. As a result, Q-OIL learns more efficiently than competitive baselines, achieving 10-50% higher success in simulation and on real robots, and improving pretrained VLAs on two bimanual manipulation tasks. As we ground both evaluation and algorithms in realistic human behavior, this work provides a practical path toward scalable robot learning from interventions.
