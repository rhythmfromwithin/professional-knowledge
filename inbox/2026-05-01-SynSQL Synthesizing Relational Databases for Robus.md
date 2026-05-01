---
title: "SynSQL: Synthesizing Relational Databases for Robust Evaluation of Text-to-SQL Systems"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.27261
priority: low
status: unread
interest: medium
next_step: skim
---
# SynSQL: Synthesizing Relational Databases for Robust Evaluation of Text-to-SQL Systems
> 原文: [https://arxiv.org/abs/2604.27261](https://arxiv.org/abs/2604.27261)

arXiv:2604.27261v1 Announce Type: new
Abstract: Evaluating text-to-SQL systems remains largely fragile: correctness is typically judged by executing predicted and gold SQL queries on a single static database, even though the same queries may behave differently under alternative database instances. This raises a broader language modeling question: Can large language models synthesize semantically meaningful, schema-consistent relational data directly from a natural language question? If so, such generation can serve as a controlled mechanism for stress-testing text-to-SQL systems beyond fixed benchmark databases. We introduce SynSQL, a framework that synthesizes test databases conditioned on question-schema alignment rather than gold SQL queries. SynSQL decomposes the task into three stages: (1) schema selection, (2) question-guided data synthesis, and (3) constraint-aware critique with iterative refinement, framing database construction as structured generation under semantic and relational constraints. Across ten text-to-SQL models on Spider, BIRD, and Spider 2.0, SynSQL-generated databases reveal performance drops of 3-14% compared to static evaluation, exposing errors masked by benchmark artifacts. We further analyze generation quality, constraint adherence, and failure modes, highlighting both the promise and limitations of LLMs in structured data synthesis. Our findings position synthetic database generation as a new lens for studying LLM reasoning, controllability, and robustness in structured environments.
