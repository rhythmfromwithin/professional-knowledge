---
interest: medium
link: https://arxiv.org/abs/2607.21746
next_step: skim
priority: medium
slack_ts: '1785208721.402839'
source: cs.DC - Distributed Computing
status: unread
title: 'PRISM: Evaluating POSIX Storage Systems for AI Research Workflows'
---
# PRISM: Evaluating POSIX Storage Systems for AI Research Workflows
> 原文: [https://arxiv.org/abs/2607.21746](https://arxiv.org/abs/2607.21746)

arXiv:2607.21746v1 Announce Type: new
Abstract: The rapid advancement of AI research is driven by massive investments in GPU clusters, yet the critical role of storage systems in enabling efficient research workflows is often overlooked. Unlike traditional HPC workloads, AI research prioritizes researcher productivity and ease of iteration. Practitioners rely on POSIX compliant file systems for seamless prototyping, debugging, and experimentation before scaling to specialized storage backends. The primary selection criterion is therefore not peak throughput alone, but rather performance within a POSIX compatible, researcher friendly interface. However, existing benchmarks evaluate storage systems exclusively on peak performance and fail to capture the bursty, heterogeneous IO patterns characteristic of real world AI research - where workflows are dynamic, continuously evolving spanning all stages of research. We introduce PRISM, an evaluation framework that reproduces representative AI research workloads - spanning data ingestion, checkpoint IO, and developer workflows to assess and qualify POSIX storage systems along both usability and performance dimensions on GPU clusters. Using PRISM we were able to compare Lustre and NFS based POSIX storage systems across multiple research workload dimensions and select the appropriate storage solution for different environments. As a specific case study in our environment we observed that a flash backed NFS solution outperformed the flash backed Lustre solution by up to 3x for the distributed checkpoint load usecase which helped us make an informed cluster design
