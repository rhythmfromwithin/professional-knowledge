---
interest: medium
link: https://arxiv.org/abs/2604.22126
next_step: skim
priority: medium
slack_ts: '1777434577.412549'
source: cs.DC - Distributed Computing
status: unread
title: 'GICC: A High-Performance Runtime for GPU-Initiated Communication and Coordination
  in Modern HPC Systems'
---
# GICC: A High-Performance Runtime for GPU-Initiated Communication and Coordination in Modern HPC Systems
> 原文: [https://arxiv.org/abs/2604.22126](https://arxiv.org/abs/2604.22126)

arXiv:2604.22126v1 Announce Type: new
Abstract: Distributed GPU applications increasingly rely on kernel-level, cross-node coordination to reduce launch overheads and improve compute-communication overlap, but such support is lacking. On OFI-based interconnects such as HPE Slingshot, which powers six of the top ten systems in the November 2025 Top500, including the top three, GPU kernels cannot autonomously drive distributed coordination: existing runtimes rely on host-driven progress and lack a bounded mechanism for recycling pre-staged NIC work across repeated GPU-triggered operations. On InfiniBand, GPU-initiated communication is possible, but current implementations incur unnecessary synchronization and locking overheads.
This paper presents GICC, a framework that enables GPU kernels to directly trigger NIC-level operations without host involvement on the fast path. In stencils, GPU threads initiate halo exchanges as soon as boundary regions are computed, enabling fine-grained overlap between interior computation and boundary transfer. GICC decouples coordination semantics from data movement and introduces asynchronous resource reclamation: the NIC signals completion to both GPU and host memory, letting a lightweight host thread recycle NIC resources concurrently with GPU execution without injecting latency into the coordination path. This sustains GPU-driven coordination under finite NIC state, absent from existing OFI-based runtimes.
We implement GICC on NVIDIA and AMD GPUs over InfiniBand and Slingshot. On Slingshot, GICC reduces per-coordination latency by up to 229x and improves weak scaling efficiency by up to 25%. On InfiniBand, it achieves up to 1.95x lower put latency than NVSHMEM by eliminating unnecessary locking and synchronization. On an industrial stencil proxy on 64 AMD MI250X GCDs, GPU-aware MPI incurs over 52% higher communication time than GICC, which achieves 42% parallel efficiency versus MPI's 35.4%.
