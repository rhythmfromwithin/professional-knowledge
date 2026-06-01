---
title: "The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2605.30666
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals
> 原文: [https://arxiv.org/abs/2605.30666](https://arxiv.org/abs/2605.30666)

arXiv:2605.30666v1 Announce Type: new
Abstract: Aligning large language models (LLMs) as math tutors typically demands costly reinforcement-learning (RL) training and external LLM judges. We ask whether a frozen model's internal reasoning signals can replace both. We propose the Tutoring Effectiveness Index (TEI), a training-free, judge-free four-signal index that combines a Schoenfeld-Verify keyword ratio, a math-step density, an ends-question rate, and a deep-reasoning gate from the Deep-Thinking Ratio (DTR) probe. Selecting from $N$ candidates with TEI (the TEI@$N$ rule) raises the improvement rate on pre-incorrect scenarios from $59.0\%$ to $81.9\%$ at $N{=}8$ on a frozen DeepSeek-R1-8B base, with no training and no external judge. We also measure the alignment tax of pedagogical GRPO. Thinking length drops from $1{,}764$ to $119$ words per turn ($-93\%$), Content-Knowledge and Pedagogical-Knowledge accuracy fall by $-71\%$ and $-80\%$ relative, and the student's $\Delta$ Solve Rate crosses from $+0.180$ to $-0.012$. To anchor the behavioural reading, we reproduce an 82-code educational codebook on $119{,}009$ tutor sentences with a one-shot structural classifier. Together, these results offer a cost-effective recipe for building math-tutoring LLMs without RL training or external judges.
