---
interest: medium
link: https://arxiv.org/abs/2611.17824
next_step: skim
priority: medium
slack_ts: '1794900948.581939'
source: cs.DC - Distributed Computing
status: unread
title: 'TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement'
---
# TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement
> 原文: [https://arxiv.org/abs/2611.17824](https://arxiv.org/abs/2611.17824)

arXiv:2611.17824v1 Announce Type: new
Abstract: AI runtimes move state between NVMe storage and GPU memory on critical paths. GPUDirect Storage (GDS) removes host staging, yet our eight-H100 measurements show it is not consistently tail-optimal for semantically identical GPU-buffer operations. The preferred path varies with operation, request size, concurrency, placement, and resource contention; bandwidth and tail-latency winners can disagree. Frameworks specify what moves and when, while GPU I/O stacks expose mechanisms; neither combines phase semantics with measured tail behavior to choose a delivery plan.
We present TailGuard-GDS, a runtime that selects a semantically equivalent plan per application phase. It profiles plans varying backend, request shape, and placement, minimizes GPU-visible tail latency under phase constraints, and revisits decisions as conditions change. Resource reuse keeps policy lookup and switching at microsecond-scale overhead.
Integrated with PyTorch FSDP and DeepSpeed ZeRO-3, TailGuard reduces FSDP step p95 by 18.4% and GPU-idle p95 by 25.3% versus the strongest fixed path. Across five eight-GPU ZeRO-3 workloads, step p95 falls 7.9-24.6% versus fixed host staging and 28.4-42.6% versus fixed GDS. Against tuned DeepSpeed AIO, TailGuard reduces step p95 by 5.6% and raises estimated throughput by 6.1%.
