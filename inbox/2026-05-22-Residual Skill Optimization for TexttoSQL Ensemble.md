---
interest: medium
link: https://arxiv.org/abs/2605.21792
next_step: skim
priority: low
slack_ts: '1779683946.999899'
source: cs.DB - Databases
status: unread
title: Residual Skill Optimization for Text-to-SQL Ensembles
---
# Residual Skill Optimization for Text-to-SQL Ensembles
> 原文: [https://arxiv.org/abs/2605.21792](https://arxiv.org/abs/2605.21792)

arXiv:2605.21792v1 Announce Type: cross
Abstract: Text-to-SQL ensembles improve over single-candidate generation by drawing multiple SQL candidates and selecting one, but their effectiveness is bounded by Pass@K, the probability that at least one of K candidates is correct. Existing methods source diversity heuristically through stochastic decoding or prompt variants, leaving candidate sets dominated by correlated failures. We present DivSkill-SQL, a residual skill optimization framework that builds complementary agentic Text-to-SQL ensembles without model fine-tuning: each new skill is optimized on examples the current skill ensemble fails on, provably targeting its marginal contribution to Pass@K. On Spider2-Lite, DivSkill-SQL improves selected accuracy by up to +11.1 points on Snowflake and +8.3 on BigQuery over the strongest ensemble baseline, with consistent gains across two base models (Opus-4.6 and GPT-5.4). Skills optimized on a single dialect transfer without retraining across dialects (Snowflake, BigQuery, SQLite) and to a different task formulation, such as BIRD-Critic (+2.6 pts). Error diagnostics show up to 3x fewer hallucinated schema references and function calls, indicating that gains come from genuinely reliable complementary skills rather than surface-form variation.
