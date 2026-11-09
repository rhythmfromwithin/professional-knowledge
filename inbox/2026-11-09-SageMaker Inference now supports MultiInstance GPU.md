---
title: "SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints"
source: "AWS Blog"
link: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/
priority: high
status: unread
interest: medium
next_step: skim
---
# SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints
> 原文: [https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/](https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/)

Amazon SageMaker Inference now supports GPU partitioning with NVIDIA Multi-Instance GPU (MIG), which divides one GPU into hardware-isolated partitions so you can run a different model in each or take a right-sized fraction of a newer accelerator. This post shows how two optional API fields place one model per partition, and what we measured against a whole older GPU.
