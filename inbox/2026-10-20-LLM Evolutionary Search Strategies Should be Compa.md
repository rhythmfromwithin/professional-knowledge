---
interest: medium
link: https://arxiv.org/abs/2610.23977
next_step: skim
priority: low
slack_ts: '1792556403.138799'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: LLM Evolutionary Search Strategies Should be Compared by Tokens
---
# LLM Evolutionary Search Strategies Should be Compared by Tokens
> 原文: [https://arxiv.org/abs/2610.23977](https://arxiv.org/abs/2610.23977)

arXiv:2610.23977v1 Announce Type: new
Abstract: LLM evolutionary search is currently evaluated by counting proposals (candidate programs). We demonstrate this metric hides the true cost of search, and redo the comparison using tokens. By replaying 600 logged runs across 5 tasks and 3 methods, we show that proposal costs vary wildly from 16k to 39k tokens. In equal-proposal comparisons, this silently grants some methods up to 1.9x the compute of others, and gives evolution roughly 6x the budget of independent sampling. When we match token budgets, giving sampling six times more attempts, and remove scorer exploits, the evolutionary advantage largely vanishes. Evolution beats independent sampling by 5% or less on 12 of 15 task-method pairs, retaining a 23 to 28% margin on only 3, all on one task. A replication with Claude Haiku 4.5 reproduces this split, though a third backbone shows its size depends on the model too. The performance margin justifying these systems is often an accounting artifact. Reporting tokens, not proposals and not model calls, fixes this and costs nothing, as the logs already hold them.
