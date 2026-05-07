---
title: "Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2605.03208
priority: low
status: unread
interest: medium
next_step: skim
---
# Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs
> 原文: [https://arxiv.org/abs/2605.03208](https://arxiv.org/abs/2605.03208)

arXiv:2605.03208v2 Announce Type: new
Abstract: Iterative GPU kernel tuning is bottlenecked by the scale of the applications that host the kernels. Rapid iteration requires isolating the kernel so it can be edited, recompiled, and validated without rebuilding the full application -- but manual isolation requires reconstructing build flags, dispatch configuration, and runtime inputs by hand, so developers usually settle for slow in-place edits.
We present Kerncap, an automated kernel extraction tool that intercepts dispatches at the HSA runtime for both HIP and Triton, bridging Triton's JIT-only metadata into HSA-level capture via a lightweight Python compile-hook shim. Kerncap performs an address-space closure of all device memory -- a virtual-address-faithful snapshot that preserves embedded device pointers without DWARF metadata or pointer chasing -- locates kernel sources, and emits self-contained reproducer projects. HIP reproducers use a Clang VFS overlay for source-level recompilation without modifying the original build system; Triton reproducers are tuning-pinned, binding the captured autotuner configuration into the artifact to preserve the JIT kernel's numerical contract.
Across six real-world HIP and Triton workloads spanning traditional HPC and ML domains on three AMD GPU architectures (CDNA2, CDNA3, RDNA3), Kerncap extracts and validates kernels from snapshots ranging from 152~MB to 30~GB -- including a VA-faithful capture of vLLM's Mixture-of-Experts weight pool reached through pointer indirection. On our llama-cpp case study, Kerncap's edit-recompile-validate loop achieves a 13.6x speedup over the traditional workflow, reducing kernel isolation from a multi-hour process to a single command. The resulting reproducers also serve as a substrate for autotuning agents and LLM-driven kernel generators that need rapid, isolated evaluation of candidates.
