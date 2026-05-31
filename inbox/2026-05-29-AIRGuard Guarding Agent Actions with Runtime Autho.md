---
interest: medium
link: https://arxiv.org/abs/2605.28914
next_step: skim
priority: low
slack_ts: '1780202382.534499'
source: cs.CR - Cryptography and Security
status: unread
title: 'AIRGuard: Guarding Agent Actions with Runtime Authority Control'
---
# AIRGuard: Guarding Agent Actions with Runtime Authority Control
> 原文: [https://arxiv.org/abs/2605.28914](https://arxiv.org/abs/2605.28914)

arXiv:2605.28914v1 Announce Type: new
Abstract: Tool-using language agents turn model decisions into external side effects: they read files, run scripts, call APIs, send messages, and invoke Model Context Protocol tools. This makes agent attacks different from jailbreaks. The harmful step is often not an obviously forbidden output, but an ordinary executable action that becomes unsafe because attacker-controlled context steers authorized access against the user's interest. We identify this failure mode as authority confusion: untrusted resources may inform reasoning, but they must not authorize side effects. We present AIRGuard, a runtime guard that operationalizes least privilege as action-time authorization. AIRGuard normalizes heterogeneous tool calls, derives task authority into step-level authority, tracks source and target trust, simulates sensitive side effects, audits cross-step risk, and enforces decisions before actions execute. On AgentTrap, AIRGuard reduces Sonnet 4.6 attack success from 36.3% without defense to 5.5%. On DTAP-150, AIRGuard preserves 76.0% benign utility with Haiku 4.5, compared with 52.0% for ARGUS and 42.0% for MELON. An ablation further shows that prompt-only policy helps only modestly, whereas a dedicated runtime authority-control layer gives the agent system direct control over tool-mediated side effects. Code and data are available at https://github.com/Sophie508/AIRGuard.
