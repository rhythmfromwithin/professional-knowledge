---
interest: medium
link: https://arxiv.org/abs/2606.19751
next_step: skim
priority: low
slack_ts: '1781847258.394309'
source: cs.DB - Databases
status: unread
title: 'DeQL: A Decision Query Language for Prescriptive Analytics over Relational
  Data'
---
# DeQL: A Decision Query Language for Prescriptive Analytics over Relational Data
> 原文: [https://arxiv.org/abs/2606.19751](https://arxiv.org/abs/2606.19751)

arXiv:2606.19751v1 Announce Type: new
Abstract: DeQL (Decision Query Language) extends SQL to express decision queries: given options drawn from relational data, constraints from policy, and a measurable objective, a DeQL query computes the best course of action. Two constructs carry the extension: CREATE CANDIDATES, which defines the space of options from relational sources, and DECIDE, which declares decision variables, named constraints, and an objective over them. The design follows SQL's principles: the user states what to optimize while the engine chooses how to solve it, every query consumes and produces relations, and the structure of a problem stays visible to the engine. This document specifies the language (its design principles, syntax, formal grammar, and execution model) with examples spanning subset selection, allocation, assignment, scheduling, and decisions at multiple levels of aggregation, and extensions for optimization under uncertainty, inline model scoring, and time- and quality-bounded solving. It is the first version of the specification; the language is under active development, and this version fixes the core constructs on which later revisions will build.
