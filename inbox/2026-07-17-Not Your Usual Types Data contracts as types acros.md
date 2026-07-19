---
interest: medium
link: https://arxiv.org/abs/2607.13339
next_step: skim
priority: low
slack_ts: '1784432002.463989'
source: cs.DB - Databases
status: unread
title: 'Not Your Usual Type(s): Data contracts as types across languages and engines'
---
# Not Your Usual Type(s): Data contracts as types across languages and engines
> 原文: [https://arxiv.org/abs/2607.13339](https://arxiv.org/abs/2607.13339)

arXiv:2607.13339v1 Announce Type: new
Abstract: Composable data systems promise to let developers combine languages, engines, and catalogs without sacrificing a coherent user experience. In practice, however, pipeline-node boundaries remain weakly specified: transformations exchange tables through schemas that are often checked late, enforced unevenly across languages, and disconnected from the semantics business users care about. Based on over a year of operating millions of jobs in Bauplan, we share the design principles behind our new SDK, which treats data contracts as types for a composable, multi-language lakehouse. Users, whether humans or agents, annotate input and output tables with schema objects that encode column types, constraints, documentation, and lineage; Bauplan then interprets these annotations at different points in the execution lifecycle. We show how this design addresses common production failures, and how an ''everything-as-code'' philosophy enables both deterministic and non-deterministic reasoning over data flows across languages and engines.
