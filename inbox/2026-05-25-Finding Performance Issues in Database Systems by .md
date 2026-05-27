---
interest: medium
link: https://arxiv.org/abs/2605.22992
next_step: skim
priority: low
slack_ts: '1779856021.157939'
source: cs.SE - Software Engineering
status: unread
title: Finding Performance Issues in Database Systems by Exploiting Dormant Code Paths
---
# Finding Performance Issues in Database Systems by Exploiting Dormant Code Paths
> 原文: [https://arxiv.org/abs/2605.22992](https://arxiv.org/abs/2605.22992)

arXiv:2605.22992v1 Announce Type: new
Abstract: Performance is a critical characteristic of fundamental systems, such as Database Management Systems (DBMSs). Both academia and industry have invested decades in exploring efficient optimization algorithms. Despite these efforts, DBMSs are prone to performance issues, which incur suboptimal performance. Finding such issues is a longstanding challenge as no ground-truth performance is available. Existing work adopts black-box methods to examine performance consistency across executions, but cannot systematically test optimizations. In this work, we propose a novel, general white-box methodology, Branch Flip Analysis (BFA), to systematically and effectively uncover performance issues. BFA flips code branches to enforce or disable an optimization, and the performance is expected to be not significantly better. Otherwise, a performance issue exists. BFA provides a new perspective to finding performance issues and testing optimization logics in a fine-grained manner. We realized BFA in a prototype system QueryZen, and evaluated it on four widely-used and mature DBMSs: PostgreSQL, MySQL, CockroachDB, and MariaDB. QueryZen found 21 previously unknown and unique performance issues with the workload of the extensively used benchmarks TPC-H and TPC-DS. The core concept of BFA is simple and broadly applicable, and can be adapted to analyze the performance of other software systems.
