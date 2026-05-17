---
interest: medium
link: https://arxiv.org/abs/2605.13940
next_step: skim
priority: low
slack_ts: '1778990763.125499'
source: cs.CR - Cryptography and Security
status: unread
title: 'AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills'
---
# AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills
> 原文: [https://arxiv.org/abs/2605.13940](https://arxiv.org/abs/2605.13940)

arXiv:2605.13940v1 Announce Type: new
Abstract: Third-party skills are becoming the package ecosystem for LLM agents. They package natural-language instructions, helper scripts, templates, documents, and service configuration into reusable workflows. This makes skills useful, but it also introduces a new security problem: a malicious skill does not need to ask the model to perform an obviously harmful action. Instead, it can disguise the harmful behavior as part of a routine workflow, relying on the agent to execute that workflow with high-value permissions and limited human supervision.
We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior. AgentTrap contains 141 tasks: 91 malicious tasks and 50 benign utility tasks, covering 16 security-impact dimensions grounded in agent-skill supply-chain threats. In each task, the agent receives an ordinary user request, runs with installed skills that may contain malicious workflow elements, and is executed in a sandboxed environment. AgentTrap then judges complete trajectories for attack success, blocked or refused behavior, attack-not-triggered cases, and no-attack-evidence outcomes. Our central finding is that the most informative failures are not simple jailbreaks. Models often complete the visible user task while treating unsafe side effects introduced by the skill as part of the normal workflow. This motivates runtime evaluation of the concrete model--framework--workspace environment in which users actually delegate work. Code and data are available at https://github.com/zhmzm/AgentTrap and https://huggingface.co/datasets/zhmzm/AgentTrap.
