---
interest: medium
link: https://arxiv.org/abs/2605.27489
next_step: skim
priority: low
slack_ts: '1780202378.700549'
source: cs.CR - Cryptography and Security
status: unread
title: 'HARP: Measuring Harm Amplification in Multi-Agent LLM Systems'
---
# HARP: Measuring Harm Amplification in Multi-Agent LLM Systems
> 原文: [https://arxiv.org/abs/2605.27489](https://arxiv.org/abs/2605.27489)

arXiv:2605.27489v1 Announce Type: new
Abstract: Multi-agent LLM systems decompose workflows across agents, tools, shared context, memory, and decision gates. This modularity improves interpretability, but creates a propagation risk: a bounded perturbation to one component can be reused by other agents and amplified into system-level harm. We introduce HARP (Harm Amplification through Role Perturbation), a trace-first methodology for studying local-to-global harm amplification in multi-agent LLM systems. HARP compares paired clean and perturbed executions and records specialist outputs, tool calls, memory reads/writes, guard events, oracle logs, latency, token cost, and decisions. We define local harm as deviation from targeted agents or corrupted channels, global harm as deviation over the full trace, and harm amplification as (H\_global/H\_local). This complements attack success rate with a measure of how strongly orchestration spreads harm beyond the attack point. We instantiate HARP in a finance-oriented seven-agent system with a deterministic decision gate and configurable attack harness for specialist compromise, collusion, shared-context corruption, and temporal or memory-persistent attacks. Across five defenses, prompt-only defenses preserve benign utility but leave high success and stealth; pre-tool and step-level guards reduce some failures with utility or latency costs; and IntegrityGuard, a trace-consistency defense, achieves the lowest attack success and global harm but introduces utility/cost trade-offs. Results show that single-specialist compromise produces the strongest amplification, shared-context corruption yields the highest attack success, and temporal persistence produces the largest malicious impact. HARP argues that secure multi-agent evaluation must measure not only bypass, but propagation.
