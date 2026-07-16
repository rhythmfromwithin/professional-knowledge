---
interest: medium
link: https://arxiv.org/abs/2607.10081
next_step: skim
priority: medium
slack_ts: '1784172045.122819'
source: cs.DC - Distributed Computing
status: unread
title: Descriptive Execution of HPC Applications and Workflows
---
# Descriptive Execution of HPC Applications and Workflows
> 原文: [https://arxiv.org/abs/2607.10081](https://arxiv.org/abs/2607.10081)

arXiv:2607.10081v1 Announce Type: new
Abstract: The means to execute and orchestrate software components has changed from human-written code to descriptive prose. In high performance computing, this transition is represented in application orchestration, workload management, and system monitoring and debugging, to name a few. The underlying means to enable descriptive definition of tasks is the use of the Large Language Model with associated tool functions and resources. A combination of a model with access to such resources, modeled in software, encompasses an autonomous framework. As fully automated and agentic frameworks are developed for science, it is important to assess reliability and strategies scoped to specific tasks. In this work, we assess the extent to which an agentic framework can optimize and run an HPC scaling study with a low latency network in Amazon Web Services, accurately transform HPC job specifications between workload managers, and design and run an entire biosciences workflow. We find that the framework completes all three tasks while surfacing task-specific failure modes. In the scaling study, agents deploy and optimize applications but monitor running jobs inefficiently, preferring conservative fixed waits over event subscriptions. In job translation, they convert specifications between Slurm and Flux with high accuracy, with processor-affinity flags the most common error. In the bioscience workflow, the agent reproduces an expert-written variant-calling pipeline almost exactly -- agreeing with the reference call set in 18 of 19 completed runs -- and reaches this result through many distinct yet functionally equivalent workflow implementations. This information is invaluable moving forward to developing multi-cluster setups with scheduling and transformation handled by agents.
