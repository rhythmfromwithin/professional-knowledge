---
interest: medium
link: https://arxiv.org/abs/2606.14007
next_step: skim
priority: medium
slack_ts: '1781586962.969289'
source: cs.DC - Distributed Computing
status: unread
title: 'VaultxGPU: GPU-Accelerated Blockchain Consensus'
---
# VaultxGPU: GPU-Accelerated Blockchain Consensus
> 原文: [https://arxiv.org/abs/2606.14007](https://arxiv.org/abs/2606.14007)

arXiv:2606.14007v1 Announce Type: new
Abstract: Blockchain consensus mechanisms based on Proof-of-Work consume significant energy, with Bitcoin alone estimated at approximately 150 TWh per year. Proof-of-Space reduces this cost by replacing repeated computation with storage, but plot generation remains bottlenecked by CPU hashing throughput. Prior work on VaultX demonstrated a high-performance CPU-based Proof-of-Space plotter using multi-threaded Blake3 hashing, achieving plotting speeds 4 to 50x faster than Chia depending on hardware configuration. In this paper, we present VaultxGPU, a GPU-accelerated extension of the VaultX plotter that offloads the Blake3 hashing pipeline to the GPU using custom kernels. We implement the plotter in both CUDA for NVIDIA hardware and SYCL for AMD and Intel GPUs, keeping Table 1 entirely in GPU VRAM and fusing the sort and match stages into a single kernel to minimize data movement. We evaluate VaultxGPU across K-values 27 through 31 against CPU baselines. Our SYCL GPU implementation achieves a 59.2x speedup over a single-threaded CPU baseline, completing a K=31 plot in 45.4 seconds compared to 2688 seconds, and outperforms even the best 384-thread CPU configuration. These results confirm that GPU acceleration is the correct direction for scaling Proof-of-Space plotting beyond what CPU parallelism can achieve.
