---
interest: medium
link: https://arxiv.org/abs/2604.15465
next_step: skim
priority: low
slack_ts: '1776742306.158759'
source: cs.SE - Software Engineering
status: unread
title: 'GraphQLify: Automated and Type Safety-Preserving GraphQL API Adoption'
---
# GraphQLify: Automated and Type Safety-Preserving GraphQL API Adoption
> 原文: [https://arxiv.org/abs/2604.15465](https://arxiv.org/abs/2604.15465)

arXiv:2604.15465v1 Announce Type: new
Abstract: GraphQL provides a schema-based, strongly typed query language that enables highly efficient client-server communication. This paper introduces GraphQLify, an automated framework designed to migrate existing REST APIs to GraphQL. Unlike prior approaches that rely on relational databases, resource description frameworks (RDF), or machine-parsable specifications, GraphQLify leverages static source code analysis for precise type inference. This novel technique generates GraphQL schemas that guarantee end-to-end type safety, preserving a core advantage of adopting GraphQL. Furthermore, existing migration tools typically generate separate adapter servers, which introduce performance overhead via dynamic request binding and network latency. GraphQLify eliminates this by generating an embedded server that directly invokes the underlying API code, significantly improving performance. We evaluated GraphQLify on 834 APIs across nine popular open-source projects, where it successfully converted 100% of the APIs with zero type mismatches. In contrast, the current state-of-the-art tool, OASGraph, exhibited a 3.5% failure rate and a 42% type mismatch rate on the same dataset. Finally, our performance evaluation demonstrates that for workflows requiring five sequential API calls, clients using GraphQLify reduce data fetching time by a factor of 2 to 4 compared to their REST counterparts.
