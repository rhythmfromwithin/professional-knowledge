---
title: "Distributed training with Ray Train DLCs and EFA on EKS"
source: "AWS Blog"
link: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/
priority: high
status: unread
interest: medium
next_step: skim
---
# Distributed training with Ray Train DLCs and EFA on EKS
> 原文: [https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/](https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/)

The Ray Train Deep Learning Container ships the full CUDA-through-EFA stack, so you build no image. This post walks through a reproducible sample that fine-tunes Qwen2.5-1.5B with PyTorch FSDP across eight GPUs on two EFA-enabled g6.12xlarge instances on Amazon EKS, using the container exactly as published.
