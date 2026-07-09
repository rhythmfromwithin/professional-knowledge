---
interest: medium
link: https://arxiv.org/abs/2607.05596
next_step: skim
priority: medium
slack_ts: '1783569525.617489'
source: cs.DC - Distributed Computing
status: unread
title: Bounded-Memory Parallel Image Pulling for Large Container Images
---
# Bounded-Memory Parallel Image Pulling for Large Container Images
> 原文: [https://arxiv.org/abs/2607.05596](https://arxiv.org/abs/2607.05596)

arXiv:2607.05596v1 Announce Type: new
Abstract: AI/ML workloads increasingly run as containers, where a container image must be downloaded to the host before the workload can start. This cold image pull lands on the critical path whenever a training or inference job scales up or a host is updated, and for GPU workloads it has become the dominant component of startup time as AI/ML images reach 31--48~GiB compressed. We present Disk-Backed Parallel Pull (DBPP), an alternative to the in-memory ordered reassembly used by containerd~2.2, the upstream container runtime. containerd splits layers into chunks fetched concurrently over HTTP range requests, but chunks that arrive out of order accumulate in the runtime heap until a sequential consumer drains them in order. This backlog grows with image size, and on GPU nodes where host memory is shared with frameworks and model weights, it leads to out of memory (OOM) termination of the runtime itself. DBPP writes each chunk directly to its target byte offset on disk, eliminating the ordering dependency and bounding memory regardless of image size. Because each layer lands on disk as a complete, seekable file, DBPP runs SHA-256 digest verification and decompression simultaneously, two passes containerd must run one after the other. In controlled experiments across five production-scale images (up to 48.5~GiB), DBPP reduces peak daemon memory by 8.7--25.3$\times$ while maintaining comparable pull throughput. On a memory-constrained node, containerd~2.2 is OOM-killed pulling a 31.4~GiB image while DBPP completes the same pull. The underlying idea reaches past container images: any pipeline that buffers data in memory only to enforce ordering can move that buffer to disk once the backing store is fast enough, trading a scarce, contended resource for an abundant one.
