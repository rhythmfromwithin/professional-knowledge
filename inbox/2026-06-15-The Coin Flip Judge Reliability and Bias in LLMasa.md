---
interest: medium
link: https://arxiv.org/abs/2606.13685
next_step: skim
priority: high
slack_ts: '1781586962.096349'
source: cs.CL - Computation and Language (NLP)
status: unread
title: The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation
---
# The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation
> 原文: [https://arxiv.org/abs/2606.13685](https://arxiv.org/abs/2606.13685)

arXiv:2606.13685v1 Announce Type: new
Abstract: LLM-as-a-Judge is now widely used to rank model outputs, train reward models, and populate public leaderboards, but its run-to-run reliability remains under-characterized. We study repeated identical evaluations on 29 tasks spanning 10 categories using two OpenAI judge models (GPT-4o-mini and GPT-4.1-mini), with 50 pairwise trials and 50 pointwise trials per question, supplemented by temperature and prompt-sensitivity ablations. Across judges, pairwise preferences flip on average 13.6% of the time, with 28% of questions exceeding a 20% flip rate and one question reaching 56%. GPT-4o-mini also exhibits a significant first-position bias (72% A-majority, p = 0.024). At the same time, mean pointwise score gaps are small (0.19--0.36 on a 10-point scale) and not statistically significant in aggregate, producing a pairwise--pointwise gap: judges frequently choose a winner even when their own scalar scores provide little evidence of a meaningful quality difference. Beyond within-judge instability, cross-judge agreement is only 76% ($\kappa = 0.51$), semantically equivalent prompt templates change majority outcomes in 25% of tested cases, and deterministic decoding reduces but does not eliminate inconsistency. A reliability curve analysis shows that, in our dataset, 11 repeated trials are needed for a majority vote to recover the 50-trial reference verdict with 95% probability on average, rising to 15 for high-variance questions. These findings suggest that single-trial LLM judging is often too noisy for high-stakes evaluation, and that multi-trial aggregation, position randomization, and explicit uncertainty reporting should be standard practice. Because both judges are from a single provider, cross-provider replication remains an important next step.
