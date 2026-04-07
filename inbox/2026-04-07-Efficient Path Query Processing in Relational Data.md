---
interest: medium
link: https://arxiv.org/abs/2604.02553
next_step: skim
priority: low
slack_ts: '1775531924.379139'
source: cs.DB - Databases
status: unread
title: Efficient Path Query Processing in Relational Database Systems
---
# Efficient Path Query Processing in Relational Database Systems
> 原文: [https://arxiv.org/abs/2604.02553](https://arxiv.org/abs/2604.02553)

arXiv:2604.02553v1 Announce Type: new
Abstract: Path queries are crucial for property graphs, and there is growing interest in queries that combine regular expressions over labels with constraints on property values of vertices and edges. Efficient evaluation of such general path queries requires that intermediate results be eliminated early when there is no possible completion to a full result path. Neither state-of-the-art (SOA) graph DBMS nor relational DBMS currently can do this effectively for a large class of queries. We show that this problem can be addressed by giving a relational optimizer ``a little help'' by specifying early filtering opportunities explicitly in the query. To this end, we propose ReCAP, an abstraction that greatly simplifies the implementation of early filtering techniques for any type of property constraint for which such early filtering can be derived. No matter how complex the constraint, one only needs to implement (1) an NFA-style state transition function and (2) a handful of functions that mirror those needed for user-defined aggregates. We show that when using ReCAP, a standard relational DBMS like DuckDB can effectively push property constraints deep into the query plan, beating the SOA graph and relational DBMS by a factor up to 400,000 over a variety of queries and input graphs.
