---
title: "LiteVLA-Edge: Quantized On-Device Multimodal Control for Embedded Robotics"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.03380
priority: medium
status: unread
---
# LiteVLA-Edge: Quantized On-Device Multimodal Control for Embedded Robotics
> 原文: [https://arxiv.org/abs/2603.03380](https://arxiv.org/abs/2603.03380)

arXiv:2603.03380v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models provide a unified framework for perception, language conditioning, and action generation, but many existing systems remain difficult to deploy in embedded robotic settings because of their computational requirements and inference latency. In this paper, we present LiteVLA-Edge, a deployment-oriented VLA pipeline for fully on-device inference on Jetson Orin-class hardware. Our approach combines supervised image-to-action fine-tuning in FP32 with post-training 4-bit GGUF quantization and GPU-accelerated inference through the \texttt{llama.cpp} runtime. Under our deployment configuration, LiteVLA-Edge achieves a mean end-to-end latency of 150.5\,ms (approximately 6.6\,Hz) while operating entirely offline within a ROS~2-integrated perception--reasoning--action pipeline. Rather than introducing a new policy objective, our contribution is a practical systems path for executing compact multimodal control models locally on embedded hardware while preserving modular interfaces between perception, reasoning, and actuation. These results establish timing feasibility for reactive language-conditioned control and provide a reproducible baseline for future task-level evaluation of on-device VLAs in robotics.
