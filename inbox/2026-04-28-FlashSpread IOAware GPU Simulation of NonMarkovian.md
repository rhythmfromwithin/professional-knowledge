---
title: "FlashSpread: IO-Aware GPU Simulation of Non-Markovian Epidemic Dynamics via Kernel Fusion"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.22092
priority: medium
status: unread
interest: medium
next_step: skim
---
# FlashSpread: IO-Aware GPU Simulation of Non-Markovian Epidemic Dynamics via Kernel Fusion
> 原文: [https://arxiv.org/abs/2604.22092](https://arxiv.org/abs/2604.22092)

arXiv:2604.22092v1 Announce Type: new
Abstract: Non-Markovian (renewal) epidemic simulation on multi-million-node contact networks is essential for realistic forecasting under general age-dependent holding-time distributions (log-normal, Weibull, Erlang, and similar), but the age-dependent hazard forces dense per-step updates that render the sparse event-queue strategies of standard CPU methods ineffective. We present FlashSpread, a GPU framework that consolidates the per-step renewal pipeline (CSR traversal, numerically stable erfcx-based hazard evaluation, Bernoulli tau-leaping, state transition, and next-step infectivity write-back) into a single fused Triton kernel whose intermediates never leave streaming-multiprocessor registers, with block-scalar skips that preserve CUDA Graph capture and a degree-aware CSR dispatch (thread / warp / edge-merge) that keeps the peak throughput on scale-free graphs. On an NVIDIA A100 the fused CUDA-Graph engine reaches 8.09 Giga-NUPS at N = 10^6 on a uniform-degree graph, a 217x strict hardware speedup over optimised CPU tau-leaping at the same N; on a Barabasi-Albert graph of the same size the merge-based dispatch recovers 4.5x (0.45 to 2.0 Giga-NUPS) over the default kernel, and the framework scales to N = 10^8 on a single A100 (40 GB), with a mixed-precision storage path that extends the L2-reachable scale by roughly 3x and delivers a 1.15x throughput lift at the far bandwidth-bound end. Validation against an exact non-Markovian Gillespie reference shows a structural-bias floor of approximately 6% on peak infection and approximately 7% on final attack rate that does not detectably decrease as epsilon nears 0 across two decades of tolerance, comfortably within typical epidemiological parameter uncertainty. Code: https://github.com/Shakeri-Lab/FlashSpread.
