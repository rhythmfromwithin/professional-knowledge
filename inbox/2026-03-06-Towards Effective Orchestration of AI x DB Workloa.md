---
title: "Towards Effective Orchestration of AI x DB Workloads"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.03772
priority: low
status: unread
---
# Towards Effective Orchestration of AI x DB Workloads
> 原文: [https://arxiv.org/abs/2603.03772](https://arxiv.org/abs/2603.03772)

arXiv:2603.03772v1 Announce Type: new
Abstract: AI-driven analytics are increasingly crucial to data-centric decision-making. The practice of exporting data to machine learning runtimes incurs high overhead, limits robustness to data drift, and expands the attack surface, especially in multi-tenant, heterogeneous data systems. Integrating AI directly into database engines, while offering clear benefits, introduces challenges in managing joint query processing and model execution, optimizing end-to-end performance, coordinating execution under resource contention, and enforcing strong security and access-control guarantees.
This paper discusses the challenges of joint DB-AI, or AIxDB, data management and query processing within AI-powered data systems. It presents various challenges that need to be addressed carefully, such as query optimization, execution scheduling, and distributed execution over heterogeneous hardware. Database components such as transaction management and access control need to be re-examined to support AI lifecycle management, mitigate data drift, and protect sensitive data from unauthorized AI operations. We present a design and preliminary results to demonstrate what may be key to the performance for serving AIxDB queries.
