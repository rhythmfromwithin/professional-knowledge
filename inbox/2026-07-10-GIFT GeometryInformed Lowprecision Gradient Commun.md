---
title: "GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.07494
priority: medium
status: unread
interest: medium
next_step: skim
---
# GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining
> 原文: [https://arxiv.org/abs/2607.07494](https://arxiv.org/abs/2607.07494)

arXiv:2607.07494v1 Announce Type: new
Abstract: Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion. We present GIFT, a geometry-informed gradient scaling method that performs low-precision communication in geometry-aware coordinates. By transforming gradients into a near-isotropic space before quantization, GIFT makes low-precision representations substantially more faithful to their high-precision counterparts. GIFT only changes the coordinate system used for low-precision gradient communication and does not change the optimizer, training recipe, communication collective, or low-precision format. We also develop a simplified geometry-aware transformation algorithm with low-rank approximation and selective application to balance the computation overhead and communication reduction. We examine the empirical convergence of GIFT using Llama-300M and Llama-600M models. Our results show that GIFT reduces the end-to-end pretraining time of Llama-600M by 7.6% on 64 NVIDIA GH200 Superchips, while improving the downstream task preservation profile over direct Euclidean FP8 communication under the same optimizer and communication path.
