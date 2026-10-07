---
interest: medium
link: https://arxiv.org/abs/2610.04037
next_step: skim
priority: medium
slack_ts: '1791351184.039419'
source: cs.DC - Distributed Computing
status: unread
title: 'BitIR: Cross-Architecture Fault Injection for Resilience Analysis of Heterogeneous
  GPU Applications'
---
# BitIR: Cross-Architecture Fault Injection for Resilience Analysis of Heterogeneous GPU Applications
> 原文: [https://arxiv.org/abs/2610.04037](https://arxiv.org/abs/2610.04037)

arXiv:2610.04037v1 Announce Type: new
Abstract: Modern GPU-based HPC systems rely on heterogeneous vendor stacks, yet resilience studies are largely limited to single architectures, leaving it unclear how faults behave across different GPU backends. We present \emph{BitIR}, a cross-architecture fault injection framework that injects deterministic single-bit faults at the LLVM IR level, ensuring semantically equivalent perturbations prior to backend lowering and enabling direct cross-vendor comparison across NVIDIA, Intel, and AMD GPUs. We evaluate BitIR on three production supercomputers -- Polaris (ALCF, NVIDIA A100), Aurora (ALCF, Intel GPU Max 1550), and Frontier (OLCF, AMD Instinct MI250X) -- representing the full spectrum of current leadership-class GPU architectures. Using representative heterogeneous benchmarks, we conduct large-scale injection campaigns across all three systems and classify outcomes into masked results, silent data corruptions (SDCs), and failures. Our results show that identical faults produce markedly different behaviors across vendors: Intel most often masks faults but exhibits more hangs when faults escape masking, NVIDIA exposes more detectable hard failures, and AMD alternates between SDC-dominant and failure-dominant behavior depending on the benchmark and fault site. These findings demonstrate that resilience is not backend-invariant, underscoring the need for backend-aware and workload-aware fault mitigation.
