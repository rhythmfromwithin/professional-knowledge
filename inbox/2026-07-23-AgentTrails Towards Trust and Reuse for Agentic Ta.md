---
interest: medium
link: https://arxiv.org/abs/2607.18816
next_step: skim
priority: low
slack_ts: '1784863626.377549'
source: cs.DB - Databases
status: unread
title: 'AgentTrails: Towards Trust and Reuse for Agentic Tasks'
---
# AgentTrails: Towards Trust and Reuse for Agentic Tasks
> 原文: [https://arxiv.org/abs/2607.18816](https://arxiv.org/abs/2607.18816)

arXiv:2607.18816v1 Announce Type: new
Abstract: LLM-powered agents increasingly tackle complex tasks by invoking tools, querying databases, executing code, and manipulating intermediate artifacts. These agents follow trajectories that are typically stored as chronological logs, obscuring the underlying dataflow -- the dependencies between their actions and the artifacts they create and manipulate. This limits developers' ability to understand the agents' trails, compare executions, debug failures, and re-use the computations. We present AgentTrails, a prototype system for agent provenance and sensemaking. AgentTrails converts raw trajectories into structured provenance graphs, where tool calls are modeled as computational actions and inputs and outputs as data artifacts. The system supports the comparison of executions by placing multiple provenance graphs on a shared canvas and constructing a joined quotient graph that aligns recurring tools, artifacts, and dependency structures across trajectories. On top of this representation, AgentTrails supports pattern extraction, downstream analysis, and skill abstraction. We demonstrate AgentTrails on real-world agent trajectories, showing that it reveals hidden dependencies, aligns divergent executions, and surfaces recurring tool-use patterns beyond chronological logs.
