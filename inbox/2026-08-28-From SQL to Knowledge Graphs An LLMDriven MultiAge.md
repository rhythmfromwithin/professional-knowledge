---
interest: medium
link: https://arxiv.org/abs/2608.26117
next_step: skim
priority: low
slack_ts: '1787986069.551469'
source: cs.DB - Databases
status: unread
title: 'From SQL to Knowledge Graphs: An LLM-Driven Multi-Agent Approach with Data
  Schema Improvement'
---
# From SQL to Knowledge Graphs: An LLM-Driven Multi-Agent Approach with Data Schema Improvement
> 原文: [https://arxiv.org/abs/2608.26117](https://arxiv.org/abs/2608.26117)

arXiv:2608.26117v1 Announce Type: new
Abstract: RDBMS (Relational Database Management System) databases face several limitations, including slow execution with multi-hop queries and a lack of explainability by graphical interpretations. In contrast, Graph database offers a more intuitive and efficient data schema that performs faster execution on large datasets. Most existing RDBMS conversion pipelines focus on running traditional loading commands and relying on Cypher queries. However, the efficiency of using an LLM to generate an effective graph data schema, significantly reducing the ambiguity of the graph database, remains underexplored in the current research literature. This paper presents a novel algorithm that bridges RDBMS and graph database by using a novel LLM-powered ETL agent to standardize table and column names before saving them to the Data Mart. A Multi-Agent System generates a looping discussion between ETL, Analyzer, and Graph agents to optimize the final design through an iterative process of suggesting and scoring the graph database schema. We ensure that the final graph database meets three criteria before being accepted for data conversion: Accuracy, Groundedness, and Faithfulness. This system demonstrates an effective pipeline to automatically convert a tabular database into a graph database through a comprehensive end-to-end process. Our study highlights notable efficiency in using the converted graph database, which is measured on 1,081 samples of the BFSI dataset across three levels of complexity (easy, medium, and hard). Specifically, CypherAgent achieves an 85.6% accuracy for Q&A tasks using a Graph database, which is 12.12% higher than the accuracy achieved by an SQLAgent on the RDBMS database type PostgreSQL, for all queries. Additionally, the Graph database demonstrates faster performance, reducing latency by approximately 3 times.
