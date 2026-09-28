---
interest: medium
link: https://arxiv.org/abs/2609.31246
next_step: skim
priority: low
slack_ts: '1790571566.816579'
source: cs.DB - Databases
status: unread
title: Provenance of HAVING Queries in Semirings with Monus
---
# Provenance of HAVING Queries in Semirings with Monus
> 原文: [https://arxiv.org/abs/2609.31246](https://arxiv.org/abs/2609.31246)

arXiv:2609.31246v1 Announce Type: new
Abstract: The semiring framework and its extensions form the basis of a rich collection of theoretical results and implementations for provenance tracking of database queries. Many real-world queries use aggregation and conditions on the aggregate values. Support for such queries has been proposed by introducing semimodule elements as aggregate values and formal comparisons between aggregate values as tuple annotations, which takes the approach outside the standard semiring framework. In this work, we show how to introduce a semantics for the provenance of such queries in arbitrary commutative semirings with monus (or m-semirings), without the need for additional operators. This semantics is shown to agree with the standard provenance of the aggregation-free self-join rewriting of HAVING COUNT(\*) queries in semirings that are absorptive and where times distributes over monus. We derive algorithms for this semantics and implement them within the ProvSQL system, with viable performance on a real-world dataset for probabilistic query evaluation.
