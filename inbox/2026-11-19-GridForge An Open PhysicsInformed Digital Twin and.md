---
title: "GridForge: An Open Physics-Informed Digital Twin and Benchmark Suite for UK 11 kV Underground Distribution Cables"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2611.23241
priority: high
status: unread
interest: medium
next_step: skim
---
# GridForge: An Open Physics-Informed Digital Twin and Benchmark Suite for UK 11 kV Underground Distribution Cables
> 原文: [https://arxiv.org/abs/2611.23241](https://arxiv.org/abs/2611.23241)

arXiv:2611.23241v1 Announce Type: new
Abstract: The UK distribution-cable monitoring sector is data-rich but framework-poor: each Distribution Network Operator (DNO) collects megabytes of telemetry per asset per day, but there is no public benchmark dataset, no shared reference model, and no commonly agreed evaluation protocol for benchmarking sectoral, data-intensive models for operational decision support; notably for maintenance planning and prioritisation. We address this gap with GridForge, an open-source physics-informed digital twin and benchmark suite for fault diagnosis and prediction, integrating four building blocks: (i) a verified steady state and transient thermal model based on IEC 60287 and IEC 60853; (ii) a calibrated synthetic dataset of 64 cables (covering 320 cable-years) representing four canonical UK 11 kV thermal archetypes and four condition modes; (iii) a Physics-Informed Neural Network (PINN) surrogate that satisfies the algebraic balance defined by IEC 60287 during training and reaches an RMSE of 0.148 {\deg}C on an independent held out set against the reference analytical oracle; and (iv) a five-task benchmark suite that includes three reference baseline models (pure physics, gradient-boosted trees, and the PINN). All numerical parameters are sourced from public standards, the code is licensed under the MIT licence, and the trained PINN converges in only two minutes (as run on the computing platform in Section 10.1), enabling independent verification by DNO engineering and research practitioners. At present only the virtual-sensor task (T4) discriminates between the reference baselines; the other tasks tie or are undefined on this test split, so extending the baselines with task-specific logic is a priority future enhancement. For open validation, the dataset, test sets and models are made available at https://github.com/mlily2024/Gridforge
