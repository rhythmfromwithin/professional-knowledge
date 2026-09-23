---
title: "Generating Query Context for Relational Databases"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.26200
priority: low
status: unread
interest: medium
next_step: skim
---
# Generating Query Context for Relational Databases
> 原文: [https://arxiv.org/abs/2609.26200](https://arxiv.org/abs/2609.26200)

arXiv:2609.26200v1 Announce Type: new
Abstract: Relational databases are the systems of record for business applications, and there is growing demand to query them through natural language interfaces. A key challenge is that AI models need appropriate query context, i.e., sample questions paired with their corresponding data-model fragments, to generate accurate SQL. Today, creating this context is a manual, time-consuming process that requires expertise in both SQL and the database schema, leading to a cold start problem for new databases and an ongoing maintenance burden as schemas and query patterns evolve. We present an automated approach for generating query context for relational databases. Our method defines query flows that capture common patterns of data retrieval and analysis questions, systematically generates data models by traversing these flows, and instantiates them with specific values sampled from the database using weighted strategies that maximize diversity and coverage. The resulting question--data-model pairs can be used to guide natural language interfaces in accurately querying relational databases. We report on our experience deploying this approach across more than 50 real-world databases connected to Tursio.
