---
title: "Rewriting Ontology-Mediated Property Graph Queries into GQL"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.20092
priority: low
status: unread
interest: medium
next_step: skim
---
# Rewriting Ontology-Mediated Property Graph Queries into GQL
> 原文: [https://arxiv.org/abs/2608.20092](https://arxiv.org/abs/2608.20092)

arXiv:2608.20092v1 Announce Type: new
Abstract: Ontology-based data access is intended for graph data, but practical support remains limited to SQL-like languages lacking the navigational and path-matching features fundamental to graph querying. Theoretical algorithms for navigational queries have long been available. Still, they have never been implemented, largely because practical graph query languages fell short of their theoretical counterparts and lacked the expressive power needed to support rewriting common ontology languages.
The recent standardisation efforts around GQL and SQL/PGQ finally allow us to overcome this barrier and present a practical query rewriting technique for ontology-mediated navigational graph queries. Ontologies are written in a DL-Lite variant tuned to property graphs, and the queries in a GQL fragment with nested two-way regular path queries and which can be evaluated in Cypher. Preliminary experiments with our proof-of-concept prototype suggest that querying graph data with ontological knowledge may finally be within reach.
