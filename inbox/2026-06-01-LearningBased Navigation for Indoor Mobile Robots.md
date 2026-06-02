---
interest: medium
link: https://arxiv.org/abs/2605.30468
next_step: skim
priority: medium
slack_ts: '1780375675.591579'
source: cs.RO - Robotics
status: unread
title: Learning-Based Navigation for Indoor Mobile Robots
---
# Learning-Based Navigation for Indoor Mobile Robots
> 原文: [https://arxiv.org/abs/2605.30468](https://arxiv.org/abs/2605.30468)

arXiv:2605.30468v1 Announce Type: new
Abstract: This paper presents a learning-based navigation framework for indoor mobile robots. The proposed method combines a supervised neural global planner, trained from cost-aware A\* expert trajectories, with the proposed Learning-Based DWA local planner, which is formulated as discrete candidate selection over the Dynamic Window Approach (DWA) action lattice. For local planning, the policy is first trained by behavior cloning and then refined by Proximal Policy Optimization (PPO) under feasibility-aware masking. The framework is implemented and evaluated in both simulated and real-world indoor environments. Experimental results show that the proposed method generates feasible global routes and reliable local motion commands for safe goal-directed navigation in the presence of obstacles. These results demonstrate the effectiveness of integrating learning-based global planning with reinforcement-learning-refined local control for indoor mobile robot navigation. The source code will be released at https://ntdathp.github.io/rl\_robot\_web/.
