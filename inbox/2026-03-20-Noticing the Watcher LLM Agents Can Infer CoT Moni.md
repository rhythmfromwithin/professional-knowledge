---
title: "Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.16928
priority: low
status: unread
interest: medium
next_step: skim
---
# Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback
> 原文: [https://arxiv.org/abs/2603.16928](https://arxiv.org/abs/2603.16928)

arXiv:2603.16928v1 Announce Type: new
Abstract: Chain-of-thought (CoT) monitoring is proposed as a method for overseeing the internal reasoning of language-model agents. Prior work has shown that when models are explicitly informed that their reasoning is being monitored, or are fine-tuned to internalize this fact, they may learn to obfuscate their CoTs in ways that allow them to evade CoT-based monitoring systems. We ask whether reasoning agents can autonomously infer that their supposedly private CoT is under surveillance, and whether this awareness leads to strategic evasion, without any explicit training or instructions. In a multi-episode agentic framework, models pursue both a primary task and a concealed side task while being told that their reasoning is private; a hidden CoT monitor blocks episodes when suspicious reasoning is detected. We find that frontier models can deduce the existence of this monitor purely from blocking feedback, with the most capable models reaching a confident belief that their thinking is observed in up to 19% of episodes. This awareness scales with model capability and, in rare cases, escalates to an explicit intent to suppress reasoning about the side task. However, models that form this intent uniformly fail to execute it, openly reasoning about their concealed objectives in the very next episode. This intent-capability gap is reassuring for current deployment, but the autonomous emergence of both monitoring awareness and evasion intent suggests that CoT monitoring is not a permanently reliable safeguard.
