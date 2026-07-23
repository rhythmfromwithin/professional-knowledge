---
interest: medium
link: https://arxiv.org/abs/2607.15684
next_step: skim
priority: low
slack_ts: '1784777489.994839'
source: cs.SE - Software Engineering
status: unread
title: 'Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical
  Study of LLM Agent Issue Reports'
---
# Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports
> 原文: [https://arxiv.org/abs/2607.15684](https://arxiv.org/abs/2607.15684)

arXiv:2607.15684v1 Announce Type: new
Abstract: LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context. Both the harness and LLM-generated responses jointly shape an agent's execution. This architecture gives rise to bugs that cannot be readily understood by inspecting either component alone, because some bugs occur only when a particular LLM response elicits an abnormal reaction from the agent. Prior empirical studies of agent bugs have largely attributed failures either to limited model capabilities or to harness-side defects, such as outdated APIs and configuration misalignment, without characterizing these AR bugs. We conduct the first empirical study focused on agent-reactive (AR) bugs. Through manual analysis of 255 bug reports from Codex, Gemini-CLI, LangChain, and CrewAI, we construct a two-axis taxonomy covering observable symptoms and the LLM behaviors that trigger them. Our findings show that many AR bugs manifest as silent errors without well-defined test oracles, which makes detection difficult. The stochasticity of LLM responses further complicates bug reproduction. We additionally examine fixes proposed by users and implemented by developers. This analysis exposes a mismatch: users frequently advocate harness-side guardrails, whereas developers may attribute the issue to the LLM or respond slowly to user-proposed fixes. These findings point to the need for mechanisms that help users and developers understand the root causes and resolutions of AR bugs. Overall, the study highlights challenges specific to LLM agents and motivates the design of test oracles, reproduction support, and fault-localization techniques for AR bugs.
