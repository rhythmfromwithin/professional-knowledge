---
title: "VTC: DNN Compilation with Virtual Tensors for Data Movement Elimination"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.09558
priority: medium
status: unread
interest: medium
next_step: skim
---
# VTC: DNN Compilation with Virtual Tensors for Data Movement Elimination
> 原文: [https://arxiv.org/abs/2604.09558](https://arxiv.org/abs/2604.09558)

arXiv:2604.09558v1 Announce Type: new
Abstract: With the widening gap between compute and memory operation latencies, data movement optimizations have become increasingly important for DNN compilation. Current optimizations such as layout transformations and operator fusion only target a subset of tensor operators and consequently miss important opportunities for reducing data movement in contemporary DNN workloads, including large language models.
We introduce VTC, a novel tensor compilation framework that for the first time eliminates all unnecessary data movement by targeting the full spectrum of data movement operators. VTC proposes the concept of virtual tensors to track data movement between compute operators via index mappings rather than expensive physical data transfers to and from global memory, which can seamlessly interoperate with existing computation kernels and handle arbitrary tensor operator compositions. We also introduce a novel data movement elimination algorithm to automatically identify a profitable virtual tensor creation strategy. Evaluation on a variety of DNNs shows that VTC can outperform existing ML compilers by up to 1.93x (1.28x on average) on NVIDIA GPUs with up to 60% (17.5% on average) inference memory savings.
