---
title: "Does SRL Pave the Road to Explainable Reasoning? Lessons Learned from an Implementer's Perspective"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.03441
priority: low
status: unread
interest: medium
next_step: skim
---
# Does SRL Pave the Road to Explainable Reasoning? Lessons Learned from an Implementer's Perspective
> 原文: [https://arxiv.org/abs/2609.03441](https://arxiv.org/abs/2609.03441)

arXiv:2609.03441v1 Announce Type: new
Abstract: The Shape Rules Language (SRL) Working Draft defines how to derive new RDF triples from an RDF graph using inference rules. Each rule matches graph patterns and instantiates triple templates whose output feeds into validation pipelines, SPARQL queries, or further inference. RDF reasoning has traditionally relied on fixed entailment regimes (RDFS, OWL), rule-based ad-hoc languages such as N3, or other implementation-specific solutions without a shared standard. SRL introduces user-defined production rules with a defined grammar, dependency analysis, execution ordering, and termination guarantees. However, no authoritative implementation exists, leaving practitioners with little guidance on how to build a conformant engine or on what problems the language can solve. We implemented two SRL engines and evaluated both on classical RDF reasoning tasks for soundness, completeness, and speed. The first reuses an existing SPARQL query engine and its query parser; the second is a dedicated engine. The SPARQL-based engine reused an existing modular parser for query construction and SPARQL CONSTRUCT for triple production, reducing engine-specific work. The dedicated engine was two to six times faster, the gap widening as rule sets grow. Both engines were validated against the SRL conformance test suite, supplemented by additional use-case-driven tests. A usable SRL engine can be built inexpensively on top of a SPARQL engine, with a moderate speed trade-off that a dedicated implementation recovers. Despite the specification's immaturity, the language already supports practically useful reasoning tasks.
