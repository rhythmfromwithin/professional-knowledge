---
interest: medium
link: https://arxiv.org/abs/2606.23891
next_step: skim
priority: medium
slack_ts: '1782274338.333269'
source: cs.DC - Distributed Computing
status: unread
title: Memory Layouts for GPU-Data Transfer Buffering in SPH
---
# Memory Layouts for GPU-Data Transfer Buffering in SPH
> 原文: [https://arxiv.org/abs/2606.23891](https://arxiv.org/abs/2606.23891)

arXiv:2606.23891v1 Announce Type: new
Abstract: The rise in GPU compute speed has outpaced improvements in host-to-device memory transfer speeds, despite the advent of shared-memory superchips. Consequently, memory transfer times now constitute an increasingly large fraction of total time-to-solution, compelling developers to compress GPU kernel input and output data into compact, minimal formats prior to GPU-offloading. This complements existing work on GPU- and compute-friendly data arrangements. We study a Smoothed Particle Hydrodynamics solver and propose memory layout strategies for host-side particle data that are particularly well-suited to GPU-offloading. Specifically, we advocate splitting classic array-of-struct data structures into a split array-of-struct arrangement, in which each logical struct decomposes into substructs determined by kernel read/write access patterns and attribute types. Splitting a monolithic particle struct into several bespoke, finer-grained structs can reduce the time required to pack data to and from buffers by ~20% - 40%, lowering total time spent on GPU-offloading by ~12% - 25%.
