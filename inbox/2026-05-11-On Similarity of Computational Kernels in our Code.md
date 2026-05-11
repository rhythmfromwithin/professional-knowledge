---
interest: medium
link: https://arxiv.org/abs/2605.06968
next_step: skim
priority: medium
slack_ts: '1778472630.330089'
source: cs.DC - Distributed Computing
status: unread
title: On Similarity of Computational Kernels in our Codes and Proxies
---
# On Similarity of Computational Kernels in our Codes and Proxies
> 原文: [https://arxiv.org/abs/2605.06968](https://arxiv.org/abs/2605.06968)

arXiv:2605.06968v1 Announce Type: new
Abstract: As high-performance computing (HPC) systems rapidly evolve, with increasing on-node parallelism and widespread use of accelerators, understanding how the code maps to hardware is essential for reaching optimal performance. Benchmarks are commonly used for early assessment of emerging architectures (as well as for informing the design of future hardware), but it is often unknown how well the benchmarks represent the performance characteristics of simulation codes. Existing methods for evaluating how well our benchmarks represent our HPC codes are manual, labor intensive, and challenging to scale to many benchmarks. In this paper, we propose performance similarity metrics based on how the code uses the compute hardware. We define and characterize two broad categories of kernels that exhibit similar performance characteristics. We evaluate the pairwise similarity metrics on kernels in the Kripke proxy application and the RAJA Performance Suite, using both a CPU-only system and a GPU-accelerated system. We validate that our similarity metrics correctly match a kernel in the Kripke proxy app to a kernel in the RAJA Performance Suite. Our proposed similarity metrics enable assessment of the similarity of computational kernels in our codes and the proxy applications we use to represent the codes.
