---
interest: medium
link: https://arxiv.org/abs/2603.24806
next_step: skim
priority: medium
slack_ts: '1774666231.352719'
source: cs.RO - Robotics
status: unread
title: 'FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent
  Robot Actions'
---
# FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent Robot Actions
> 原文: [https://arxiv.org/abs/2603.24806](https://arxiv.org/abs/2603.24806)

arXiv:2603.24806v1 Announce Type: new
Abstract: Diffusion models are increasingly used for robot learning, but current designs face a clear trade-off. Action-chunking diffusion policies like ManiCM are fast to run, yet they only predict short segments of motion. This makes them reactive, but unable to capture time-dependent motion primitives, such as following a spring-damper-like behavior with built-in dynamic profiles of acceleration and deceleration. Recently, Movement Primitive Diffusion (MPD) partially addresses this limitation by parameterizing full trajectories using Probabilistic Dynamic Movement Primitives (ProDMPs), thereby enabling the generation of temporally structured motions. Nevertheless, MPD integrates the motion decoder directly into a multi-step diffusion process, resulting in prohibitively high inference latency that limits its applicability in real-time control settings. We propose FODMP (Fast One-step Diffusion of Movement Primitives), a new framework that distills diffusion models into the ProDMPs trajectory parameter space and generates motion using a single-step decoder. FODMP retains the temporal structure of movement primitives while eliminating the inference bottleneck through single-step consistency distillation. This enables robots to execute time-dependent primitives at high inference speed, suitable for closed-loop vision-based control. On standard manipulation benchmarks (MetaWorld, ManiSkill), FODMP runs up to 10 times faster than MPD and 7 times faster than action-chunking diffusion policies, while matching or exceeding their success rates. Beyond speed, by generating fast acceleration-deceleration motion primitives, FODMP allows the robot to intercept and securely catch a fast-flying ball, whereas action-chunking diffusion policy and MPD respond too slowly for real-time interception.
