---
interest: medium
link: https://arxiv.org/abs/2604.20032
next_step: skim
priority: medium
slack_ts: '1777087204.800239'
source: cs.DC - Distributed Computing
status: unread
title: 'LEO: Tracing GPU Stall Root Causes via Cross-Vendor Backward Slicing'
---
# LEO: Tracing GPU Stall Root Causes via Cross-Vendor Backward Slicing
> 原文: [https://arxiv.org/abs/2604.20032](https://arxiv.org/abs/2604.20032)

arXiv:2604.20032v1 Announce Type: new
Abstract: More than half of the Top 500 supercomputers employ GPUs as accelerators. On GPU-accelerated platforms, developers face a key diagnostic gap: profilers show source lines where stalls occur, but not why they occur. Furthermore, the same kernel may have different stalls and underlying causes on different GPUs. This paper presents LEO, a root-cause analyzer for NVIDIA, AMD, and Intel GPUs that performs backward slicing from stalled instructions, considering dependencies arising from registers as well as vendor-specific synchronization mechanisms. LEO attributes GPU stalls to source instructions with the goal of explaining root causes of these inefficiencies. Across 21 workloads on three GPU platforms, LEO-guided optimizations deliver geometric-mean speedups of 1.73$\times$--1.82$\times$. Our case studies show that (1) the same kernel may require different optimizations for different GPU architectures, and (2) LEO's structured diagnostics improve code optimization with large language models relative to code-only and raw-stall-count baselines.
