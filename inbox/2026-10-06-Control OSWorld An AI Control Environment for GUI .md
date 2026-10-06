---
interest: medium
link: https://arxiv.org/abs/2610.03818
next_step: skim
priority: low
slack_ts: '1791266358.804679'
source: cs.CR - Cryptography and Security
status: unread
title: 'Control OSWorld: An AI Control Environment for GUI Computer Use Agents'
---
# Control OSWorld: An AI Control Environment for GUI Computer Use Agents
> 原文: [https://arxiv.org/abs/2610.03818](https://arxiv.org/abs/2610.03818)

arXiv:2610.03818v1 Announce Type: new
Abstract: AI agents that operate a computer through its graphical user interface (GUI) are being widely deployed. AI control studies how to prevent an AI system from causing harm even if it is misaligned and actively trying to do so. Most control research to date has focused on coding agents, leaving computer use largely unexplored. We introduce Control OSWorld, a control evaluation that pairs 318 tasks from OSWorld with 81 harmful side tasks (e.g., exfiltrating a private file) that an agent must complete without being caught. We use Control OSWorld to create and study control monitors that detect malicious agents interacting with a GUI. We find that a weaker monitor can reliably distinguish honest from malicious trajectories produced by a more capable agent when it sees the full trajectory (97% recall at 3% false positive rate). However, when the monitor has to score each step before it is executed, recall drops at low false positive rates because each action is judged with less context. Monitor performance also depends on what the monitor can see: access to the agent's visible text is critical, while screenshots provide little additional value.
