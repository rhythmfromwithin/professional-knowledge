---
interest: medium
link: https://arxiv.org/abs/2603.02376
next_step: skim
priority: medium
slack_ts: '1773369794.238639'
source: cs.DC - Distributed Computing
status: unread
title: 'CUCo: An Agentic Framework for Compute and Communication Co-design'
---
# CUCo: An Agentic Framework for Compute and Communication Co-design
> 原文: [https://arxiv.org/abs/2603.02376](https://arxiv.org/abs/2603.02376)

arXiv:2603.02376v1 Announce Type: new
Abstract: Custom CUDA kernel development is essential for maximizing GPU utilization in large-scale distributed LLM training and inference, yet manually writing kernels that jointly leverage both computation and communication remains a labor-intensive and error-prone process. Prior work on kernel optimization has focused almost exclusively on computation, leaving communication kernels largely untouched even though they constitute a significant share of total execution time. We introduce CUCo, a training-free agent-driven workflow that automatically generates high-performance CUDA kernels that jointly orchestrate computation and communication. By co-optimizing these traditionally disjoint components, CUCo unlocks new optimization opportunities unavailable to existing approaches, outperforming state-of-the-art baselines and reducing end-to-end latency by up to $1.57\times$.
