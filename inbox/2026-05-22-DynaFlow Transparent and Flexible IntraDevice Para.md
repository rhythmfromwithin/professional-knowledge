---
interest: medium
link: https://arxiv.org/abs/2605.21603
next_step: skim
priority: medium
slack_ts: '1779596225.271879'
source: cs.DC - Distributed Computing
status: unread
title: 'DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable
  Operator Scheduling'
---
# DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling
> 原文: [https://arxiv.org/abs/2605.21603](https://arxiv.org/abs/2605.21603)

arXiv:2605.21603v1 Announce Type: new
Abstract: Intra-device parallelism addresses resource under-utilization in ML inference and training by overlapping the execution of operators with different resource usage. However, its wide adoption is hindered by a fundamental conflict with the static, sequential programming model of existing frameworks. Integrating these strategies requires invasive, model-specific code overhauls, representing an intractable engineering cost. This is further amplified by the high sensitivity of strategies to execution contexts (e.g., workload, model architecture, hardware), forcing developers to implement and maintain multiple specialized solutions. To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule. DynaFlow introduces a flexible frontend with annotations for graph partitioning and a programmable interface for defining custom intra-device parallelism strategies. Its efficient backend manages complex control/data-flow asynchronously, uses custom memory management to eliminate copy overheads, and preserves compatibility with optimizations like CUDA Graphs and TorchInductor. We demonstrate that DynaFlow can integrate representative parallelism strategies into 6 state-of-the-art ML systems with minimal code changes, achieving up to a 1.29x throughput improvement. DynaFlow is publicly available at https://github.com/uw-syfi/DynaFlow.
