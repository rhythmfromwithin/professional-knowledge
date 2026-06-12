---
interest: medium
link: https://arxiv.org/abs/2606.12753
next_step: skim
priority: medium
slack_ts: '1781239686.533739'
source: cs.DC - Distributed Computing
status: unread
title: On the Limits of Performance Portability in Directive-Based GPU Programming
---
# On the Limits of Performance Portability in Directive-Based GPU Programming
> 原文: [https://arxiv.org/abs/2606.12753](https://arxiv.org/abs/2606.12753)

arXiv:2606.12753v1 Announce Type: new
Abstract: The transition of scientific applications to GPU-accelerated exascale systems is constrained by trade-offs between performance, portability, and productivity. This work evaluates the performance portability of directive-based GPU programming by porting gPLUTO, a production-grade magnetohydrodynamics code for astrophysical simulations, from OpenACC to OpenMP, and analyzing its performance on NVIDIA A100 (Leonardo Booster) and AMD MI250X (LUMI-G) devices. On NVIDIA platforms, OpenACC and OpenMP achieve comparable performance due to a shared compiler backend, providing a consistent baseline for assessing algorithmic efficiency. In contrast, the same OpenMP implementation is approximately three times slower at the application level on AMD MI250X with respect to the NVIDIA A100 OpenACC baseline, with kernel-level slowdowns reaching up to an order of magnitude, driven by sensitivity to strided memory-access patterns and compiler limitations. Kernel-level profiling shows that the dominant contributors to run-time are memory-latency-bound rather than limited by peak band-width. In low-parallelism kernels, C++ abstraction layers increase register pressure and spilling, leading to extreme slowdowns of up to 47x in specific cases. These results indicate that portable performance across GPU architectures requires not only application-level changes but also continued advances in compiler backends and architecture-aware optimization strategies
