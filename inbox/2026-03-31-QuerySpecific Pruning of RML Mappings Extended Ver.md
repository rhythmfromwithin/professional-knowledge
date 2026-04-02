---
interest: medium
link: https://arxiv.org/abs/2603.26269
next_step: skim
priority: low
slack_ts: '1775098513.336129'
source: cs.DB - Databases
status: unread
title: Query-Specific Pruning of RML Mappings (Extended Version)
---
# Query-Specific Pruning of RML Mappings (Extended Version)
> 原文: [https://arxiv.org/abs/2603.26269](https://arxiv.org/abs/2603.26269)

arXiv:2603.26269v1 Announce Type: new
Abstract: Current approaches for knowledge graph construction with RML focus on full RDF graph materialization without considering user queries. As a result, mapping engines are inefficient in dynamic query environments, materializing large graphs even when only a small subset is needed to answer user queries. In this paper, we formally define satisfiability for SPARQL queries with respect to RDF data obtained via RML mappings and use this property to prune RML mappings for partial RDF graph materialization. Evaluation on the GTFS-Madrid benchmark shows that pruning significantly reduces materialization time, and RDF graph size while also noticeably improving querying time. Thus, enabling existing materialization engines to efficiently support generating RDF graphs in dynamic federated querying environment where user queries change frequently.
