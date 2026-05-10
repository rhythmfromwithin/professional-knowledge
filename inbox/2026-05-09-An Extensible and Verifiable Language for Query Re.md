---
interest: medium
link: https://arxiv.org/abs/2605.05536
next_step: skim
priority: low
slack_ts: '1778385544.206299'
source: cs.DB - Databases
status: unread
title: An Extensible and Verifiable Language for Query Rewrite Rules
---
# An Extensible and Verifiable Language for Query Rewrite Rules
> 原文: [https://arxiv.org/abs/2605.05536](https://arxiv.org/abs/2605.05536)

arXiv:2605.05536v1 Announce Type: new
Abstract: Logical query plan rewriting transforms a relational database query into an equivalent but more efficient form and is crucial to the performance of database-backed applications. In existing systems, rewrite rules are typically implemented manually, tightly coupled to specific execution engines, and often lack formal correctness guarantees. Consequently, developing a new engine requires reimplementing both legacy and new rules, incurring significant engineering cost, limiting portability, and every new implementation is an opportunity for introducing new bugs.
We introduce Rulescript, an engine-agnostic domain-specific language (DSL) for developing query rewrite rules. Rulescript separates rule definition from execution infrastructure via a relational algebra-inspired core language and an explicit decomposition of rules into matching and transformation phases. Developers express rewrites by pattern-matching query plans using Rulescript's core operators and constructing semantically equivalent transformed plans, with all rewrites automatically verified formally to ensure correctness. Rulescript is extensible: users can define custom operators in terms of the core language to capture engine-specific semantics. To integrate with an existing system, developers need only implement a lightweight adapter that maps Rulescript's core and custom operators to the operators implemented in the target engine.
We evaluate Rulescript by reimplementing 33 rewrite rules from Apache Calcite and extending the language with several custom operators. To demonstrate portability, we automatically deploy these rules to CockroachDB and Apache Data Fusion, two engines with substantially different backends. Our results show that Rulescript enables "write once, deploy everywhere" paradigm for query plan rewriting, with minimal effort required to deploy previously written rules on a new data engine.
