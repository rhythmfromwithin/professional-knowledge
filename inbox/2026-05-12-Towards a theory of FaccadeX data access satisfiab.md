---
title: "Towards a theory of Fa\c{c}ade-X data access: satisfiability of SPARQL basic graph patterns"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2602.11756
priority: low
status: unread
interest: medium
next_step: skim
---
# Towards a theory of Fa\c{c}ade-X data access: satisfiability of SPARQL basic graph patterns
> 原文: [https://arxiv.org/abs/2602.11756](https://arxiv.org/abs/2602.11756)

arXiv:2602.11756v2 Announce Type: replace
Abstract: Data integration is the primary use case for knowledge graphs. However, integrated data are not typically graphs but come in different formats, for example, CSV, XML, or a relational database. Fa\c{c}ade-X is a recently proposed method for providing direct access to an open-ended set of data formats. The method includes a meta-model that specialises RDF to fit general data structures. This model allows to express SPARQL queries targeting data sources with those structures. Previous work formalised Fa\c{c}ade-X and demonstrated how it can theoretically represent any format expressible with a context-free grammar, as well as the relational model. A reference implementation, SPARQL Anything, demonstrates the feasibility of the approach in practice. It is noteworthy that Fa\c{c}ade-X utilises a fraction of RDF, and, consequently, not all SPARQL queries yield a solution (i.e. are satisfiable) when evaluated over a Fa\c{c}ade-X graph. In this article, we consolidate Fa\c{c}ade-X, and we study the satisfiability of basic graph patterns. The theory is accompanied by an algorithm for deciding the satisfiability of basic graph patterns on Fa\c{c}ade-X data sources. Furthermore, we provide extensive experiments with a proof-of-concept implementation, demonstrating practical feasibility, including with real-world queries. Our results pave the way for studying query execution strategies for Fa\c{c}ade-X data access with SPARQL and supporting developers to build more efficient data integration systems for knowledge graphs.
