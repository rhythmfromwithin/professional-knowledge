---
title: "Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.04466
priority: medium
status: unread
interest: medium
next_step: skim
---
# Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation
> 原文: [https://arxiv.org/abs/2603.04466](https://arxiv.org/abs/2603.04466)

arXiv:2603.04466v1 Announce Type: new
Abstract: Can a multimodal language model learn to manipulate physical objects by reasoning about its own failures-without gradient updates, demonstrations, or reward engineering? We argue the answer is yes, under conditions we characterise precisely. We present Act-Observe-Rewrite (AOR), a framework in which an LLM agent improves a robot manipulation policy by synthesising entirely new executable Python controller code between trials, guided by visual observations and structured episode outcomes. Unlike prior work that grounds LLMs in pre-defined skill libraries or uses code generation for one-shot plan synthesis, AOR makes the full low-level motor control implementation the unit of LLM reasoning, enabling the agent to change not just what the robot does, but how it does it. The central claim is that interpretable code as the policy representation creates a qualitatively different kind of in-context learning from opaque neural policies: the agent can diagnose systematic failures and rewrite their causes. We validate this across three robosuite manipulation tasks and report promising results, with the agent achieving high success rates without demonstrations, reward engineering, or gradient updates.
