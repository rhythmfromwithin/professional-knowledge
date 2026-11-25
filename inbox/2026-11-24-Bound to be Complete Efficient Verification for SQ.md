---
interest: medium
link: https://arxiv.org/abs/2611.28516
next_step: skim
priority: low
slack_ts: '1795593784.683799'
source: cs.DB - Databases
status: unread
title: 'Bound to be Complete: Efficient Verification for SQL Equivalence via U-Expressions'
---
# Bound to be Complete: Efficient Verification for SQL Equivalence via U-Expressions
> 原文: [https://arxiv.org/abs/2611.28516](https://arxiv.org/abs/2611.28516)

arXiv:2611.28516v1 Announce Type: new
Abstract: Automated verification of SQL query equivalence is a fundamental problem in database area. Recent works developed verifiers with guaranteed completeness, which can generate counterexamples to disprove non-equivalent queries and are useful in various scenarios. However, they have to solve complex formulas and can fail to produce counterexamples within a reasonable time budget.
This paper presents a new complete verifier called SQLution, which not only greatly reduces the verification time, but also supports more SQL features. The key insight is to represent SQL semantics using U-expression, a functional algebra that can model SQL with significantly simpler formulas than prior works, thereby leading to more efficient SMT solving. To turn this insight into a practical verifier, SQLution further tackles two technical challenges associated with modeling SQL using U-expression, namely, the lack of tuple ordering and the presence of unbounded summations. In particular, to support tuple ordering, SQLution proposes order semantics encoding which combines U-expressions with first-order logic. To handle unbounded summation, SQLution introduces unbounded summation expansion to transform them into bounded summations, which can be directly encoded into FOL formulas. Evaluation shows that compared with state-of-the-art verifiers, SQLution can support all 271 non-equivalent query pairs derived from the Spider dataset and reduces verification time by up to 98.6%.
