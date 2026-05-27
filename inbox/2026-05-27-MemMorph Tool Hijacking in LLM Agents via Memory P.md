---
title: "MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.26154
priority: low
status: unread
interest: medium
next_step: skim
---
# MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning
> 原文: [https://arxiv.org/abs/2605.26154](https://arxiv.org/abs/2605.26154)

arXiv:2605.26154v1 Announce Type: new
Abstract: LLM-driven agents are capable of selecting external tools to complete users' tasks. However, attackers could compromise such process, steering agents toward inappropriate/wrong tools and enabling malicious actions. Most existing attacks primarily manipulate the tool metadata, which is easily detectable by auditing and may lose effectiveness as modern agents increasingly adopt memory modules to refine tool selection policies through accumulated experience. This paper proposes MemMorph, the first attack that bias tool selection by poisoning the agent's long-term memory. Rather than explicitly dictating the tool invocation decision, MemMorph injects a small number of crafted records that are disguised as technical facts, incident reports, and operational policies. These poisoned records reshape the agent's contextual perception and decision-making process, leading it to autonomously infer and select the tool preferred by the attacker. Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. Our findings expose long-term memory as a critical and under-explored attack surface in tool-augmented agents, urging the development of memory-level integrity safeguards.
