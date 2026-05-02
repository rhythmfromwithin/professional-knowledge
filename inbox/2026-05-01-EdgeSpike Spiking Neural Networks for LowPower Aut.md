---
interest: medium
link: https://arxiv.org/abs/2604.27004
next_step: skim
priority: low
slack_ts: '1777692909.159279'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'EdgeSpike: Spiking Neural Networks for Low-Power Autonomous Sensing in Edge
  IoT Architectures'
---
# EdgeSpike: Spiking Neural Networks for Low-Power Autonomous Sensing in Edge IoT Architectures
> 原文: [https://arxiv.org/abs/2604.27004](https://arxiv.org/abs/2604.27004)

arXiv:2604.27004v1 Announce Type: new
Abstract: We propose EdgeSpike, a co-designed spiking neural network (SNN) framework for autonomous low-power sensing in edge Internet of Things (IoT) architectures. EdgeSpike unifies (i) a hybrid surrogate-gradient and direct-encoding training pipeline, (ii) a hardware-aware neural architecture search (NAS) bounded by per-inference energy and memory budgets, (iii) an event-driven runtime targeting Intel Loihi 2, SpiNNaker 2, and commodity ARM Cortex-M microcontrollers with custom spike-sparse SIMD kernels, and (iv) a lightweight local plasticity rule enabling continual on-device adaptation without backpropagation. The framework is evaluated across five sensing tasks (keyword spotting, vibration-based machine fault detection, surface electromyography gesture recognition, 77 GHz radar human-activity classification, and structural-health acoustic-emission monitoring) on three hardware targets. EdgeSpike achieves a mean classification accuracy of 91.4%, within 1.2 percentage points (pp) of strong INT8 convolutional neural network (CNN) baselines (mean 92.6%), while reducing energy per inference by 18x to 47x on neuromorphic hardware (mean 31x) and by 4.6x to 7.9x on Cortex-M (mean 6.1x). End-to-end latency remains at or below 9.4 ms across all 15 task-hardware configurations. A seven-month, 64-node wireless field deployment confirms a 6.3x extension in projected battery lifetime (from 312 to 1978 days at 2 Wh per node) and bounded accuracy degradation under seasonal drift (0.7 pp with on-device adaptation versus 2.1 pp without). Hardware-aware NAS evaluates 8400 candidates and yields a 12-point Pareto front. EdgeSpike will be released as open source with reproducible training pipelines, hardware-portable runtimes, and benchmark suites.
