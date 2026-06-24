---
title: "The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.23969
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing
> 原文: [https://arxiv.org/abs/2606.23969](https://arxiv.org/abs/2606.23969)

arXiv:2606.23969v1 Announce Type: new
Abstract: GPU Confidential Computing (GPU-CC) now preserves GPU-local performance: on NVIDIA B300, BF16 matmul runs at 0.998x of non-confidential performance. Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. This paper studies that gap on two Blackwell platforms, RTX Pro 6000 and B300 HGX, and identifies its dominant cause: the confidential VM-GPU bridge, not GPU compute.
We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. Secure copies do not gain CUDA-stream concurrency within a context, asynchronous transfers block at the runtime boundary, and small crossings pay a fixed toll. This violates the assumptions of modern inference runtimes, where DMA is expected to be cheap, concurrent, and asynchronous. In vLLM dense decode, the gap closes around 44x-slower small alloc-and-copy operations; targeted patches reject alternative explanations. A scheduling flag recovers 57% of the gap, while a worker-thread drain recovers up to 92% in qualified high-concurrency runs. The same bridge model explains a +131% KV-restore penalty and a 34x model-load slowdown.
Blackwell also changes the confidential tenancy unit. We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms.
