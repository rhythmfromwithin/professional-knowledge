---
interest: medium
link: https://arxiv.org/abs/2608.11407
next_step: skim
priority: medium
slack_ts: '1786844804.055879'
source: cs.RO - Robotics
status: unread
title: Top-down Traffic Scenario Generation via Joint Initial-Goal Diffusion and Trajectory
  Infilling
---
# Top-down Traffic Scenario Generation via Joint Initial-Goal Diffusion and Trajectory Infilling
> 原文: [https://arxiv.org/abs/2608.11407](https://arxiv.org/abs/2608.11407)

arXiv:2608.11407v1 Announce Type: new
Abstract: Robust traffic simulators are crucial for developing and testing autonomous vehicles to reduce the costly, labor-intensive real-world data collection process and the need for physical presence on the road. However, existing simulators require agents' initial states to generate trajectories, which limits scalability and diversity due to restrictions on the given initial states. While data-driven agent initialization has been widely studied, the generated initial states are not interpretable in terms of why the agents are initialized at those specific locations. Given known initial states, trajectory generation is also a challenging problem, as the model must learn the variability of the destination and how agents should reach it over time. In this paper, we propose TrafficDiffuser, a top-down traffic scenario generation framework that generates high-level traffic scenarios, defined by initial and goal state pairs, by jointly modeling them. The high-level scenario generation makes initial states better interpretable and reduces trajectory generation into as simple as an infilling problem. We demonstrate how the generated high-level traffic scenarios can be used, including constraining based on different trajectory modes and integrating them with existing trajectory generation models. We conduct extensive experiments on the Argoverse 2 motion prediction dataset to evaluate how well the generated outputs capture real-world distributions. In addition to generating goal states, TrafficDiffuser outperforms the next-best approach for agent initialization, reducing speed distribution distance by 55.3% and the off-road rate by 2.8%.
