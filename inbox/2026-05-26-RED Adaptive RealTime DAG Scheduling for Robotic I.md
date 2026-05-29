---
interest: medium
link: https://arxiv.org/abs/2605.24044
next_step: skim
priority: medium
slack_ts: '1780028369.965989'
source: cs.RO - Robotics
status: unread
title: 'RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental
  Dynamics'
---
# RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental Dynamics
> 原文: [https://arxiv.org/abs/2605.24044](https://arxiv.org/abs/2605.24044)

arXiv:2605.24044v1 Announce Type: new
Abstract: Robots deployed in dynamic environments must contend with environment-driven changes that reshape computation at runtime: new tasks may appear, precedence relations can shift, and overall workload structure evolves, all of which degrade performance, especially when multi-task inference is required under tight resource and real-time budgets. We present RED, a real-time scheduling framework for multi-task deep neural network workloads on resource-constrained robotic platforms that adapts to Robotic Environmental Dynamics (RED) while preserving end-to-end timing guarantees under modeling assumptions. The core of RED is a deadline-aware scheduler that assigns intermediate sub-deadlines, allowing it to accommodate evolving computation graphs and asynchronous inference induced by unpredictable conditions. The framework also supports flexible deployment of MIMONet (multi-input multi-output neural networks), commonly used in multi-tasking robots to alleviate memory pressure through weight sharing. RED explicitly leverages this shared-parameter property via a workload refinement and graph-reconstruction procedure that aligns MIMONet structure with schedulability requirements, improving compatibility and efficiency. We implement RED on NVIDIA Jetson family platforms and on an Apple M-series MacBook and evaluate it on navigation-oriented workloads representative of real robotic scenarios. Experiments show consistent gains over existing methods in throughput, deadline satisfaction, robustness to interference, adaptability, and runtime overhead.
