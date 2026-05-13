---
title: "ShardTensor: Domain Parallelism for Scientific Machine Learning"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.11111
priority: medium
status: unread
interest: medium
next_step: skim
---
# ShardTensor: Domain Parallelism for Scientific Machine Learning
> 原文: [https://arxiv.org/abs/2605.11111](https://arxiv.org/abs/2605.11111)

arXiv:2605.11111v1 Announce Type: new
Abstract: Scientific Machine Learning (SciML) faces unique challenges for extreme-resolution data, with mitigations that often fail to scale or degrade the accuracy of trained models. While some specialized methods have achieved remarkable results in training models or performing inference on massive spatial datasets with bespoke techniques, there is no generalized framework for parallelization over input data below batch size one per device. In this work we introduce ShardTensor: a novel paradigm of domain parallelism that enables flexible scaling of input data to arbitrary sizes. By decoupling the spatial dimensionality of input data from hardware constraints, ShardTensor enables scientific machine learning workloads to reach new levels of high fidelity training and inference. We demonstrate both strong and weak scaling of workloads during training and inference, showing improved latency with strong scaling and demonstrating the capacity to process higher data sizes with weak scaling. Additionally, we demonstrate multiple dimensions of parallelization, removing barriers to SciML on extreme-scale inputs.
