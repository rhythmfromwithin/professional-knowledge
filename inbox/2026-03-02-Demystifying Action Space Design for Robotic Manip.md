---
title: "Demystifying Action Space Design for Robotic Manipulation Policies"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2602.23408
priority: medium
status: unread
interest: medium
next_step: skim
---
# Demystifying Action Space Design for Robotic Manipulation Policies
> 原文: [https://arxiv.org/abs/2602.23408](https://arxiv.org/abs/2602.23408)

arXiv:2602.23408v1 Announce Type: new
Abstract: The specification of the action space plays a pivotal role in imitation-based robotic manipulation policy learning, fundamentally shaping the optimization landscape of policy learning. While recent advances have focused heavily on scaling training data and model capacity, the choice of action space remains guided by ad-hoc heuristics or legacy designs, leading to an ambiguous understanding of robotic policy design philosophies. To address this ambiguity, we conducted a large-scale and systematic empirical study, confirming that the action space does have significant and complex impacts on robotic policy learning. We dissect the action design space along temporal and spatial axes, facilitating a structured analysis of how these choices govern both policy learnability and control stability. Based on 13,000+ real-world rollouts on a bimanual robot and evaluation on 500+ trained models over four scenarios, we examine the trade-offs between absolute vs. delta representations, and joint-space vs. task-space parameterizations. Our large-scale results suggest that properly designing the policy to predict delta actions consistently improves performance, while joint-space and task-space representations offer complementary strengths, favoring control stability and generalization, respectively.
