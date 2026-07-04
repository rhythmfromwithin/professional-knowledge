---
interest: medium
link: https://arxiv.org/abs/2607.01605
next_step: skim
priority: low
slack_ts: '1783136981.515479'
source: cs.DB - Databases
status: unread
title: 'pykci: A Compact Urban Knowledge Graph for Semantic and Spatial Queries using
  LLMs'
---
# pykci: A Compact Urban Knowledge Graph for Semantic and Spatial Queries using LLMs
> 原文: [https://arxiv.org/abs/2607.01605](https://arxiv.org/abs/2607.01605)

arXiv:2607.01605v1 Announce Type: new
Abstract: CityGML, the OGC standard for modeling, storage, and exchange of semantic 3D city models, describes urban objects with detailed semantics, geometry, and topology. Yet this richness is difficult to query directly: CityGML's XML encoding is designed for exchange rather than analysis, and relational mappings expose it through schemas requiring expert knowledge. We present pykci (Python Knowledge Graph for Cities), an open-source system that transforms CityGML 2.0 datasets into a compact urban knowledge graph in Neo4j and makes it queryable in natural language. The graph schema covers all thematic feature modules of CityGML 2.0 across all levels of detail and is spatially indexed with an R-tree for efficient geometric retrieval. A complete end-to-end Python pipeline ingests CityGML datasets into the knowledge graph, exports them to OGC 3D Tiles for interactive visualization, and supports lossless round-trip export of all content back to CityGML. For querying, the graph is paired with a large language model through a model-agnostic text-to-Cypher mechanism: the graph schema is supplied as context, and the model translates natural-language questions into Cypher queries executed against the graph. We evaluate both a locally running open-weight model, which keeps sensitive city data on-premise, and a state-of-the-art commercial model for the most demanding spatial and semantic queries. Answers are grounded in exact city data rather than the model's parametric memory, reducing hallucination and providing auditable provenance for every response. We demonstrate the system on open-government CityGML LoD2 datasets from Hamburg, Germany, including complex semantic and spatial queries such as identifying roof surfaces suitable for greening. pykci enables urban planners, GIS practitioners, and citizens to interact with semantic 3D city models without expertise in query languages and database schemas.
