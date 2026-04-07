---
interest: medium
link: https://arxiv.org/abs/2604.02375
next_step: skim
priority: low
slack_ts: '1775531930.273839'
source: cs.SE - Software Engineering
status: unread
title: 'KAIJU: An Executive Kernel for Intent-Gated Execution of LLM Agents'
---
# KAIJU: An Executive Kernel for Intent-Gated Execution of LLM Agents
> 原文: [https://arxiv.org/abs/2604.02375](https://arxiv.org/abs/2604.02375)

arXiv:2604.02375v1 Announce Type: new
Abstract: Tool-calling autonomous agents based on large language models using ReAct exhibit three limitations: serial latency, quadratic context growth, and vulnerability to prompt injection and hallucination. Recent work moves towards separating planning from execution but in each case the model remains coupled to the execution mechanics. We introduce a system-level abstraction for LLM agents which decouples the execution of agent workflows from the LLM reasoning layer. We define two first-class abstractions: (1) Intent-Gated Execution (IGX), a security paradigm that enforces intent at execution, and (2) an Executive Kernel that manages scheduling, tool dispatch, dependency resolution, failures and security. In KAIJU, the LLM plans upfront, optimistically scheduling tools in parallel with dependency-aware parameter injection. Tools are authorised via IGX based on four independent variables: scope, intent, impact, and clearance (external approval). KAIJU supports three adaptive execution modes (Reflect, nReflect, and Orchestrator), providing progressively finer-grained execution control apt for complex investigation and deep analysis or research. Empirical evaluation against a ReAct baseline shows that KAIJU has a latency penalty on simple queries due to planning overhead, convergence at moderate complexity, and a structural advantage on computational queries requiring parallel data gathering. Beyond latency, the separation enforces behavioural guarantees that ReAct cannot match through prompting alone. Code available at https://github.com/compdeep/kaiju
