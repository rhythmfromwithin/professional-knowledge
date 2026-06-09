---
interest: medium
link: https://arxiv.org/abs/2606.07855
next_step: skim
priority: medium
slack_ts: '1780978312.347569'
source: cs.RO - Robotics
status: unread
title: 'Path Planning Using Deep Deterministic Policy Gradient: A Reinforcement Learning
  Approach'
---
# Path Planning Using Deep Deterministic Policy Gradient: A Reinforcement Learning Approach
> 原文: [https://arxiv.org/abs/2606.07855](https://arxiv.org/abs/2606.07855)

arXiv:2606.07855v1 Announce Type: new
Abstract: Path-planning for autonomous vehicles in threat-laden environments is a fundamental challenge because the problem is nonlinear and nonconvex even in simplest scenarios. While traditional optimal control methods can be used to find ideal paths, the computational time is often too slow for real-time decision-making. To solve this challenge, we propose a method based on Deep Deterministic Policy Gradient (DDPG) and model the threat as possibly multiple circular 'no-go' zones. A mission is regarded as a failure if the vehicle enters this restricted zone at any time or does not reach a neighborhood of the destination. The DDPG agent is trained through trial and error in a simulated environment, learning a direct mapping from its current state (position and heading) to a series of feasible actions that guide the agent to safely reach its destination. The reword function has three parts: (a) an attractive field centered at the final destination, (b) some repulsive fields centered at the origins of circular obstacles, and (c) a penalty of control energy consumption (the magnitude of heading change) that indirectly in favor for straight path. The DDPG trains the agent using these incentives to find the largest possible set of starting points wherein a safe path to the destination is guaranteed. This provides critical information for mission planning, showing beforehand whether a task is achievable from a given starting point, assisting pre-mission planning activities. The approach is validated in simulation. A comparison between the DDPG method and a traditional optimal control (pseudo-spectral) method is carried out. The results show that the learning-based agent produces effective paths while being significantly faster, making it a better fit for real-time applications.
