---
title: "uGDS: A User-Space Development Kit for High-Performance GPU Direct Storage"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.30868
priority: medium
status: unread
interest: medium
next_step: skim
---
# uGDS: A User-Space Development Kit for High-Performance GPU Direct Storage
> 原文: [https://arxiv.org/abs/2610.30868](https://arxiv.org/abs/2610.30868)

arXiv:2610.30868v1 Announce Type: new
Abstract: Data-intensive GPU applications increasingly rely on NVMe SSDs to extend GPU memory. NVIDIA GPU Direct Storage (GDS) enables direct SSD-GPU transfers via PCIe peer-to-peer DMA, eliminating host staging. However, GDS retains three key limitations: (1) its control path traverses the kernel for every I/O request, introducing software overhead; (2) its stream-ordered path imposes strict total ordering even when workloads only require batch-level ordering; and (3) its closed-source user-space engine hinders diagnosis and custom scheduling.
We present uGDS, https://github.com/ScaleX-IO/uGDS, an open-source user-space GPU Direct Storage library built on four principles: user-space control, unified cross-vendor abstraction, workload-aware scheduling, and end-to-end transparency. The host CPU manages the entire NVMe command lifecycle in user space, while payloads move via PCIe P2P DMA without consuming GPU compute. A minimal kernel module (ugds\_drv.ko) is used only for one-time privileged setup. uGDS partitions hardware queues between synchronous and batch traffic, enforces DMA-safe buffer lifetimes, and provides cuFile-compatible synchronous, batched, and stream-ordered APIs with polling or interrupt completion on both NVIDIA CUDA and AMD HIP.
Evaluated on an A100 with a Samsung 990 PRO, uGDS achieves up to 12.12x GDS's batch-read bandwidth and 30.69x its batch-write bandwidth (8- and 4-KiB requests, batch size 128), and reduces 4-KiB synchronous write latency by 84.1% with two threads. Its stream-ordered path sustains 5.49 GiB/s on a single stream, where GDS retains only 40.8% of its synchronous bandwidth. In LMCache, uGDS reduces median time-to-first-token (TTFT) by up to 62.7% and raises serving goodput by 2.63x. On AMD, uGDS achieves up to 1.19x hipFile's synchronous-write bandwidth.
