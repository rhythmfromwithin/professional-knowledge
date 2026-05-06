---
title: "Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.00827
priority: medium
status: unread
interest: medium
next_step: skim
---
# Separating Intelligence from Execution: A Workflow Engine for the Model Context Protocol
> 原文: [https://arxiv.org/abs/2605.00827](https://arxiv.org/abs/2605.00827)

arXiv:2605.00827v1 Announce Type: new
Abstract: Large Language Model (LLM) agents increasingly interact with external systems through tool-calling protocols such as the Model Context Protocol (MCP). In prevailing architectures, the agent must reason about every tool invocation in every session, consuming tokens proportional to the number of actions performed--even when the task has been solved before. We present the MCP Workflow Engine, a novel MCP-native orchestration layer that decouples intelligence (deciding what to do) from execution (carrying it out). An agent reasons once to produce a declarative workflow blueprint--a JSON document specifying a directed sequence of MCP tool calls with parameterized templates, loops, parallel branches, and data piping. Subsequent executions are triggered by a single run\_workflow tool call, consuming one invocation's worth of tokens regardless of the blueprint's internal complexity. We formalize the MCP Mediator architectural pattern--an MCP server that simultaneously acts as a client to downstream MCP servers--and implement it in TypeScript against the MCP SDK. We evaluate the engine on a production-scale Kubernetes CMDB synchronization task spanning 67 orchestrated steps across 2 MCP servers, 38 namespaces, 13 worker nodes, and 22 distinct resource types. The engine reduces per-execution token cost by over 99%, completes the full cluster graph--comprising 1,200+ nodes and 2,800+ relationships across 20 relationship types--in under 45 seconds, and achieves deterministic, idempotent execution with zero agent involvement at run time.
