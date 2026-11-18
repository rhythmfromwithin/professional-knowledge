---
interest: medium
link: https://arxiv.org/abs/2611.21645
next_step: skim
priority: low
slack_ts: '1794985134.537149'
source: cs.DB - Databases
status: unread
title: 'Asking What Matters: Disagreement-Guided Ambiguity Detection for Interactive
  Text-to-SQL'
---
# Asking What Matters: Disagreement-Guided Ambiguity Detection for Interactive Text-to-SQL
> 原文: [https://arxiv.org/abs/2611.21645](https://arxiv.org/abs/2611.21645)

arXiv:2611.21645v1 Announce Type: new
Abstract: Interactive text-to-SQL requires an LLM agent not only to generate executable SQL, but also to decide which uncertainty to clarify within a limited interaction budget. However, current clarification policies have three limitations: (i) they target surface ambiguity without testing its SQL impact; (ii) they miss ambiguities implicit in schema routes or domain knowledge; and (iii) they spend limited turns on unfocused or redundant questions. These limitations expose a critical challenge: identifying SQL-impacting ambiguity before the intended SQL is known. In this paper, we propose DisGuAD, a Disagreement-Guided Ambiguity Detection framework that specializes clarification selection. DisGuAD treats disagreement among plausible SQL interpretations as direct evidence of which uncertainty matters to the final query. Specifically, it constructs a query-term inventory, elicits contrastive SQL interpretations through complementary probe families, compares their canonical SQL components, and attributes recurring differences to user-facing clarification targets. A lightweight prioritization and dialogue-state mechanism then selects one high-impact unresolved target for clarification. Experiments on BIRD-Interact Lite and Full with two LLM backbones demonstrate consistent improvements in task success and clarification quality. Compared with the original interaction policy, DisGuAD improves normalized Reward by 4.40--8.97 points and raises overall critical-ambiguity coverage from 48.62% to 82.75% and from 45.76% to 85.14%. Its clarification signals further improve two independently designed static text-to-SQL frameworks by up to 13.97 Reward points while keeping their SQL generators fixed. These results demonstrate that disagreement among plausible SQL queries provides actionable evidence for selecting clarification targets that matter to downstream generation.
