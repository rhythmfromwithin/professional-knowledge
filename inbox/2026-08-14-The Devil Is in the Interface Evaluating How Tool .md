---
title: "The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.11386
priority: low
status: unread
interest: medium
next_step: skim
---
# The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior
> 原文: [https://arxiv.org/abs/2608.11386](https://arxiv.org/abs/2608.11386)

arXiv:2608.11386v1 Announce Type: new
Abstract: As large language models continue to improve, agentic systems are becoming increasingly important, and tools are a key design dimension because they determine how agents access information and take action in their environments. Prior work on agent tooling has primarily focused on expanding what agents can do, but has paid less systematic attention to how those capabilities are organized and exposed to the model. We refer to this latter design dimension as tool architecture. We study tool architecture in coding agents through controlled experiments on repository-level issue fixing, comparing six tool architectures that hold the underlying information and actions similar while varying how they are organized and exposed to the model, across three actors and a total of 11,700 trajectories. Our experiments show that, even when tools provide similar capabilities, tool architecture changes agent behavior: Compared to a basic architecture where the agent has only the bash tool, more structured low-level interfaces improve consistency across repeated attempts by up to 4.7 $\times$; natural-language search broadens repository exploration and increases access to relevant files by more than 11%; and Python CodeAct-style interfaces achieve similar task performance with 41.6% fewer steps and 56.3% lower token usage. By contrast, lightweight text-based cognitive-scaffolding tools, such as tools that let the agent record intermediate reasoning, have limited effect on actor behavior.
