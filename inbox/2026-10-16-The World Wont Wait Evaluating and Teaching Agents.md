---
title: "The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.20665
priority: high
status: unread
interest: medium
next_step: skim
---
# The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock
> 原文: [https://arxiv.org/abs/2610.20665](https://arxiv.org/abs/2610.20665)

arXiv:2610.20665v1 Announce Type: new
Abstract: Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate agents while games continue running during inference. Paired evaluations show that GPT-6.1-sol outperforms the faster Jev when games are paused, but falls behind when they keep running. We propose Two-Timescale Offline Recursive Self-Improvement (TORSI): a slow teacher studies failures and tests corrections in paused games between attempts, then writes reusable instructions for a fast student. The student acts without teacher calls during gameplay, and validation scores determine which updates are adopted. Two rounds raise Jev's average test score from 13.51 to 24.19 on a 0--100 progress scale, improving all six game types. The instructions also improve average scores for three other models without retuning. These findings point toward real-time intelligence: enabling powerful LLM agents to remain effective in a continuously changing world by organizing deliberation, learning, and action across timescales.
