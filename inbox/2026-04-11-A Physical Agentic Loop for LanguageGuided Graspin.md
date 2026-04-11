---
interest: medium
link: https://arxiv.org/abs/2604.07395
next_step: skim
priority: medium
slack_ts: '1775875960.784489'
source: cs.RO - Robotics
status: unread
title: A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring
---
# A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring
> 原文: [https://arxiv.org/abs/2604.07395](https://arxiv.org/abs/2604.07395)

arXiv:2604.07395v1 Announce Type: new
Abstract: Robotic manipulation systems that follow language instructions often execute grasp primitives in a largely single-shot manner: a model proposes an action, the robot executes it, and failures such as empty grasps, slips, stalls, timeouts, or semantically wrong grasps are not surfaced to the decision layer in a structured way. Inspired by agentic loops in digital tool-using agents, we reformulate language-guided grasping as a bounded embodied agent operating over grounded execution states, where physical actions expose an explicit tool-state stream. We introduce a physical agentic loop that wraps an unmodified learned manipulation primitive (grasp-and-lift) with (i) an event-based interface and (ii) an execution monitoring layer, Watchdog, which converts noisy gripper telemetry into discrete outcome labels using contact-aware fusion and temporal stabilization. These outcome events, optionally combined with post-grasp semantic verification, are consumed by a deterministic bounded policy that finalizes, retries, or escalates to the user for clarification, guaranteeing finite termination. We validate the resulting loop on a mobile manipulator with an eye-in-hand D405 camera, keeping the underlying grasp model unchanged and evaluating representative scenarios involving visual ambiguity, distractors, and induced execution failures. Results show that explicit execution-state monitoring and bounded recovery enable more robust and interpretable behavior than open-loop execution, while adding minimal architectural overhead. For the source code and demo refer to our project page: https://wenzewwz123.github.io/Agentic-Loop/
