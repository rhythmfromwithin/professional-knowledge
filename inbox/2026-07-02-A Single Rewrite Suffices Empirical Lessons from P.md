---
interest: medium
link: https://arxiv.org/abs/2606.30775
next_step: skim
priority: high
slack_ts: '1782965351.614919'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'A Single Rewrite Suffices: Empirical Lessons from Production Skill Description
  Optimization'
---
# A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization
> 原文: [https://arxiv.org/abs/2606.30775](https://arxiv.org/abs/2606.30775)

arXiv:2606.30775v1 Announce Type: new
Abstract: Enterprise AI agents route user queries to specialized skills by matching queries against natural language skill descriptions. When two skills share overlapping descriptions, the routing LLM misroutes queries, a failure we term skill collision. As agents scale to dozens of skills, manually tuning descriptions to maintain routing accuracy becomes a significant engineering bottleneck. We deploy an automated description optimization pipeline on a production enterprise group chat agent (9 skills, 372 regression cases). The pipeline produces descriptions averaging 79.2% F1, matching manually tuned descriptions at 79.4% F1 (average per-skill difference -0.20%, within the 0.78% multi-seed noise floor), while reducing per-skill engineering effort from 120 minutes to 3.8 minutes (32 times speedup). We then examine which pipeline components actually drive this match. Systematic ablation on both the production system and ToolBench (16k tools) reveals that a single LLM rewrite using any available false-positive and false-negative cases captures most of the available improvement. Other design choices we tested (iteration budget, feedback signal composition, dual editing of confused pairs, and training set size) each affect final F1 by less than 0.5%. Description optimization addresses skill collisions caused by overlapping descriptions but cannot resolve cases where two skills intended scopes genuinely overlap. We identify a diagnostic (a large train-validation F1 gap) that flags the latter cases for architectural rather than text-level intervention.
