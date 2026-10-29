---
interest: medium
link: https://arxiv.org/abs/2610.33358
next_step: skim
priority: low
slack_ts: '1793251497.774679'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'MOSHO: A Native Discrete Shark-Inspired Metaheuristic for Hardware-Aware Neural
  Architecture Search'
---
# MOSHO: A Native Discrete Shark-Inspired Metaheuristic for Hardware-Aware Neural Architecture Search
> 原文: [https://arxiv.org/abs/2610.33358](https://arxiv.org/abs/2610.33358)

arXiv:2610.33358v1 Announce Type: new
Abstract: Hardware-aware neural architecture search (NAS) requires jointly optimizing predictive accuracy and device-specific latency over discrete search spaces. While multi-objective swarm optimizers show promise, continuous formulations such as the Multi-Objective White Shark Optimizer (MOWSO) can suffer from quantization noise when rounded to integer-encoded architecture vectors. To address this limitation, we propose MOSHO (Multi-Objective Shark Hunting Optimization), a native discrete metaheuristic that replaces continuous motion equations with discrete architecture-editing operators. MOSHO integrates adaptive operator scheduling, energy-regulated restarts, and deferred crowding-distance truncation to enhance exploration and search efficiency. On the merged NAS-Bench-201/HW-NAS-Bench benchmark across 18 contexts, MOSHO achieves a median normalized hypervolume of 0.9987 and IGD+ of 0.0064, yielding Pareto fronts competitive with NSGA-II while reducing search runtime by 96.4% (0.64 s vs. 17.72 s). These results demonstrate that tailored discrete search mechanisms can enable swarm optimizers to achieve high-quality multi-objective solution quality with substantially lower search cost in hardware-aware NAS.
