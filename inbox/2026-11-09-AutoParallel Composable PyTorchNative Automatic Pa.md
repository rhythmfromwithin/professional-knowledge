---
title: "AutoParallel: Composable, PyTorch-Native Automatic Parallelism for Production Training"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.08660
priority: medium
status: unread
interest: medium
next_step: skim
---
# AutoParallel: Composable, PyTorch-Native Automatic Parallelism for Production Training
> 原文: [https://arxiv.org/abs/2611.08660](https://arxiv.org/abs/2611.08660)

arXiv:2611.08660v1 Announce Type: new
Abstract: Training large models requires multiple interacting forms of parallelism. As models and clusters scale, finding and maintaining efficient parallelization plans becomes essential for training performance. Diverse model architectures, workloads, and hardware topologies demand flexible strategies, yet production PyTorch systems typically rely on hand-written recipes that are costly to adapt and tend to reuse familiar patterns, which may be suboptimal for a given workload. We present AutoParallel, a PyTorch-native planner for distributed model training. AutoParallel searches parallelization choices jointly across the training computation, allowing established techniques to be combined and unconventional strategies to emerge. It expresses its decisions using native PyTorch abstractions and produces ordinary PyTorch programs, avoiding a separate execution runtime while composing directly with the PyTorch compilation and training stack. AutoParallel also composes automatic decisions with model-specific distributed code, allowing dynamic or specialized regions to remain under user control. Plans are inspectable and replayable artifacts. Across dense, hybrid, and mixture-of-experts models on meshes of up to four dimensions and 128 NVIDIA H100 GPUs, AutoParallel matches or exceeds expert-written TorchTitan recipes on most configurations, with throughput gains of up to 18.3%, and discovers plans that uniform expert recipes do not express.
