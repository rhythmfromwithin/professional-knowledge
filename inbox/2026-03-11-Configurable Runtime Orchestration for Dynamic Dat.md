---
title: "Configurable Runtime Orchestration for Dynamic Data Retrieval in Distributed Systems"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.06980
priority: medium
status: unread
interest: medium
next_step: skim
---
# Configurable Runtime Orchestration for Dynamic Data Retrieval in Distributed Systems
> 原文: [https://arxiv.org/abs/2603.06980](https://arxiv.org/abs/2603.06980)

arXiv:2603.06980v1 Announce Type: new
Abstract: Modern enterprise platforms increasingly depend on distributed microservices, analytical data platforms, and external APIs to construct composite responses for applications. Orchestrating data retrieval across these heterogeneous systems is challenging because many workflow platforms rely on predefined workflows or state-machine definitions. Systems such as Apache Airflow, AWS Step Functions, and Temporal provide powerful orchestration capabilities but typically assume workflows are defined prior to execution. This paper presents a configuration-driven runtime orchestration framework for dynamic data retrieval in distributed systems. The framework generates execution graphs dynamically from configuration at request time, enabling low-latency orchestration without redeploying workflow code when integrations evolve. The execution planner performs dependency-aware scheduling and parallel execution of independent tasks, allowing efficient aggregation across distributed services. The paper describes the architecture, execution model, and operational tradeoffs of this framework, and presents a representative enterprise case study for Customer 360 retrieval. The approach demonstrates how runtime configuration can enable flexible and scalable orchestration in rapidly evolving integration environments.
