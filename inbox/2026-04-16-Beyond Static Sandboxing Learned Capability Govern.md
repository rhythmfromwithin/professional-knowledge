---
title: "Beyond Static Sandboxing: Learned Capability Governance for Autonomous AI Agents"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.11839
priority: low
status: unread
interest: medium
next_step: skim
---
# Beyond Static Sandboxing: Learned Capability Governance for Autonomous AI Agents
> 原文: [https://arxiv.org/abs/2604.11839](https://arxiv.org/abs/2604.11839)

arXiv:2604.11839v1 Announce Type: new
Abstract: Autonomous AI agents built on open-source runtimes such as OpenClaw expose every available tool to every session by default, regardless of the task. A summarization task receives the same shell execution, subagent spawning, and credential access capabilities as a code deployment task, a 15x overprovision ratio that we call the capability overprovisioning problem. Existing defenses, including the NemoClaw container sandbox and the Cisco DefenseClaw skill scanner, address containment and threat detection but do not learn the minimum viable capability set for each task type.
We present Aethelgard, a four layer adaptive governance framework that enforces least privilege for AI agents through a learned policy. Layer 1, the Capability Governor, dynamically scopes which tools the agent is aware of in each session. Layer 3, the Safety Router, intercepts tool calls before execution using a hybrid rule based and fine tuned classifier. Layer 2, the RL Learning Policy, trains a PPO policy on the accumulated audit log to learn the minimum viable skill set for each task type.
