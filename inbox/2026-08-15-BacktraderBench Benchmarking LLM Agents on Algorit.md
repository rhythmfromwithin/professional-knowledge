---
interest: medium
link: https://arxiv.org/abs/2608.11232
next_step: skim
priority: high
slack_ts: '1786931055.978959'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated
  MCQs'
---
# Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated MCQs
> 原文: [https://arxiv.org/abs/2608.11232](https://arxiv.org/abs/2608.11232)

arXiv:2608.11232v1 Announce Type: new
Abstract: Evaluating LLM coding agents in algorithmic trading is difficult because static benchmarks risk data contamination and numerical backtest outputs require ground truth from actual code execution. We present Backtrader-Bench, a framework with two complementary pipelines. A deterministic multiple-choice question (MCQ) pipeline generates questions from backtest configurations across five trading strategies, 33 templates, and three difficulty tiers, with an independent checker that re-derives every answer. A generator-solver filtering pipeline autonomously mines harder questions: a generator writes questions verified by executable code, converts them to MCQs, and discards any that a no-tool solver can answer without code execution. We evaluate 11 models without tools (10 runs each) and four with-tools configurations on a 30-question curated set. Tool-augmented agents reach 90.0% accuracy in a single pass (GPT-5.5 and Opus 4.7), outperforming the best no-tools baselines (73.0%, averaged over 10 runs) by 17 percentage points. On 38 separately mined questions, no-tools accuracy drops further, with half the models falling to roughly random-chance level (25%). Beyond evaluation, the scalable MCQ infrastructure is designed to produce a training corpus for reinforcement learning, with the ultimate goal of building a specialized agent for quantitative trading workflows.
