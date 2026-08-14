---
title: "Reinforcement Learning based DBMS Buffer Pool Auto-Tuning for Optimal Memory Utilization"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.11239
priority: low
status: unread
interest: medium
next_step: skim
---
# Reinforcement Learning based DBMS Buffer Pool Auto-Tuning for Optimal Memory Utilization
> 原文: [https://arxiv.org/abs/2608.11239](https://arxiv.org/abs/2608.11239)

arXiv:2608.11239v1 Announce Type: new
Abstract: Administering Database Management Systems (DBMS) instances requires Database Administrators (DBA) to balance performance in terms of Service Level Agreement (SLA) against resource usage, often prompting RAM over-allocation that wastes memory. We introduce MicroTune, an online RL-based buffer adjustment system that minimizes unnecessary memory allocation while ensuring SLA compliance. To identify the most effective RL core, we evaluate multiple algorithms under diverse benchmark workloads, training MicroTune on extensive traces of both external metrics (latency, throughput) and internal DBMS metrics (status variables and performance statistics). Experimental results demonstrate that MicroTune dynamically adapts buffer sizes to workload fluctuations, outperforming baselines by achieving significant memory savings with fewer SLA violations. These findings underscore the promise of reinforcement learning for adaptive resource management in DBMS environments.
