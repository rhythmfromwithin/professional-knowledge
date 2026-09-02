---
interest: medium
link: https://arxiv.org/abs/2609.00381
next_step: skim
priority: low
slack_ts: '1788321942.340619'
source: cs.DB - Databases
status: unread
title: 'Bounded, Indeterminate, or a Bug: A Condition-Aware Oracle for Differential
  Testing of SQL Aggregates'
---
# Bounded, Indeterminate, or a Bug: A Condition-Aware Oracle for Differential Testing of SQL Aggregates
> 原文: [https://arxiv.org/abs/2609.00381](https://arxiv.org/abs/2609.00381)

arXiv:2609.00381v1 Announce Type: new
Abstract: Differential database testing compares results across engines and calls a discrepancy a bug. For floating-point aggregates this is unsound: engines legitimately disagree because floating-point arithmetic is not associative. Practice patches this with an epsilon; the leading oracles avoid floating point entirely. We give the oracle this practice lacks, and show its decisive quantity is not the query but the engine's algorithm. Ground truth is the exact rational value of the stored doubles -- arithmetic, not another engine -- and each discrepancy is classified exact, bounded, or indeterminate. The relative error of an aggregate f under an algorithm A obeys rel\_err <= C\_A(n,u) \* kappa\_f^p, so the testability boundary, beyond which no oracle can separate a bug from rounding, is kappa\*\_{f,A} = (1/C\_A)^{1/p}. SUM and AVG are the linear case p=1; variance is p=2 for the one-pass algorithm and p=1 for Welford. Across eight engines in four classes the measured exponent recovers each algorithm, and ClickHouse is the lone one-pass engine (p=2.05); engine-wide, it returns zero standard deviation, NaN correlation and wrong-sign regression, while every other engine stays exact and the vendor ships the Welford fix. Its variance is untestable at a condition number 10^6 below SUM's, which ordinary storage conventions (epoch-nanosecond timestamps, tight sensors) cross -- there ClickHouse errs by 2100%. A randomised hunt of 360 tests finds zero anomalies, evidence the oracle is sound. Code and data are public.
