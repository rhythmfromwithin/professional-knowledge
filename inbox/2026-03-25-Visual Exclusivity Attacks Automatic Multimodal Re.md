---
title: "Visual Exclusivity Attacks: Automatic Multimodal Red Teaming via Agentic Planning"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.20198
priority: low
status: unread
interest: medium
next_step: skim
---
# Visual Exclusivity Attacks: Automatic Multimodal Red Teaming via Agentic Planning
> 原文: [https://arxiv.org/abs/2603.20198](https://arxiv.org/abs/2603.20198)

arXiv:2603.20198v1 Announce Type: new
Abstract: Current multimodal red teaming treats images as wrappers for malicious payloads via typography or adversarial noise. These attacks are structurally brittle, as standard defenses neutralize them once the payload is exposed. We introduce Visual Exclusivity (VE), a more resilient Image-as-Basis threat where harm emerges only through reasoning over visual content such as technical schematics. To systematically exploit VE, we propose Multimodal Multi-turn Agentic Planning (MM-Plan), a framework that reframes jailbreaking from turn-by-turn reaction to global plan synthesis. MM-Plan trains an attacker planner to synthesize comprehensive, multi-turn strategies, optimized via Group Relative Policy Optimization (GRPO), enabling self-discovery of effective strategies without human supervision. To rigorously benchmark this reasoning-dependent threat, we introduce VE-Safety, a human-curated dataset filling a critical gap in evaluating high-risk technical visual understanding. MM-Plan achieves 46.3% attack success rate against Claude 4.5 Sonnet and 13.8% against GPT-5, outperforming baselines by 2--5x where existing methods largely fail. These findings reveal that frontier models remain vulnerable to agentic multimodal attacks, exposing a critical gap in current safety alignment. Warning: This paper contains potentially harmful content.
