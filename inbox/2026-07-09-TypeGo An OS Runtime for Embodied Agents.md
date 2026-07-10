---
interest: medium
link: https://arxiv.org/abs/2607.05482
next_step: skim
priority: low
slack_ts: '1783655935.647339'
source: cs.SE - Software Engineering
status: unread
title: 'TypeGo: An OS Runtime for Embodied Agents'
---
# TypeGo: An OS Runtime for Embodied Agents
> 原文: [https://arxiv.org/abs/2607.05482](https://arxiv.org/abs/2607.05482)

arXiv:2607.05482v1 Announce Type: new
Abstract: Large language models (LLMs) can plan behavior for embodied agents from natural language, but treating the LLM as a request/response oracle on the critical path is fundamentally at odds with real-time control and concurrent goals. We argue for an operating-system-style runtime for embodied agents, and instantiate this idea in an early prototype, TypeGo. TypeGo structures LLM-based planning as asynchronous loops at multiple timescales that overlap with execution, and manages the agent's physical body like an OS manages hardware: the Skill Kernel arbitrates typed physical subsystems among concurrent per-task processes, a scheduler preempts them and resumes or replaces each by source, and speculative skill streaming hides LLM latency behind ongoing motion, while a fast first-action path yields visible feedback within a second. Users program behavior through natural language prescriptions that TypeGo dispatches to the LLM-based planners or compiles into low-latency interrupt handlers. Our prototype of Kalos, a Unitree Go2 quadruped, provides preliminary evidence for the design: in our current task suite, it cuts per-step delay by 50% over step-by-step planning and time-to-first-action by 73% over monolithic planning, while admitting concurrent tasks at low scheduling overhead.
