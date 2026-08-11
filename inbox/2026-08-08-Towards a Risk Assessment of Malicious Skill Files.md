---
interest: medium
link: https://arxiv.org/abs/2608.05223
next_step: skim
priority: low
slack_ts: '1786414343.365499'
source: cs.SE - Software Engineering
status: unread
title: Towards a Risk Assessment of Malicious Skill Files in Coding Agents
---
# Towards a Risk Assessment of Malicious Skill Files in Coding Agents
> 原文: [https://arxiv.org/abs/2608.05223](https://arxiv.org/abs/2608.05223)

arXiv:2608.05223v1 Announce Type: new
Abstract: Autonomous coding agents are increasingly embedded in enterprise software workflows with delegated authority over connected systems. Central to this architecture is the agent skills interface: folders of instructions and scripts that agents load dynamically to specialize their behavior. This interface also widens the attack surface, letting malicious shell commands hide within natural-language skill files. We make three contributions. First, an adversarial skill-synthesis method using six LLMs across four families to transform 471 real-world shell commands into benign-appearing skills, released as a benchmark of 2,826 skills mapped to 11 MITRE ATT&CK tactics. Second, a reproducible evaluation pipeline coupling run stratification, evidence anchoring, a refusal veto, and a deterministic declared-intent override with a three-judge LLM-as-a-judge panel, validated against a blind human gold standard (Cohen's kappa = 0.85). Third, a large-scale characterization of two enterprise-grade agents across 5,629 completed runs. Gemini CLI is exploited in 95.5-96.1% of runs and Qwen Code in 71.6-74.0% (raw majority vote to declared-intent-corrected estimate, both within the human gold standard), nearly invariant to the generating model. Explicit safety recognition occurs in only 1.99% of runs. Enterprises must assess and mitigate skill-interface risk before adopting coding agents. Our code and dataset are available at https://github.com/awsm-research/AgentJailbreak
