---
interest: medium
link: https://arxiv.org/abs/2611.17394
next_step: skim
priority: medium
slack_ts: '1794808695.368199'
source: cs.RO - Robotics
status: unread
title: 'Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training'
---
# Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training
> 原文: [https://arxiv.org/abs/2611.17394](https://arxiv.org/abs/2611.17394)

arXiv:2611.17394v1 Announce Type: new
Abstract: Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning. Coding agents can autonomously generate demonstrations through environment interaction, yet successful execution alone does not ensure effective supervision for VLA learning. We introduce Agentic-Teacher, an autonomous data engine for failure-driven VLA post-training. Given a VLA checkpoint, a task specification, and configured environment tools, the engine analyzes failed rollouts, selects intervention states, and iteratively develops closed-loop code policies through execution feedback. Validated policies become reusable demonstration generators that collect successful continuations from states where the VLA struggles. To make these demonstrations suitable for learning, Agentic-Teacher introduces temporally correlated action noise to broaden state-action coverage, removes idle frames while preserving gripper transitions, and filters trajectories using the frozen base model's flow-matching loss. The resulting demonstrations are combined with successful VLA rollouts for post-training, yielding an updated policy that operates without coding-agent assistance. Agentic-Teacher thus connects the weaknesses of a target VLA to both the generation and curation of its training data. In simulation, it improves $\pi\_0$ success rates from 79.4% to 87.8% on LIBERO-10, from 80.4% to 90.6% on MetaWorld-10, and from 0% to 30.0% across three RoboCasa tasks.
