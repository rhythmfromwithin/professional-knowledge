---
interest: medium
link: https://arxiv.org/abs/2605.24069
next_step: skim
priority: low
slack_ts: '1779768855.008729'
source: cs.CR - Cryptography and Security
status: unread
title: 'When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks
  for LLM Agents'
---
# When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents
> 原文: [https://arxiv.org/abs/2605.24069](https://arxiv.org/abs/2605.24069)

arXiv:2605.24069v1 Announce Type: new
Abstract: The rise of tool-using Large Language Model (LLM) agents, standardized by protocols like the Model Context Protocol (MCP), has unlocked unprecedented autonomous execution capabilities for LLM Agents by integrating external open-domain knowledge and tools. However, this interoperability introduces a covert attack surface targeting the agent's cognitive planning layer. This paper systematically investigates Tool Description Poisoning (TDP), a novel semantic attack. In TDP, malicious instructions are not embedded in a tool's executable code, but rather covertly injected into its descriptive metadata, the very "manual" an agent relies on for secure planning and decision-making. To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark. This high-fidelity sandbox environment comprises 32 realistic, real-world test cases spanning 6 distinct risk categories. Our evaluation of 8 mainstream LLMs reveals severe vulnerabilities, with leading models like GPT-4o exhibiting a nearly 100% Attack Success Rate (ASR) in six high-risk scenarios. Furthermore, our findings demonstrate that common prompt-guardrail defenses are largely ineffective and can, counterintuitively, even be counterproductive (a phenomenon which we term the "Firewall Fallacy"). Crucially, we also propose a defense mechanism: "Reactive Self-Correction," where an agent autonomously detects and reverts its own malicious actions post-execution. This work provides the first specialized security benchmark tailored for TDP, offering essential insights for securing the cognitive and planning layers of advanced agentic systems.
