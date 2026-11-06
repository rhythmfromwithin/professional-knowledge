---
title: "Selective Retrieval Routing for Multi-Violation Knowledge Graph Repair"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.07342
priority: low
status: unread
interest: medium
next_step: skim
---
# Selective Retrieval Routing for Multi-Violation Knowledge Graph Repair
> 原文: [https://arxiv.org/abs/2611.07342](https://arxiv.org/abs/2611.07342)

arXiv:2611.07342v1 Announce Type: new
Abstract: Knowledge graphs often contain missing or inconsistent facts that undermine the applications built on them. Schema validation detects such violations but does not identify which of several valid repairs recovers the intended graph. External corpora can supply the evidence needed to identify the intended repair, but retrieving from them is costly and not always successful. We propose a framework for selective retrieval in iterative graph repair. An LLM repair agent explores and edits the graph, while a router controls its access to a researcher agent that retrieves external evidence. We extend a violation-injection framework to generate cases with multiple compatible violations and known reference repairs. The agent's repair outcomes on these cases provide supervision for training the deployment-specific router. On two building-automation datasets, researcher access improves repairs for some violations and degrades them for others, with effects differing across deployments. The router uses fewer repair-time tokens than always enabling access in all six evaluation suites. It achieves higher repair $F\_1$ than always disabling access in five of six suites.
