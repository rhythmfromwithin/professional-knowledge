---
interest: medium
link: https://arxiv.org/abs/2610.12549
next_step: skim
priority: medium
slack_ts: '1791873083.191409'
source: cs.RO - Robotics
status: unread
title: 'Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual
  and Physical Feedback'
---
# Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback
> 原文: [https://arxiv.org/abs/2610.12549](https://arxiv.org/abs/2610.12549)

arXiv:2610.12549v1 Announce Type: new
Abstract: Embodied coding agents construct robot policies from natural-language instructions by generating executable programs and refining them from execution feedback. This refinement assumes that execution feedback reveals whether the task succeeded and, after a failure, provides sufficient evidence to guide program revision. Aerial manipulation violates this assumption in two ways. Payload constraints restrict onboard camera coverage and leave task-critical outcomes outside the robot's view (partial observability), while strong dynamic coupling and limited control margins make physical interactions fragile (limited interaction robustness) and leave failure causes unresolved. Re-examining the same feedback cannot recover observations that were never collected or separate failure causes that the available evidence does not distinguish. To acquire this missing evidence, we introduce Active Feedback (AF), an active "View and Probe" framework. When execution feedback leaves unresolved questions, the agent synthesizes a separate diagnostic program that runs in simulation to inspect unseen outcomes from informative viewpoints (View) or test hypotheses about failure causes through targeted physical interactions (Probe). Across six simulated aerial manipulation tasks with 60 trials per condition, AF reduces false completion declarations from 25 to 5 and raises final task success from 31.7% to 75% compared with terminal feedback under the same coding-agent configuration and task-execution limit. Using shared robot APIs, task programs refined with AF in simulation run on a physical aerial manipulator without task-program source-code modification and complete multi-stage manipulation tasks in the real world. These results show that executable diagnosis fills gaps in execution feedback for embodied coding agents, improving both completion assessment and program refinement in aerial manipulation.
