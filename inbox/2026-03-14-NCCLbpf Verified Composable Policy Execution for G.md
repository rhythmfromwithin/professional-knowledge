---
interest: medium
link: https://arxiv.org/abs/2603.11438
next_step: skim
priority: medium
slack_ts: '1773802302.539239'
source: cs.DC - Distributed Computing
status: unread
title: 'NCCLbpf: Verified, Composable Policy Execution for GPU Collective Communication'
---
# NCCLbpf: Verified, Composable Policy Execution for GPU Collective Communication
> 原文: [https://arxiv.org/abs/2603.11438](https://arxiv.org/abs/2603.11438)

arXiv:2603.11438v1 Announce Type: new
Abstract: NCCL is the de facto standard for collective GPU communication in large-scale distributed training, relying heavily on plugins to customize runtime behavior. However, these plugins execute as unverified native code within NCCL's address space, risking job crashes, silent state corruption, and downtime from restarts during policy updates. Inspired by kernel extensibility models, we introduce NCCLbpf, a verified, high-performance extension framework embedding a userspace eBPF runtime directly into NCCL's existing plugin interfaces, without modifying NCCL itself. NCCLbpf offers load-time static verification to prevent unsafe plugin execution, structured cross-plugin maps enabling composable policies and closed-loop adaptation, and atomic policy hot-reloads eliminating downtime previously required for policy updates. Evaluations on 8x NVIDIA B300 GPUs connected via NVLink demonstrate that NCCLbpf imposes just 80-130 ns overhead per tuner decision (less than 0.03% of collective latency), prevents all tested unsafe plugin behaviors at load-time, and enables a message-size-aware eBPF policy that improves AllReduce throughput by up to 27% over NCCL's default in the 4-128 MiB range.
