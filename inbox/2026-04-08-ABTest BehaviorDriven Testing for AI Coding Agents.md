---
interest: medium
link: https://arxiv.org/abs/2604.03362
next_step: skim
priority: low
slack_ts: '1775618432.381139'
source: cs.SE - Software Engineering
status: unread
title: 'ABTest: Behavior-Driven Testing for AI Coding Agents'
---
# ABTest: Behavior-Driven Testing for AI Coding Agents
> 原文: [https://arxiv.org/abs/2604.03362](https://arxiv.org/abs/2604.03362)

arXiv:2604.03362v1 Announce Type: new
Abstract: AI coding agents are increasingly integrated into real-world software development workflows, yet their robustness under diverse and adversarial scenarios remains poorly understood. We present ABTest, a behavior-driven fuzzing framework that systematically tests coding agents by turning real-world failure reports into repository-grounded behavioral tests. ABTest (1) mines user-reported anomalies to derive reusable workflow patterns (Interaction Patterns) and behaviors (Action types); (2) composes them into stepwise fuzzing templates; (3) instantiates executable test cases in real repositories; (4) executes them with coding agents while recording traces and artifacts; and (5) detects and validates anomalous behaviors.
We apply ABTest to three widely used coding agents: Claude Code, OpenAI Codex CLI, and Gemini CLI. From 400 user-reported developer-confirmed agent failures, we extract 47 Interaction Patterns and 128 Action types, generating 647 repository-grounded fuzzing cases. Executing the 647-case bundle once per evaluated configuration, ABTest flags 1,573 behavioral anomalies across the three coding agent families, of which 642 are manually confirmed as new true anomalies, achieving a detection precision of 40.8%. Our results demonstrate that ABTest effectively uncovers real-world failures, exposes robustness differences across models, and reveals previously unreported failure modes.
