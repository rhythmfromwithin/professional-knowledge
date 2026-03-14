---
title: "DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.11076
priority: high
status: unread
interest: medium
next_step: skim
---
# DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use
> 原文: [https://arxiv.org/abs/2603.11076](https://arxiv.org/abs/2603.11076)

arXiv:2603.11076v1 Announce Type: new
Abstract: Recent work synthesizes agentic tasks for post-training tool-using LLMs, yet robust generalization under shifts in tasks and toolsets remains an open challenge. We trace this brittleness to insufficient diversity in synthesized tasks. Scaling diversity is difficult because training requires tasks to remain executable and verifiable, while generalization demands coverage of diverse tool types, toolset combinations, and heterogeneous tool-use patterns. We propose DIVE, an evidence-driven recipe that inverts synthesis order, executing diverse, real-world tools first and reverse-deriving tasks strictly entailed by the resulting traces, thereby providing grounding by construction. DIVE scales structural diversity along two controllable axes, tool-pool coverage and per-task toolset variety, and an Evidence Collection--Task Derivation loop further induces rich multi-step tool-use patterns across 373 tools in five domains. Training Qwen3-8B on DIVE data (48k SFT + 3.2k RL) improves by +22 average points across 9 OOD benchmarks and outperforms the strongest 8B baseline by +68. Remarkably, controlled scaling analysis reveals that diversity scaling consistently outperforms quantity scaling for OOD generalization, even with 4x less data.
