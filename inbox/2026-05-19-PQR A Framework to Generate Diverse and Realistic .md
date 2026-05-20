---
interest: medium
link: https://arxiv.org/abs/2605.16551
next_step: skim
priority: high
slack_ts: '1779250492.162169'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'PQR: A Framework to Generate Diverse and Realistic User Queries that Elicit
  QA Agent Failures'
---
# PQR: A Framework to Generate Diverse and Realistic User Queries that Elicit QA Agent Failures
> 原文: [https://arxiv.org/abs/2605.16551](https://arxiv.org/abs/2605.16551)

arXiv:2605.16551v1 Announce Type: new
Abstract: Evaluating LLM-based agents remains challenging because identifying meaningful failure cases often requires substantial human effort to design realistic test scenarios. Prior works primarily focus on automatically discovering agent failures induced by adversarial users, while overlooking queries with real user intents that also trigger agent failures. We introduce PQR, a framework that not only surfaces agent failures with respect to specific objectives (e.g., helpfulness, safety, etc.) but also resembles real users' intents. PQR operates through an iterative interaction between two complementary modules. The query refinement module performs rewrites to explore diverse query variations, while the prompt refinement module uses prior feedback to derive new objective-violating strategies and realism policies for refining prompts, which in turn generate failure-triggering yet realistic queries. We evaluate PQR on detecting an e-commerce QA agent's unhelpful responses. Our method uncovers 23% - 78% more unhelpful responses, and our generated queries are more diverse and realistic compared to previous methods.
