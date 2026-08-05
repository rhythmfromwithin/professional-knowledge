---
interest: medium
link: https://arxiv.org/abs/2608.00113
next_step: skim
priority: medium
slack_ts: '1785899836.572519'
source: cs.RO - Robotics
status: unread
title: Track-Guided Hierarchical Reinforcement Learning for Autonomous Vehicle Drifting
  with Minimum-Lap-Time Planning
---
# Track-Guided Hierarchical Reinforcement Learning for Autonomous Vehicle Drifting with Minimum-Lap-Time Planning
> 原文: [https://arxiv.org/abs/2608.00113](https://arxiv.org/abs/2608.00113)

arXiv:2608.00113v1 Announce Type: new
Abstract: In Formula 1, drivers optimize racing lines within tire grip limits to minimize lap times; however, in rally racing, drivers intentionally break traction to drift on loose surfaces. This maneuver rapidly aligns the vehicle for corner exits, ultimately reducing lap time. Autonomously executing such maneuvers formulates a complex dual-objective control problem: stabilizing highly nonlinear drift dynamics while strictly minimizing lap time. Addressing this challenge motivates the development of advanced Minimum-Lap-Time (MLT) drift control architectures. This paper proposes a planning-control framework specifically designed for MLT drifting scenario. First, we formulate an optimal control problem to generate a MLT drift planning trajectory, which is used as prior data to train a deep reinforcement learning drift controller. Given that drifting involves extremely large sideslip angles and is therefore challenging to learn directly, a Track-guided Reinforcement Learning (TgRL) drift control method is proposed to enable progressive training in a step-by-step manner, from drift control policy, to drift corner policy, and finally to a comprehensive drift race policy. The reward function incorporates both an instant reward term and an end reward term derived from the Minimum-Lap-Time objective. Simulation results demonstrate that the proposed framework enables the agent to learn a drift racing policy that not only ensures vehicle motion control performance but also effectively reduces lap time.
