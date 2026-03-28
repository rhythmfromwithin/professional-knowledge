---
interest: medium
link: https://arxiv.org/abs/2603.24703
next_step: skim
priority: low
slack_ts: '1774666236.070599'
source: cs.SE - Software Engineering
status: unread
title: 'IndustriConnect: MCP Adapters and Mock-First Evaluation for AI-Assisted Industrial
  Operations'
---
# IndustriConnect: MCP Adapters and Mock-First Evaluation for AI-Assisted Industrial Operations
> 原文: [https://arxiv.org/abs/2603.24703](https://arxiv.org/abs/2603.24703)

arXiv:2603.24703v1 Announce Type: new
Abstract: AI assistants can decompose multi-step workflows, but they do not natively speak industrial protocols such as Modbus, MQTT/Sparkplug B, or OPC UA, so this paper presents INDUSTRICONNECT, a prototype suite of Model Context Protocol (MCP) adapters that expose industrial operations as schema-discoverable AI tools while preserving protocol-specific connectivity and safety controls; the system uses a common response envelope and a mock-first workflow so adapter behavior can be exercised locally before connecting to plant equipment, and a deterministic benchmark covering normal, fault-injected, stress, and recovery scenarios evaluates the flagship adapters, comprising 870 runs (480 normal, 210 fault-injected, 120 stress, 60 recovery trials) and 2820 tool calls across 7 fault scenarios and 12 stress scenarios, where the normal suite achieved full success, the fault suite confirmed structured error handling with adapter-level uint16 range validation, the stress suite identified concurrency boundaries, and same-session recovery after endpoint restart is demonstrated for all three protocols, with results providing evidence spanning adapter correctness, concurrency behavior, and structured error handling for AI-assisted industrial operations.
