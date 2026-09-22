---
interest: medium
link: https://arxiv.org/abs/2609.21564
next_step: skim
priority: low
slack_ts: '1790051348.001319'
source: cs.DB - Databases
status: unread
title: 'kgsteward: a tool for building, reproducing and maintaining distributed knowledge
  graphs'
---
# kgsteward: a tool for building, reproducing and maintaining distributed knowledge graphs
> 原文: [https://arxiv.org/abs/2609.21564](https://arxiv.org/abs/2609.21564)

arXiv:2609.21564v1 Announce Type: new
Abstract: Collaborative research projects in life sciences increasingly need to integrate private, embargoed consortium data with public reference databases in order to reach statistically meaningful interpretations. The Resource Description Framework (RDF) is well suited to this task: it facilitates the integration of heterogeneous data sources, and allows researchers to keep data and their documentation as metadata in the same place, provided the knowledge graph itself remains private during the time course of the project. Nevertheless, the development and long-term maintenance of a scientific knowledge graph remains a challenging, labour-intensive endeavour owing to the state of constant flux of most public resources. To tackle this challenge, we present kgsteward, a Python command-line tool that builds and maintains knowledge graphs inside RDF stores from a single, version-controlled configuration file. kgsteward supports multiple triplestores, keeps the local graph up-to-date with its external sources possibly already in RDF, or transformed into it on the fly, and uses SPARQL 1.1 UPDATE commands to amend further imported RDF on the fly. It can also validate the resulting graph with SPARQL queries that double as usage examples for both human users and AI agents. kgsteward has already been used in several collaborative projects at the SIB Swiss Institute of Bioinformatics, and we demonstrate its applicability in two real-world international research projects: one that builds a library of plant extracts with chemical analyses and associated bio-activities, and a second that reconciles public reference resources for human metabolic-network reconstruction.
