---
interest: medium
link: https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/
next_step: skim
priority: high
slack_ts: '1789619673.761619'
source: AWS Blog
status: unread
title: Fault tolerant distributed training on Amazon EKS using NVRx
---
# Fault tolerant distributed training on Amazon EKS using NVRx
> 原文: [https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/](https://aws.amazon.com/blogs/machine-learning/fault-tolerant-distributed-training-on-amazon-eks-using-nvrx/)

Integrate NVIDIA Resiliency Extension (NVRx) into PyTorch FSDP training on Amazon EKS to overlap checkpoint I/O with training and recover from GPU faults in seconds. This post covers async checkpointing, in-process restart, and ft\_launcher in-job restart, with H100 benchmarks at 2 to 8 nodes showing 99%+ training efficiency and second-scale recovery.
