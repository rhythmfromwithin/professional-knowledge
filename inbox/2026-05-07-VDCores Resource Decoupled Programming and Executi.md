---
title: "VDCores: Resource Decoupled Programming and Execution for Asynchronous GPU"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.03190
priority: medium
status: unread
interest: medium
next_step: skim
---
# VDCores: Resource Decoupled Programming and Execution for Asynchronous GPU
> 原文: [https://arxiv.org/abs/2605.03190](https://arxiv.org/abs/2605.03190)

arXiv:2605.03190v1 Announce Type: new
Abstract: Modern GPUs increasingly rely on specialized and asynchronous hardware units to deliver high performance. Yet these units are often underutilized because today's GPU software stacks still organize programming and execution around a monolithic kernel model that mismatches asynchronous hardware. To address this issue, Virtual Decoupled Engines (VDCores) presents a new decoupled programming and execution model for asynchronous GPUs. VDCores abstracts asynchronous hardware execution units as resource isolated virtual cores and represents workloads as dependency-connected micro-operations (micro-ops). this abstraction removes static orchestration from the programmer, enables automatic overlap of memory and compute based on dependency and resource readiness, and thereby improves utilization of asynchronous hardware resources.
Realizing such a decoupled abstraction efficiently on today's GPUs is itself challenging, VDCores addresses this through a GPU-specialized programming model and GPU runtime design that preserves the flexibility while minimizing implementation overhead. Across four LLM inference workloads on GH200, H100, and RTX 6000 Pro GPUs, VDCores significantly improves decoding throughput by 24% on average and by up to 77% under dynamic inputs, while reducing kernel programming and specialization effort by 90%. We have open sourced VDCores at https://github.com/vdcores/vdcores.
