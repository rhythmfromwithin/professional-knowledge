---
title: "The Fabric Is the Cluster Driver: Cross-Layer eBPF Policies for GPU-CXL Fabrics"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.26335
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Fabric Is the Cluster Driver: Cross-Layer eBPF Policies for GPU-CXL Fabrics
> 原文: [https://arxiv.org/abs/2607.26335](https://arxiv.org/abs/2607.26335)

arXiv:2607.26335v1 Announce Type: new
Abstract: We present fabric\_ext, an eBPF middleware compiler and runtime for extensible OS policies over GPU--CXL fabrics. fabric\_ext lets one policy program execute across GPU hooks, driver/runtime hooks, DPU/NIC hooks, and CXL switch or near-memory hooks. The key abstraction is a semantic movement graph: edges describe bytes, stride, reuse distance, read/write ratio, source and destination, ordering requirement, alias set, ownership, and transformations such as Move, Quantize, Compress, Checksum, Filter, Reduce, Scatter/Gather, Replicate, and Persist. The compiler lowers this graph into per-device eBPF programs, verifier obligations, consistency-classed BPF maps, and artifacts for bpftime and dputime. At the fabric edge, fabric\_ext treats a near-Type-2 small core as a hardware-JIT and state manager: it specializes verified movement descriptors into local copy, placement, ordering, and transformation commands, while the surrounding Von Neumann island of memory, DMA, and compute engines performs the dataflow. Because this dataflow is data-driven, fabric\_ext also places observation beside the island, where queues, DMA completions, memory placement, and ownership transitions are visible as they happen. The canonical stress case is LLM prefill: attention streams KV blocks and reductions while FFN streams activations, weights, and compressible intermediates, forcing one request to cross GPU tensor execution, DPU/NIC event execution, and CXL or switch-local dataflow islands.
