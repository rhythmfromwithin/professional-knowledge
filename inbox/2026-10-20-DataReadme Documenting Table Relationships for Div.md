---
interest: medium
link: https://arxiv.org/abs/2610.25131
next_step: skim
priority: low
slack_ts: '1792556396.564849'
source: cs.DB - Databases
status: unread
title: 'Data.Readme: Documenting Table Relationships for Diverse Data Tasks'
---
# Data.Readme: Documenting Table Relationships for Diverse Data Tasks
> 原文: [https://arxiv.org/abs/2610.25131](https://arxiv.org/abs/2610.25131)

arXiv:2610.25131v1 Announce Type: new
Abstract: Large language models (LLMs) can perform diverse data tasks when given a small set of relevant tables. However, for complex tasks requiring multiple tables over large data lakes, identifying relevant tables for the task becomes a prerequisite, but remains challenging. This is because there are often many tables in a data lake with similar table and schema names, and limited additional semantic context, thereby forcing agents to spend substantial time exploring tables at online query time, greatly affecting models' ability to perform tasks accurately, while increasing cost/latency substantially.
We present Data.Readme, a novel table documentation approach that uses lightweight offline processing to infer and index rich \emph{table-to-table relationships}, including confusable, joinable, and union-able tables. We further develop a suite of agentic tools for LLMs to work with the index, to help agents retrieve relevant tables and perform tasks much more efficiently and effectively. Finally, we study how to optimize our index construction with a budget constraint. On data lakes containing up to 12K tables, Data.Readme improves task accuracy by as much as 40 percentage points across a range of data discovery, data analysis, and data science tasks, outperforming diverse baselines, including powerful coding agents with unlimited time and monetary budgets. We also show that equipping existing methods (such as coding agents) with Data.Readme can not only lead to consistent quality gains, but also significantly reduce their latency by up to 6x, demonstrating the potential of Data.Readme.
