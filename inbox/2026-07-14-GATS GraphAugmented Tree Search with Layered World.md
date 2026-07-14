---
interest: medium
link: https://arxiv.org/abs/2607.08894
next_step: skim
priority: high
slack_ts: '1783998912.199969'
source: cs.AI - Artificial Intelligence
status: unread
title: 'GATS: Graph-Augmented Tree Search with Layered World Models for Efficient
  Agent Planning'
---
# GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning
> 原文: [https://arxiv.org/abs/2607.08894](https://arxiv.org/abs/2607.08894)

arXiv:2607.08894v1 Announce Type: new
Abstract: Large Language Model (LLM) agents have shown promise in multi-step planning tasks, but existing approaches like LATS (Language Agent Tree Search) and ReAct rely heavily on LLM inference during planning, leading to high computational costs and stochastic behavior. We present \textbf{GATS} (Graph-Augmented Tree Search), a planning framework that combines systematic UCB1-based tree search with a layered world model to eliminate LLM calls during inference while achieving superior planning performance. Our three-layer world model integrates: (L1) exact symbolic action matching, (L2) statistics learned from execution logs, and (L3) LLM-based prediction for unknown actions. On synthetic planning tasks with branching paths and dead-ends, GATS achieves \textbf{100\% success rate} compared to 92 % for LATS and 64\% for ReAct. On a comprehensive stress test spanning 12 challenging scenarios -- including coding workflows, web navigation, and long-horizon tasks -- GATS maintains \textbf{100\% success} while LATS drops to 88.9 % and ReAct to 23.9%. GATS requires \textbf{zero LLM calls per task} during planning (vs. 37 per task for LATS) and produces deterministic plans with zero variance across runs. Our results demonstrate that systematic search with learned world models can substantially outperform LLM-guided exploration for agent planning.
